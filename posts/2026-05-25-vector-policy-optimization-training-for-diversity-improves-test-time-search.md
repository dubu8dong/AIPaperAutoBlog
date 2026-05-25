# 다양성 최적화로 검색 성능 강화

**부제:** Vector Policy Optimization: Training for Diversity Improves Test-Time Search

## 한 줄 결론
VPO는 다차원 벡터 보상을 활용해 LLM의 응답 다양성을 높여, 테스트 시 검색 절차에서 기존 스칼라 강화학습 대비 향상된 성능을 달성한다.

## TL;DR (요약)
- 대규모 언어 모델(Large Language Model, LLM)은 사후 학습(Post-Training) 시 단일 스칼라 보상만 최적화해 낮은 엔트로피 응답 분포를 생성하며, 검색 기반 추론에서 다양한 해답 집합이 요구된다.  
- Vector Policy Optimization(VPO)는 다차원(벡터) 보상을 명시적으로 학습에 반영해 서로 다른 보상 축 간 트레이드오프를 전문화한 다수의 솔루션 세트를 출력하도록 설계된 강화 학습(Reinforcement Learning, RL) 알고리즘이다.  
- VPO는 Generalized Ridge Policy Optimization(GRPO)의 어드밴티지 추정기를 드롭인(drop-in) 대체하며, 네 가지 과제에서 pass@k와 best@k 기준 모두 스칼라 RL 기반 기법을 능가하거나 동등한 성능을 보였다.  
- 특히 검색 예산(Search Budget)이 커질수록 성능 격차가 확대되며, 진화적 검색(Evolutionary Search)에서는 GRPO로 해결할 수 없던 문제를 VPO가 해결함을 확인했다.

## 문제 정의(Problem)
AlphaEvolve와 같은 검색 기반 추론 절차는 복수의 과제별 보상 함수를 고려해 최적의 롤아웃(Rollout)을 선택해야 하지만, 표준 LLM 사후 학습은 미리 정의된 하나의 스칼라 보상만 최적화해 낮은 엔트로피 응답을 생성한다. 이로 인해 검색 단계에서 요구되는 해답 집합(Diverse Solutions Set)의 다양성이 부족해져, 전체적인 검색 성능이 제한된다.

## 제안 방법(Method)
- VPO는 보상이 다차원 벡터(Vector-Valued Reward)로 주어지는 환경을 가정해, 복수의 보상 축(예: 테스트 케이스별 정답률, 사용자 페르소나) 간 트레이드오프를 명시적으로 학습한다.  
- 기존 Generalized Ridge Policy Optimization(GRPO)의 어드밴티지 추정기를 대체해, 정책이 다수의 솔루션을 서로 다른 보상 공간 지점에 전문화(Specialize)하도록 최적화한다.  
- 테스트 시 pass@k 및 best@k 지표를 최대화하도록 학습 과정을 구성해, 검색 예산이 증가할수록 스칼라 RL 대비 성능 이점을 확대한다.

## 핵심 기여/차별점(Contributions)
- 다차원 벡터 보상을 직접 활용해 다양한 downstream 보상 함수에 미리 대응하도록 LLM 정책을 학습하는 접근을 제안.  
- GRPO 어드밴티지 추정기와 호환되는 드롭인 교체 방법을 통해 기존 강화 학습 파이프라인에 손쉽게 통합 가능.  
- 네 가지 벤치마크 과제에서 검색 예산에 따라 pass@k 및 best@k 기준으로 스칼라 RL baseline을 일관되게 상회하거나 동등한 성능을 달성.

## 한계/리스크(Limitations)
- 평가가 네 가지 과제에 국한돼 범용성은 초록 기준으로 확인 불가.  
- 계산 비용 및 학습 안정성에 관한 상세 정보가 없어, 대규모 모델 적용 시 리소스 부담 예측이 어렵다.  
- 벡터 보상 설계(Vector Reward Design) 및 하이퍼파라미터 최적화 절차에 대한 구체적 언급이 없어 구현 난이도를 가늠하기 어렵다.

## 실무 적용 아이디어(Practical Takeaways)
- 코드 생성 서비스에 VPO를 적용해 테스트 케이스별 정확도 향상과 응답 다양성 확보.  
- 대화형 에이전트에서 사용자 페르소나별 다차원 보상 설계를 통해 시나리오별 맞춤형 응답 동시 제공.  
- 클라우드 기반 검색 워크플로우에 VPO 학습 모델을 통합해, 검색 예산별 최적 해답 집합 탐색 자동화.

## 메타 정보
- 저자: Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani, Sebastian Risi, Omar Khattab, Zhang-Wei Hong, Pulkit Agrawal  
- 발표일: 2026년 5월 (arXiv 2605.22817v1)  
- 카테고리: 언어 모델, 강화 학습, 검색 최적화

## 참고 링크
[https://arxiv.org/abs/2605.22817v1](https://arxiv.org/abs/2605.22817v1)
