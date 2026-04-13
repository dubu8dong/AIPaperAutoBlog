# 시각 인식만 강한 MoE의 한계
**부제:** Seeing but Not Thinking: Routing Distraction in Multimodal Mixture-of-Experts

## 한 줄 결론
멀티모달 Mixture-of-Experts(MoE) 모델은 시각 입력 처리 시 핵심 추론 전문가 활성화가 방해를 받아 성능이 저하되며, 라우팅 개입으로 이를 일부 개선할 수 있다.

## TL;DR (요약)
- 멀티모달 MoE 모델에서 이미지를 입력할 때는 시각 전문가가 선택되나 추론 전문가가 덜 활성화되어 일종의 “보긴 하지만 사고하지 않는” 현상이 발생한다.
- 저자들은 레이어별 라우팅 분리를 관찰하고, 시각 입력이 중간 레이어에서 도메인(추론) 전문가의 라우팅을 방해한다는 ‘Routing Distraction’ 가설을 제시했다.
- 제안된 라우팅 개입 기법은 도메인 전문가의 활성화를 보강하여 복합 시각 추론 벤치마크에서 최대 3.17% 성능 향상을 확인했다.
- 전문가 식별 결과 인지 기능 단위로 모듈이 분리되어, 서로 다른 태스크 구조 간 전이 가능함을 보였다.

## 문제 정의(Problem)
멀티모달 Mixture-of-Experts(MoE) 모델은 시각(Language-Vision) 및 언어 텍스트 입력을 모두 처리할 때 뛰어난 성능을 보인다. 그럼에도 불구하고 동일한 추론 문제를 텍스트 형태로 제시하면 정확히 풀지만, 이미지를 함께 넣으면 오답률이 높아지는 현상이 관찰된다. 이를 저자들은 “Seeing but Not Thinking(보기만 하고 사고하지 않음)” 현상이라 부르며, 이미지 처리 과정에서 추론 전문가(domain expert)가 충분히 활성화되지 않아 발생한다고 가설을 세웠다.

## 제안 방법(Method)
1. Cross-modal Semantic Sharing 검증  
   - MoE 아키텍처 내에서 시각·언어 간 의미 공유가 존재함을 확인해, 단순한 의미 정렬(failure of semantic alignment) 문제로는 설명 불가함을 보였다.
2. Layer-wise Routing 분석  
   - 시각 입력 시 중간 레이어에서 전문가 간 라우팅 분기가 크게 달라져, 도메인 전문가 활성화가 감소함을 계층별로 분석했다.
3. Routing Distraction 가설  
   - 시각 모달리티가 라우팅 메커니즘을 분산(distraction)시켜, 태스크 핵심 추론 전문가가 충분히 선택되지 못한다고 정의.
4. Routing-guided Intervention  
   - 도메인 전문가 활성화를 강화하는 라우팅 개입 방식을 설계·적용, 세 가지 멀티모달 MoE 모델과 여섯 개 벤치마크에서 성능 개선을 검증했다.

## 핵심 기여/차별점(Contributions)
- "Seeing but Not Thinking" 현상 규명: 시각 입력이 추론 전문가 선택을 방해한다는 새로운 현상을 정의하고 분석  
- Routing Distraction 가설 제시: 레이어별 라우팅 분산 메커니즘이 모델 추론 성능 저하를 일으킨다는 이론적 근거 제공  
- Routing-guided Intervention: 도메인(추론) 전문가 활성화를 높이는 기법으로, 복합 시각 추론 벤치마크에서 최대 3.17% 성능 향상 달성

## 한계/리스크(Limitations)
- 초록 기준으로는 제안된 개입 기법의 계산 비용이나 지연(latency) 증감 등 실시간 서비스 적용 영향을 확인할 수 없다.  
- 세 가지 모델과 여섯 개 벤치마크에 대한 실험 결과만 제공되며, 기타 멀티모달 아키텍처나 대규모 데이터셋 일반화 여부는 확인 불가하다.  
- 개입 방식이 학습 안정성(training stability)이나 과적합(overfitting)에 미치는 영향은 초록만으로는 파악할 수 없다.

## 실무 적용 아이디어(Practical Takeaways)
- 모달리티별 라우팅 통계 모니터링: 시각·언어 입력 시 주요 전문가 활성화 비율을 점검해 추론 전문가 저활성화를 조기에 탐지  
- 라우팅 개입 적용: 기존 멀티모달 MoE 모델에 도메인 전문가 보강용 게이트 또는 스코어 재조정 모듈을 추가하여 성능을 개선  
- 전문가 전이 활용: 전문가 식별 결과를 바탕으로 인지 기능 단위 모듈을 별도 저장해, 유사 구조의 다른 태스크에 전이 학습

## 메타 정보
- 저자: Haolei Xu, Haiwen Hong, Hongxing Li, Rui Zhou, Yang Zhang, Longtao Huang, Hui Xue, Yongliang Shen, Weiming Lu, Yueting Zhuang  
- 발행일: 2026-04 (arXiv preprint)  
- 카테고리: 멀티모달 모델, Mixture-of-Experts, 라우팅 분석

## 참고 링크
[https://arxiv.org/abs/2604.08541v1](https://arxiv.org/abs/2604.08541v1)
