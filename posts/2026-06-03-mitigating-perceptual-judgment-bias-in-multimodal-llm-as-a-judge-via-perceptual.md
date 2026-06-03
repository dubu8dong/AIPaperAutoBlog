# 멀티모달 평가의 지각 편향 완화
**부제:** Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling

## 한 줄 결론
깊은 시각-언어 평가 모델의 지각 판단 편향을 시각적 교란과 보상 모델링으로 완화한다.

## TL;DR (요약)
- 멀티모달 대형 언어 모델(MLLM)을 평가자로 사용할 때 시각-텍스트 불일치 상황에서 텍스트 서술에 편향되어 평가지가 이탈되는 현상을 정의하고 분석했다.  
- 최소한의 시각 교란을 적용해 지각 오류만을 분리한 Perceptually Perturbed Judgment Dataset을 구축했다.  
- 구조화된 GRPO 기반 보상 모델링과 배치-랭킹 손실함수를 결합한 통합 학습으로 전역 서열 일관성을 확보했다.  
- 다양한 벤치마크에서 지각 충실도, 순위 일관성, 인간 평가 정합성이 크게 개선되었다.

## 문제 정의(Problem)
멀티모달 대형 언어 모델(MLLM)을 평가자로 활용할 경우, 이미지 기반 증거와 텍스트 설명이 충돌하는 상황에서 모델이 시각적 정보 대신에 텍스트 서술의 그럴듯함(plausibility)에 지나치게 의존한다. 이를 본 논문에서는 Perceptual Judgment Bias(지각 판단 편향)이라 명명했다. 연구진은 통제된 시각적 교란(Controlled Visual Perturbations) 실험을 통해, 기존 MLLM 평가자는 응답 텍스트에 고정(anchoring)되어 자신의 시각 인식을 무시하고, 일관성 없는 평가 결과를 도출한다는 사실을 밝혀냈다.

## 제안 방법(Method)
- Perceptually Perturbed Judgment Dataset 구축  
  - 실제 정답(ground truth) 기반 응답에 대하여 색상이나 배경 등 시각적 요소를 최소한으로 교란(perturbation)해 대조(counterfactual) 응답을 생성했다.  
  - 각 대조 응답은 원본과 최소 차이만 존재하므로, 지각 오류(perceptual error)만을 분리해 감독(supervision)할 수 있다.  
- 통합 학습 프레임워크  
  - 구조화된 GRPO(초록 기준으로는 약어 풀네임 미확인) 기반 reward modeling(보상 모델링)과 배치-랭킹(batch-ranking) 손실함수를 결합했다.  
  - 명시적 페어와이즈(pairwise) 레이블 없이도 다양한 응답 간 전역(global) 서열(ordering) 일관성을 학습하며, 단일 배치(batch) 내에서 순위를 최적화한다.

## 핵심 기여/차별점(Contributions)
- Perceptual Judgment Bias 현상을 정의·분석하고, 시각-텍스트 충돌 상황에서 평가 신뢰도를 정량화했다.  
- 최소 교란된 반증(counterfactual) 응답을 포함하는 Perceptually Perturbed Judgment Dataset을 제안해 지각 오류 감독에 활용했다.  
- GRPO 기반 보상 모델과 배치-랭킹 학습을 결합한 통합 훈련 방식으로, 다양한 벤치마크에서 지각 충실도, 서열 일관성, 인간 평가 정합성을 동시에 개선했다.

## 한계/리스크(Limitations)
- 초록 기준으로는 실제 비조작(real-world) 이미지나 복잡한 시나리오에서의 효과 검증 여부 확인 불가  
- 반증 응답이 최소 교란된 예시 중심으로 구성되어, 광범위한 도메인 일반화 성능은 미확인  
- GRPO 보상 모델의 구체적 메커니즘 및 학습 비용·스케일링 정보는 초록에서 제공되지 않음

## 실무 적용 아이디어(Practical Takeaways)
- MLLM 평가지 구축 시, 의도된 시각 교란을 적용한 반증 예시를 포함해 모델의 지각 신뢰도를 점검하라.  
- 보상 모델링과 배치-랭킹 손실함수를 조합해 평가자 모델의 전역 서열 일관성을 확보하라.  
- 평가 파이프라인에서 텍스트 서술뿐 아니라 이미지-텍스트 일관성을 주기적으로 검증하는 모니터링 체계를 도입하라.

## 메타 정보
- 저자: Seojeong Park, Jiho Choi, Junyong Kang, Seonho Lee, Jaeyo Shin, Hyunjung Shim  
- 발행일: 초록 기준으로는 확인 불가  
- 카테고리: 초록 기준으로는 확인 불가  

## 참고 링크
[https://arxiv.org/abs/2606.02578v1](https://arxiv.org/abs/2606.02578v1)
