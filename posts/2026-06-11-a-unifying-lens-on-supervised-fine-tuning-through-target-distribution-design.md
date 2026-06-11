# 타겟 분포로 보는 SFT 통합

**부제:** A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design

## 한 줄 결론
SFT를 대상 분포 설계 관점으로 재해석해 Target-SFT를 제안, 다양한 추론 과제에서 성능을 일관되게 향상시킨다.

## TL;DR (요약)
- 기존 감독 학습적 파인튜닝(Supervised Fine-Tuning, SFT)은 관찰된 토큰을 일대일(one-hot)로 최대화해 사전학습된 언어 모델의 풍부한 사전 지식을 제대로 활용하지 못한다.  
- 본 논문은 SFT를 토큰 수준의 목표 분포(Target Distribution) 설계 관점에서 재해석하고, Q-target 프레임워크를 통해 관찰 토큰 의존도와 나머지 확률 질량 할당 방식을 분리하여 정의한다.  
- 이 관점으로 다양한 기존 SFT 변형 기법을 통합적으로 설명하며, Target-SFT라는 새로운 학습 목표 함수를 제안한다.  
- 열 가지 추론 과제 및 모델 조합에서 실험한 결과, Target-SFT가 전통적 SFT 대비 일관된 성능 향상을 보인다.

## 문제 정의(Problem)
전통적인 감독 학습적 파인튜닝(SFT)은 모델이 출력할 토큰에 대해 관찰된 정답 토큰에 확률을 집중시키는(one-hot) 방식으로 학습한다. 그러나 실제 데이터에서 관찰된 토큰은 중복되거나 노이즈가 포함될 수 있고, 사전학습된 모델이 이미 학습한 풍부한 지식을 배제할 위험이 있다. 이러한 접근은 불완전하거나 다의적 표현을 무시함으로써 최적의 일반화 성능을 내기 어려울 수 있다.

## 제안 방법(Method)
본 연구는 SFT를 토큰 수준의 목표 분포(Target Distribution) 설계 문제로 재정의한다. Q-target 프레임워크는 SFT 감독을 두 가지 명시적 선택으로 분해한다. 첫째, 관찰된 토큰에 얼마나 강하게 의존할지 결정하고, 둘째, 남은 확률 질량을 대안 토큰에 어떻게 분배할지 규정한다. 이로써 기존의 여러 SFT 변형 기법들이 암묵적으로 선택한 목표 분포 Q로 해석될 수 있다. 이를 바탕으로, 연구진은 원하는 대상 분포로부터 직접 학습 목표 함수를 구성하는 Target-SFT 기법을 제안했으며, 다양한 모델과 추론 데이터셋에서 일관된 성능 개선을 확인했다.

## 핵심 기여/차별점(Contributions)
- Q-target 프레임워크: SFT 감독을 관찰 토큰 의존도와 대안 토큰 분배로 분해하는 통합적 틀을 제시  
- SFT 변형 기법 통합: 기존의 여러 일관성 제약, 라벨 스무딩(label smoothing) 등 기법을 하나의 분포 설계 관점에서 통합적 분석  
- Target-SFT 제안: 명시적 목표 분포로부터 학습 목표 함수를 직접 구성, 열 가지 추론 과제에서 전통적 SFT 대비 우수한 성능 확보  

## 한계/리스크(Limitations)
- 실험은 열 가지 추론(reasoning) 데이터셋과 모델 조합에 한정되어 있어 다른 도메인(예: 번역, 요약)에서의 일반화 성능은 초록 기준으로는 확인 불가하다.  
- Target-SFT 적용 시 추가 하이퍼파라미터(관찰 토큰 의존도 비율, 분포 할당 방식 등) 설정이 필요하며, 이에 따른 튜닝 비용과 민감도는 초록에서 상세히 다루지 않는다.  

## 실무 적용 아이디어(Practical Takeaways)
- 파인튜닝 시 단일 one-hot 감독 대신 토큰별 확률 분포를 설계해 모델 사전 지식을 더욱 효과적으로 활용  
- Q-target 프레임워크를 참고해 관찰 토큰 가중치와 대안 토큰 분포 전략(균등, 사전확률 기반 등)을 실험  
- Label smoothing, 지식 증류(kd) 기법과 결합해 커스텀 대상 분포를 구성함으로써 성능·안정성 이점을 탐색  

## 메타 정보
- 저자: Tong Xie, Yuanhao Ban, Yunqi Hong, Sohyun An, Yihang Chen, Cho-Jui Hsieh  
- 발행일: 2026년 6월 (arXiv 사전 인쇄)  
- 카테고리: Machine Learning, Natural Language Processing, Supervised Learning  

## 참고 링크
[https://arxiv.org/abs/2606.11189v1](https://arxiv.org/abs/2606.11189v1)
