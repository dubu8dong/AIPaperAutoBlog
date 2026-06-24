# 랜덤화 YaRN으로 긴문맥 추론 강화

**부제:** Randomized YaRN Improves Length Generalization for Long-Context Reasoning

## 한 줄 결론
Randomized YaRN은 단기 문맥 훈련만으로도 16K~128K 길이에서의 추론 성능을 유의미하게 향상시킨다.

## TL;DR (요약)
- 기존 대규모 언어 모델(large language models, LLMs)은 짧은 시퀀스로 사전훈련 후 긴 문맥 일반화에 한계를 보인다.  
- Randomized YaRN은 YaRN 기반 위치 인코딩에 무작위화를 도입하고 길이 커리큘럼을 결합해 단기 입력에서도 이상치(out-of-distribution, OOD) 위치 인코딩을 학습시킨다.  
- BABILong 및 멀티 라운드 공교환(Multi-Round Coreference Resolution, MRCR) 벤치마크에서 8K 미만 훈련으로 16K~128K 범위의 추론 성능을 일관되게 개선한다.  
- 특히 훈련 데이터보다 훨씬 긴 문맥에서 표준 파인튜닝 대비 큰 성능 향상을 보인다.  
- OOD 위치 분포에 점진적으로 노출하는 방식이 긴 문맥 일반화의 효과적인 레시피임을 시사한다.

## 문제 정의(Problem)
대규모 언어 모델은 주로 짧은 시퀀스로 사전훈련되어 있으며, 추가 학습을 통해 더 긴 문맥을 처리하도록 확장된다. 그러나 매우 긴 시퀀스에 대한 일반화 능력은 여전히 제한적이며, 특히 16K를 넘어서는 길이 영역에서 추론 성능이 급격히 저하된다.

## 제안 방법(Method)
Randomized YaRN은 세 가지 요소를 결합한 훈련 기법이다.  
- YaRN 기반 위치 보간(유추) 메커니즘을 활용해 모델이 위치 정보를 확장 학습하도록 한다.  
- 훈련 시 단기 문맥(<8K)에도 샘플된 더 큰 위치 범위에서 랜덤화된 YaRN 위치 인코딩을 할당해 이상치(out-of-distribution, OOD) 위치 표현을 경험하도록 한다.  
- 단계별 길이 커리큘럼을 설계해 점진적으로 긴 위치 분포에 노출시킴으로써 문맥 길이 일반화를 촉진한다.

## 핵심 기여/차별점(Contributions)
- Randomized YaRN: YaRN 위치 인코딩 무작위화와 길이 커리큘럼 결합으로 단기 문맥에서도 OOD 위치 학습을 유도.  
- 16K~128K 길이 범위에서 단일 <8K 훈련만으로도 추론 성능을 일관되게 개선.  
- BABILong 및 MRCR(long-context coreference) 벤치마크에서 표준 파인튜닝 대비 높은 성능 향상 확인.

## 한계/리스크(Limitations)
- 평가가 BABILong과 MRCR 두 가지 벤치마크에 한정되어 있어, 다른 긴 문맥 추론 과제에 대한 일반화는 초록 기준으로 확인 불가.  
- 모델 크기, 계산 비용, 응답 지연(latency) 등 실제 배포 시 고려해야 할 지표는 초록에서 확인 불가.  
- 구체적인 길이 커리큘럼 스케줄 및 하이퍼파라미터 설정 세부 사항은 초록만으로는 파악 불가.

## 실무 적용 아이디어(Practical Takeaways)
- 긴 문맥 파인튜닝 시 YaRN 기반 위치 보간에 무작위화 기법을 도입하여 OOD 위치 분포를 학습하도록 구성해 보자.  
- 길이 커리큘럼을 설계해 짧은 문맥 단계부터 점진적으로 긴 문맥 분포에 모델을 노출시키는 전략을 고려하자.  
- 기존 파인튜닝 워크플로우에 큰 변경 없이도 단기 데이터만으로 긴 문맥 성능을 개선할 수 있는 가능성을 검토해보자.

## 메타 정보
- 저자: Manas Mehta, Fangcong Yin, Greg Durrett  
- 발행일: 2026년 6월 (arXiv v1)  
- 카테고리: Machine Learning (cs.LG), Natural Language Processing (cs.CL)

## 참고 링크
[https://arxiv.org/abs/2606.23687v1](https://arxiv.org/abs/2606.23687v1)
