# 상관관계가 형성하는 피처 중첩

**부제:** From Data Statistics to Feature Geometry: How Correlations Shape Superposition

## 한 줄 결론
피처 간 상관관계는 중첩(superposition)에서 간섭(interference)을 건설적으로 배열해 의미적 클러스터와 순환 구조를 형성함을 보여준다.

## TL;DR (요약)
- 전통적 관점에서는 희소(sparse)・무상관(uncorrelated) 피처만을 고려해 중첩에서 발생하는 간섭을 최소화하려 했음.  
- Bag-of-Words Superposition(BOWS)라는 통제된 설정에서 이진 BoW 표현을 중첩하여 학습한 결과, 상관된 피처 간 간섭이 오히려 유용한 신호로 작용함을 발견.  
- 피처를 공활성화(co-activation) 패턴에 따라 배치해 활성 피처 간 시너지를 극대화하고, ReLU(렐루)를 이용해 거짓 양성(false positive)을 제어.  
- 가중치 감쇠(weight decay)를 적용한 모델에서 의미적 클러스터와 순환 구조가 자연스레 나타나는 현상을 확인.

## 문제 정의(Problem)
- 신경망이 보유한 차원보다 더 많은 피처를 중첩(superposition)하여 과잉 완전 기저(over-complete basis)를 형성한다는 메커니즘 해석(mechanistic interpretability) 패러다임이 존재.  
- 기존 연구는 희소・무상관 피처 상황을 이상화하여 중첩 간섭을 비선형 활성화 함수로 걸러내는 방식으로 이해해 왔음.  
- 현실 데이터에서는 피처 간 상관관계가 일반적이며, 이 경우 기존의 간섭 최소화 관점만으로는 모델 내부 기하학을 설명하기 어려움.

## 제안 방법(Method)
- Bag-of-Words Superposition(BOWS) 설정을 도입해 이진(binary) 형태의 인터넷 텍스트 BoW 표현을 중첩 방식으로 인코딩하고 학습.  
- 학습된 네트워크에서 피처별 co-activation 패턴을 분석해, 상관된 피처들이 중첩 시 간섭(interference)을 어떻게 이용하는지 조사.  
- 피처를 co-activation 유사도에 따라 기하학적으로 배열하고, ReLU 비선형성을 활용해 비활성 상태에서의 잘못된 활성화를 억제.

## 핵심 기여/차별점(Contributions)
- BOWS(Bag-of-Words Superposition)라는 새로운 통제된 실험 설정을 제안하여 중첩 거동을 연구할 프레임워크를 제공.  
- 상관된 피처 간 간섭이 단순한 잡음이 아니라 건설적인 신호로 작용함을 규명.  
- 가중치 감쇠(weight decay) 하에서 의미적 클러스터와 순환 구조(cyclical structures)가 자연 발생함을 실험적으로 확인.

## 한계/리스크(Limitations)
- 실험은 이진 BoW 표현에 국한되어 있으며, 연속 임베딩이나 복잡한 언어 모델의 일반화 가능성은 초록 기준으로는 확인 불가.  
- 가중치 감쇠 외의 규제(regularization) 기법이 유사한 구조를 유도하는지 여부는 알 수 없음.  

## 실무 적용 아이디어(Practical Takeaways)
- 임베딩 설계 시 피처 간 상관관계를 고려해 co-activation 패턴 기반의 기하학적 배열 구조를 검토.  
- 가중치 감쇠를 적절히 활용해 의미적 클러스터 및 순환 구조의 학습을 유도, 모델 해석성과 정밀도를 동시에 향상.  
- 학습된 모델 내부에서 활성화 패턴 분석을 수행해 피처 중첩의 건설적 간섭 여부를 지속적으로 점검.

## 메타 정보
- 저자: Lucas Prieto, Edward Stevinson, Melih Barsbey, Tolga Birdal, Pedro A. M. Mediano  
- 발행일: 2026년 3월 (arXiv v1)  
- 카테고리: 기계 학습(Machine Learning)

## 참고 링크
[https://arxiv.org/abs/2603.09972v1](https://arxiv.org/abs/2603.09972v1)
