# 회복형 비주얼 토큰 라우팅

**부제:** Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models

## 한 줄 결론
Reroute는 기존 비주얼 토큰 제거 방식을 복원이 가능한 라우팅으로 대체해, 과감한 토큰 축소에서도 grounding 성능을 높이면서 VQA 등 일반 질의응답 성능을 유지한다.

## TL;DR (요약)
- 비전-언어 모델(Vision-Language Model, VLM)은 수백~수천 개의 시각 토큰을 생성해 디코더의 연산과 KV-캐시 메모리를 크게 소모한다.  
- 기존 방법은 토큰 중요도에 따라 저순위 토큰을 영구 폐기(removal)하지만, 층별 중요도 변화에 취약하다.  
- Reroute는 훈련 불필요 플러그인으로, 선택되지 않은 토큰을 다음 스테이지로 되돌려 복원(recoverable routing)한다.  
- 기존 TFLOPs 및 KV-캐시 예산을 유지하면서 FastV, PDrop, Nüwa 기법에 적용해 grounding 민감 쿼리 성능을 개선했다.

## 문제 정의(Problem)
비전-언어 모델은 이미지를 수백~수천 개의 시각 토큰으로 분할해 디코더에 입력한다. 이 과정은 멀티-헤드 어텐션 연산량과 KV-캐시 메모리 사용량을 크게 증가시켜 비용이 높다.  
기존 비주얼 토큰 축소(pruning) 기법은 토큰에 점수를 매겨 상위 일부만 남기고 나머지를 영구 제거한다(rank-and-remove). 하지만 디코더 블록을 거치며 토큰의 중요도는 변하기 때문에, 한때 저평가됐던 토큰이 나중 단계에서는 핵심 정보로 부각되는 경우가 발생한다. 특히, grounding-sensitive 쿼리(예: 객체 위치 묻기)에서는 이 문제로 성능이 급격히 저하될 수 있다.

## 제안 방법(Method)
Reroute는 훈련 없이 후처리로 삽입할 수 있는 플러그인이다. 각 라우팅 단계에서:
- 어텐션 점수 기반으로 상위 K개 토큰을 선택해 디코더 블록에 투입한다.
- 나머지 토큰은 해당 단계 처리를 건너뛰고, 다음 라우팅 결정 시점에 후보 풀로 되돌아간다.
이 과정을 통해 한 단계에서 탈락한 토큰도 이후 단계에서 재평가할 수 있다.  
기존 프루닝(pruning) 방식의 이론적 TFLOPs와 KV-캐시 예산 클래스는 유지하며, FastV, PDrop, Nüwa 계열의 토큰 축소 기법에 그대로 적용 가능하다. LLaVA-1.5 및 Qwen 백본을 대상으로 실험한 결과, 과감한 축소 조건에서도 grounding 성능과 일반 VQA 성능을 함께 개선했다.

## 핵심 기여/차별점(Contributions)
- 복원형 라우팅 개념 제시: 한 번 제거된 토큰도 다음 단계에서 재진입해 중요도를 재평가할 수 있도록 함  
- 훈련 불필요한 플러그인 구조: 기존 어텐션 스코어 산출 및 단계별 스케줄을 그대로 활용, 추가 학습 없이 적용  
- 범용 호환성 입증: FastV, PDrop, Nüwa 등 다양한 토큰 프루닝 기법 및 LLaVA-1.5, Qwen 백본에서 grounding 민감 질의 성능 개선

## 한계/리스크(Limitations)
- 초록 기준으로는 Reroute 적용 시 실제 지연(latency) 오버헤드 정도를 확인할 수 없음  
- 단계별 토큰 재진입 빈도나 토큰 풀 크기에 따른 성능/자원 trade-off 수치는 공개되지 않음  
- 대규모 실서비스 환경에서 KV-캐시 관리 복잡도 증대 여부는 초록 수준에서 파악 불가

## 실무 적용 아이디어(Practical Takeaways)
- 클라우드 기반 VLM 추론 파이프라인에 Reroute 플러그인을 추가해 토큰 축소 시 성능 저하를 완화  
- 어텐션 스코어 순위를 이용한 단계별 라우팅 스케줄링을 통해 KV-캐시 메모리 예산을 그대로 유지  
- 이미지-텍스트 grounding이 중요한 VQA, 멀티모달 검색, 대화형 AI 서비스 등에 토큰 복원 메커니즘 적용  

## 메타 정보
- 저자: Cheng-Yu Yang, Shao-Yuan Lo, Yu-Lun Liu  
- 발행일: 2026-06 (arXiv v1)  
- 카테고리: Computer Vision and Pattern Recognition (cs.CV)

## 참고 링크
[https://arxiv.org/abs/2606.12412v1](https://arxiv.org/abs/2606.12412v1)
