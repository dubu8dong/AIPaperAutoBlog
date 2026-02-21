# 디퓨전 언어모델 싱크 인식 프루닝  
**부제:** Sink-Aware Pruning for Diffusion Language Models

## 한 줄 결론
불안정한 attention sink를 인식·가지치기하여 DLM의 반복적 추론 과정을 최적화하고 성능 저하를 최소화한다.

## TL;DR (요약)
- 확산 언어모델(Diffusion Language Models, DLM)은 수백 개 스텝의 노이즈 제거 과정을 거쳐 텍스트를 생성, 추론 비용과 지연이 높다.  
- AR(Autoregressive, 자기회귀) 모델과 달리 DLM의 attention sink 위치는 시점별로 크게 변동하여 기존 sink 보존 휴리스틱이 부적합함을 확인.  
- 제안하는 Sink-Aware Pruning은 sink 위치 분산을 측정해 불안정한 sink를 자동 선택·제거, 재학습 없이 효율성과 품질 간 trade-off를 개선.  
- 동일한 계산 예산 하에서 기존 가지치기 기법 대비 더 나은 성능을 보임.

## 문제 정의(Problem)
Diffusion Language Models(DLM)은 입력 문장에 점진적으로 노이즈를 추가하고 이를 반복적으로 제거(iterative denoising)하는 과정을 통해 문장을 생성한다. 보통 수십에서 수백 스텝의 연속적인 선형 변환 및 attention 계산이 필요해 실시간 응답성이 중요한 서비스에서는 높은 연산 비용과 지연(latency)이 문제로 작용한다. Autoregressive(AR) 언어모델에서 개발된 가지치기(pruning) 기법은 주로 attention sink 토큰을 보존하도록 설계되어 왔다. AR 모델에서는 sink가 전역 앵커 역할을 해 안정적이지만, DLM의 경우 sink 위치가 시점마다 이동하며 구조적으로 덜 필수적일 수 있어 동일한 가정 적용에 한계가 있다.

## 제안 방법(Method)
본 연구에서는 DLM 전 단계에서 dominant sink 위치가 어떻게 이동하는지 분석하고, 위치 변화의 분산(variance)이 AR보다 유의미하게 크다는 사실을 확인했다. 이를 기반으로 Sink-Aware Pruning을 제안한다.
1. 각 레이어 및 타임스텝별 attention map을 분석해 dominant sink 위치 추출  
2. 전체 스텝에 걸친 sink 위치의 분산 값을 계산해 불안정 sink 후보 식별  
3. 식별된 sink 토큰 및 연관 파라미터를 prune하되, 추가 재학습 없이 곧바로 적용  
4. 계산 예산에 따라 prune 비율을 조정해 효율성과 품질을 동시에 최적화  
이 방법으로 DLM 추론 시 연산량을 줄이며, 기존 강력한 가지치기 기법에 비해 우수한 품질-효율성 균형을 달성한다.

## 핵심 기여/차별점(Contributions)
- DLM-specific sink 분석: 확산 모델에서 attention sink의 시점별 변동성을 정량적으로 평가  
- Sink-Aware Pruning 프레임워크: 분산 기반으로 불안정 sink를 자동 식별·제거하는 새로운 기법  
- 재학습 없는 성능 향상: 추가 훈련 없이 동일 계산 예산 하에서 기존 기법 대비 성능 우위 검증  

## 한계/리스크(Limitations)
초록 기준으로는 제안 기법의 대규모 모델 확장성, 다양한 언어·도메인 일반화 및 장기적 안정성 등은 확인 불가하다.

## 실무 적용 아이디어(Practical Takeaways)
- 클라우드 기반 DLM 서비스에서 sink 변동성 지표를 도입해 효율적 가지치기 파이프라인 구성  
- 에지 디바이스나 보안 환경에서 재학습 없이 즉시 적용 가능한 경량화 전략으로 활용  
- Pruning 설정 시 sink 분산 임계치와 compute budget 간 밸런스를 조정해 서비스 품질을 관리  

## 메타 정보
- 저자: Aidar Myrzakhan, Tianyi Li, Bowei Guo, Shengkun Tang, Zhiqiang Shen  
- 발행일: 2026-02 (arXiv v1)  
- 카테고리: cs.CL (Computation and Language)  

## 참고 링크
[https://arxiv.org/abs/2602.17664v1](https://arxiv.org/abs/2602.17664v1)
