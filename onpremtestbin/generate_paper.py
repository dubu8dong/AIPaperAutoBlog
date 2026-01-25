import os
import re
import argparse
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode

import feedparser
from dotenv import load_dotenv
from openai import AzureOpenAI
import markdown as mdlib


# ---------- small utils ----------
def slugify(text: str, max_len: int = 80) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text).strip("-")
    return text[:max_len].strip("-") or "paper"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


# ---------- arXiv helpers ----------
def extract_arxiv_id(link: str) -> str:
    """
    e.g. https://arxiv.org/abs/2401.12345v2 -> 2401.12345
         http://arxiv.org/abs/2401.12345 -> 2401.12345
    """
    if not link:
        return ""
    m = re.search(r"arxiv\.org/abs/([0-9]+\.[0-9]+)(v[0-9]+)?", link)
    return m.group(1) if m else ""


def fetch_latest_arxiv_entries(categories: list[str], max_results: int) -> list[dict]:
    """
    Fetch recent entries from arXiv API.
    NOTE: arXiv query must be URL-encoded (spaces etc.)
    """
    cat_query = " OR ".join([f"cat:{c}" for c in categories])

    params = {
        "search_query": cat_query,
        "start": 0,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = "http://export.arxiv.org/api/query?" + urlencode(params)

    feed = feedparser.parse(url)
    entries = []

    for e in getattr(feed, "entries", []):
        authors = [a.name for a in getattr(e, "authors", [])]
        link = getattr(e, "link", "").strip()
        arxiv_id = extract_arxiv_id(link)

        entries.append({
            "arxiv_id": arxiv_id,
            "title": getattr(e, "title", "").strip().replace("\n", " "),
            "summary": getattr(e, "summary", "").strip().replace("\n", " "),
            "published": getattr(e, "published", "").strip(),
            "updated": getattr(e, "updated", "").strip(),
            "authors": authors,
            "link": link,
            "categories": [t.term for t in getattr(e, "tags", [])] if hasattr(e, "tags") else categories,
        })

    return entries


def build_paper_input(entry: dict) -> str:
    return (
        f"arXiv ID: {entry.get('arxiv_id','')}\n"
        f"Title: {entry.get('title','')}\n"
        f"Authors: {', '.join(entry.get('authors', [])) if entry.get('authors') else 'N/A'}\n"
        f"Published: {entry.get('published','')}\n"
        f"Updated: {entry.get('updated','')}\n"
        f"Categories: {', '.join(entry.get('categories', []))}\n"
        f"Link: {entry.get('link','')}\n\n"
        f"Abstract:\n{entry.get('summary','')}\n"
    )


# ---------- dedupe (state) ----------
def load_processed_ids(state_file: Path) -> set[str]:
    if not state_file.exists():
        return set()
    lines = [ln.strip() for ln in state_file.read_text(encoding="utf-8").splitlines()]
    return {ln for ln in lines if ln}


def append_processed_id(state_file: Path, arxiv_id: str) -> None:
    if not arxiv_id:
        return
    state_file.parent.mkdir(parents=True, exist_ok=True)
    with state_file.open("a", encoding="utf-8") as f:
        f.write(arxiv_id + "\n")


def pick_first_unprocessed(entries: list[dict], processed_ids: set[str]) -> dict | None:
    for e in entries:
        arxiv_id = e.get("arxiv_id", "")
        # arxiv_id가 비어있다면 link 기반으로라도 중복 체크를 하고 싶지만,
        # abs 링크는 거의 항상 있으므로 우선은 id 기준으로만.
        if arxiv_id and arxiv_id not in processed_ids:
            return e
    return None


# ---------- LLM + postprocess ----------
def normalize_markdown(md: str) -> str:
    """
    출력 편차 최소화(가벼운 안전장치)
    - '## TL;DR' -> '## TL;DR (요약)'
    - '## 메타 정보 (...)' -> '## 메타 정보'
    """
    text = md.strip()

    text = re.sub(r"^##\s*TL;DR\s*$", "## TL;DR (요약)", text, flags=re.MULTILINE)
    text = re.sub(r"^##\s*TL;DR\s*\(요약\)\s*$", "## TL;DR (요약)", text, flags=re.MULTILINE)
    text = re.sub(r"^##\s*메타\s*정보.*$", "## 메타 정보", text, flags=re.MULTILINE)

    return text + "\n"


def call_aoai_markdown(prompt_template: str, paper_input: str) -> str:
    load_dotenv()

    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    missing = [k for k, v in {
        "AZURE_OPENAI_API_KEY": api_key,
        "AZURE_OPENAI_ENDPOINT": endpoint,
        "AZURE_OPENAI_DEPLOYMENT": deployment,
        "AZURE_OPENAI_API_VERSION": api_version,
    }.items() if not v]
    if missing:
        raise RuntimeError(f".env에 값이 없습니다: {', '.join(missing)}")

    client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
    )

    user_prompt = prompt_template.replace("{{PAPER_INPUT}}", paper_input)

    # o4-mini는 temperature 등 일부 샘플링 파라미터 제약이 있을 수 있으므로 기본값 사용
    resp = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return resp.choices[0].message.content


def markdown_to_tistory_html(md_text: str) -> str:
    """
    티스토리 HTML 모드 붙여넣기용 변환.
    nl2br: 단일 줄바꿈도 <br> 처리해 가독성 개선.
    """
    return mdlib.markdown(
        md_text,
        extensions=["fenced_code", "tables", "toc", "codehilite", "nl2br"],
        extension_configs={"codehilite": {"guess_lang": False}},
    )


# ---------- main ----------
def main():
    parser = argparse.ArgumentParser(description="arXiv 논문 1편을 기술 리포트형 Markdown/HTML로 생성 (중복 방지 포함)")
    parser.add_argument("--categories", default="cs.AI,cs.CL", help="arXiv 카테고리(콤마), 예: cs.CL,cs.LG")
    parser.add_argument("--outdir", default="outputs", help="출력 디렉터리")
    parser.add_argument("--prompt", default="prompts/blog_report_v1.txt", help="프롬프트 템플릿 경로")
    parser.add_argument("--state", default="state/processed_arxiv_ids.txt", help="처리 이력 파일(중복 방지)")
    parser.add_argument("--lookback", type=int, default=10, help="최신 몇 편까지 훑어서 신규 1편을 고를지")
    args = parser.parse_args()

    categories = [c.strip() for c in args.categories.split(",") if c.strip()]
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    prompt_path = Path(args.prompt)
    if not prompt_path.exists():
        raise FileNotFoundError(f"프롬프트 파일이 없습니다: {prompt_path}")
    prompt_template = read_text(prompt_path)

    state_file = Path(args.state)
    processed_ids = load_processed_ids(state_file)

    # 1) 최근 N개 조회
    entries = fetch_latest_arxiv_entries(categories, max_results=args.lookback)
    if not entries:
        print("arXiv에서 결과를 찾지 못했습니다. 카테고리/네트워크를 확인하세요.")
        return

    # 2) 아직 처리 안 된 1편 선택
    entry = pick_first_unprocessed(entries, processed_ids)
    if entry is None:
        print("생성할 신규 논문이 없습니다 (최근 항목이 모두 처리됨). 정상 종료합니다.")
        return

    # 3) 글 생성
    paper_input = build_paper_input(entry)
    md = call_aoai_markdown(prompt_template, paper_input)
    md = normalize_markdown(md)

    # 4) 저장
    today = datetime.now().strftime("%Y-%m-%d")
    filename_base = f"{today}_{slugify(entry['title'])}"
    md_path = outdir / f"{filename_base}.md"
    html_path = outdir / f"{filename_base}.html"

    write_text(md_path, md)
    html = markdown_to_tistory_html(md)
    write_text(html_path, html)

    # 5) 처리 이력 기록(성공 후에만)
    append_processed_id(state_file, entry.get("arxiv_id", ""))

    print("=== Selected Paper ===")
    print(f"arXiv ID: {entry.get('arxiv_id','')}")
    print(f"Title   : {entry.get('title','')}")
    print(f"Link    : {entry.get('link','')}")
    print("=== Generated (MD) ===")
    print(md_path.resolve())
    print("=== Generated (HTML) ===")
    print(html_path.resolve())
    print("=== State Updated ===")
    print(state_file.resolve())


if __name__ == "__main__":
    main()
