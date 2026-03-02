# 소량 라벨로 비전·언어 모델 정합

**부제:** SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via Optimal Transport

## 한 줄 결론
SOTAlign은 소량의 대응 이미지-텍스트 쌍과 대량의 비대응 데이터를 활용해 최적 수송 기반 정합으로 비전·언어 임베딩을 효과적으로 정렬한다.

## TL;DR (요약)
- 소량의 이미지-텍스트 대응 쌍과 대규모 비대응 데이터를 활용하는 반지도학습 설정을 제안한다.  
- 1단계에서 선형 교사(Linear Teacher)로 제한된 대응 데이터에서 공동 기하구조를 회복하고, 2단계에서 최적 수송(Optimal Transport) 기반 발산(Divergence)으로 비대응 샘플 간 관계 구조를 전송한다.  
- 기존 대조학습(Contrastive Learning) 및 반지도학습 기법 대비 적은 감독 데이터로도 우수한 정합 성능을 보인다.  
- 다양한 데이터셋과 프리트레인된 비전·언어 인코더 쌍에서 강인한 공동 임베딩을 학습함을 실험적으로 검증했다.

## 문제 정의(Problem)
최근 비전(Vision)과 언어(Language) 프리트레인 모델은 서로 다른 모달리티를 공유된 통계 모델로 수렴한다는 가설(Platonic Representation Hypothesis)을 기반으로, 고정된 인코더(frozen encoder)에 경량 정합 레이어(alignment layers)를 추가해 두 모달리티를 정렬한다.  
그러나 기존 연구는 수백만 개의 이미지-텍스트 대응 샘플과 대조학습 손실을 필요로 하며, 데이터 수집 및 레이블링 부담이 크다.  
본 연구에서는 훨씬 적은 감독 샘플로도 의미 있는 정합을 달성할 수 있는지, 대규모 비대응(unpaired) 데이터를 효과적으로 활용할 수 있는지에 집중한다.

## 제안 방법(Method)
SOTAlign은 두 단계로 구성된 반지도학습 프레임워크다.  
1. Coarse Alignment: 소량의 이미지-텍스트 대응 쌍을 활용해 선형 교사(Linear Teacher)를 학습하고, 이로부터 비전·언어 임베딩의 조밀한(shared) 기하구조를 추정한다.  
2. Refined Alignment: 대규모 비대응 이미지와 텍스트 샘플에서 최적 수송(Optimal Transport) 기반 발산(Divergence)을 사용해 정합을 정제한다.  
   - 발산 함수는 관계 구조(relational structure)를 전송하되, 대상(target) 임베딩 공간을 과도하게 제약하지 않도록 설계되었다.  
   - 이를 통해 비대응 샘플에서도 공동 임베딩을 일관되게 유지하며 정렬 품질을 높인다.

## 핵심 기여/차별점(Contributions)
- 반지도학습 설정 도입: 소량의 대응 이미지-텍스트 쌍과 대규모 비대응 데이터를 동시에 활용하는 새로운 학습 패러다임을 제시.  
- SOTAlign 프레임워크: 1단계 선형 교사 기반 기하구조 회복, 2단계 최적 수송 발산을 결합해 효율적인 공동 임베딩 정합을 달성.  
- 실험적 검증: 다양한 데이터셋 및 비전/언어 인코더 조합에서 기존 감독(supervised)·반지도학습(semi-supervised) 기준을 크게 상회함을 확인.

## 한계/리스크(Limitations)
초록 기준으로는 구체적인 계산 비용, 대규모 비대응 데이터 품질 의존성, 실제 대형 모델 상 적용 가능성 등 상세 한계점이 제시되지 않았다.

## 실무 적용 아이디어(Practical Takeaways)
- 라벨링된 대응 데이터가 제한적인 환경에서, 소량의 paired 샘플과 대규모 unpaired 샘플을 결합해 모델 정합을 고려할 수 있다.  
- contrastive learning 대신 optimal transport 기반 발산을 도입해 모달리티 간 관계 구조를 효과적으로 전송하는 방법을 실험해볼 수 있다.  
- 기존 프리트레인된 frozen encoder 위에 선형 교사 및 경량 정합 레이어만 추가해 빠른 프로토타이핑 및 비용 절감이 가능하다.

## 메타 정보
- 저자: Simon Roschmann, Paul Krzakala, Sonia Mazelet, Quentin Bouniot, Zeynep Akata  
- 발행일: 2026년 2월 (arXiv v1 기준)  
- 카테고리: Vision and Language Alignment, Semi-Supervised Learning, Optimal Transport  

## 참고 링크
[https://arxiv.org/abs/2602.23353v1](https://arxiv.org/abs/2602.23353v1)
