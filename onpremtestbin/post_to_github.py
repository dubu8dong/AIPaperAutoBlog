import os
import json
import base64
import argparse
from pathlib import Path
from typing import Optional, Tuple

import requests


# ============================================================
# GitHub 설정 (맨 앞에 변수로 고정 / 필요하면 여기만 보면 됨)
#  - 환경변수로도 덮어쓸 수 있게 처리했음 (Azure Function 배포용)
# ============================================================

GITHUB_TOKEN  = os.getenv("GITHUB_TOKEN",  "ghp_PASTE_YOUR_TOKEN_HERE")
GITHUB_OWNER  = os.getenv("GITHUB_OWNER",  "dubudong")
GITHUB_REPO   = os.getenv("GITHUB_REPO",   "AIpaperAutoBlog")
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "main")

# 업로드 위치(레포 안 경로)
GITHUB_POSTS_DIR = os.getenv("GITHUB_POSTS_DIR", "posts")


# ------------------ utils ------------------

def die(msg: str) -> None:
    raise SystemExit(msg)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def b64_utf8(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def guess_title_from_md(md_text: str) -> str:
    """
    Markdown 첫 번째 '# ' 헤더를 제목으로 사용.
    없으면 파일명을 사용.
    """
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def gh_headers(token: str) -> dict:
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


def gh_contents_url(owner: str, repo: str, path: str) -> str:
    # path는 URL-safe 형태로 들어가야 하는데, 대부분 posts/... 정도면 문제 없음
    return f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"


def get_existing_file_sha(
    *,
    owner: str,
    repo: str,
    branch: str,
    token: str,
    repo_path: str,
) -> Optional[str]:
    """
    파일이 이미 존재하면 sha를 반환 (update에 필요)
    없으면 None 반환
    """
    url = gh_contents_url(owner, repo, repo_path)
    r = requests.get(url, headers=gh_headers(token), params={"ref": branch}, timeout=30)

    if r.status_code == 404:
        return None
    if r.status_code >= 400:
        die(f"[GET sha] GitHub API error {r.status_code}\n{r.text}")

    data = r.json()
    return data.get("sha")


def create_or_update_file(
    *,
    owner: str,
    repo: str,
    branch: str,
    token: str,
    repo_path: str,
    content_text: str,
    commit_message: str,
) -> Tuple[str, str]:
    """
    PUT /repos/{owner}/{repo}/contents/{path}
    - 새 파일이면 create
    - 기존 파일이면 sha 포함해서 update
    반환: (file_html_url, commit_sha)
    """
    url = gh_contents_url(owner, repo, repo_path)

    sha = get_existing_file_sha(
        owner=owner, repo=repo, branch=branch, token=token, repo_path=repo_path
    )

    payload = {
        "message": commit_message,
        "content": b64_utf8(content_text),
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha

    r = requests.put(url, headers=gh_headers(token), data=json.dumps(payload), timeout=30)
    if r.status_code >= 400:
        die(f"[PUT] GitHub API error {r.status_code}\nURL: {url}\n{r.text}")

    data = r.json()
    file_url = data.get("content", {}).get("html_url", "")
    commit_sha = data.get("commit", {}).get("sha", "")
    return file_url, commit_sha


def pick_latest_md(outdir: Path) -> Path:
    """
    outputs 폴더에서 가장 최근 수정된 .md 1개 선택
    """
    md_files = list(outdir.glob("*.md"))
    if not md_files:
        die(f"'{outdir}'에 .md 파일이 없습니다.")
    md_files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return md_files[0]


def main():
    parser = argparse.ArgumentParser(description="생성된 Markdown(.md)을 GitHub repo posts/에 업로드(커밋)합니다.")
    parser.add_argument("--md", help="업로드할 .md 파일 경로 (없으면 outdir에서 최신 .md 선택)")
    parser.add_argument("--outdir", default="outputs", help="--md가 없을 때 최신 .md를 찾을 폴더 (기본: outputs)")
    parser.add_argument("--repo-path", help="레포 안 경로를 직접 지정(예: posts/2026-01-26_xxx.md). 없으면 posts/<파일명> 사용")
    parser.add_argument("--message", help="커밋 메시지(없으면 자동 생성)")
    args = parser.parse_args()

    # 1) 입력 md 파일 결정
    if args.md:
        md_path = Path(args.md)
        if not md_path.exists():
            die(f"파일이 없습니다: {md_path}")
    else:
        md_path = pick_latest_md(Path(args.outdir))

    md_text = read_text(md_path)

    # 2) repo 내 업로드 경로 결정
    if args.repo_path:
        repo_path = args.repo_path.replace("\\", "/")
    else:
        repo_path = f"{GITHUB_POSTS_DIR}/{md_path.name}".replace("\\", "/")

    # 3) 커밋 메시지 결정
    title = guess_title_from_md(md_text) or md_path.stem
    commit_message = args.message or f"post: {title}"

    # 4) 토큰 체크 (실수 방지)
    if not GITHUB_TOKEN or "PASTE_YOUR_TOKEN_HERE" in GITHUB_TOKEN:
        die("GITHUB_TOKEN이 설정되지 않았습니다. 파일 상단 변수 또는 환경변수(GITHUB_TOKEN)를 설정하세요.")

    # 5) 업로드 실행
    file_url, commit_sha = create_or_update_file(
        owner=GITHUB_OWNER,
        repo=GITHUB_REPO,
        branch=GITHUB_BRANCH,
        token=GITHUB_TOKEN,
        repo_path=repo_path,
        content_text=md_text,
        commit_message=commit_message,
    )

    print("✅ GitHub 업로드 성공")
    print(f"- Local MD : {md_path.resolve()}")
    print(f"- Repo Path: {repo_path}")
    if file_url:
        print(f"- File URL : {file_url}")
    if commit_sha:
        print(f"- Commit   : {commit_sha}")


if __name__ == "__main__":
    main()
