# 범용 절차적 추론 데이터베이스 설계
**부제:** Reasoning Core: Designing Broad Procedural Data for Completion-Supervised Reasoning Training

## 한 줄 결론
Reasoning Core는 50개의 절차적 생성기와 평가 체계를 결합해 기존 컬렉션 대비 completion-supervised 방식의 추론 성능을 크게 향상시킨다.

## TL;DR (요약)
- 절차적 생성기는 검증 가능한 추론 문제를 대규모로 제공하지만, completion-supervised 방식의 미세조정 데이터로는 부족함이 있었다.  
- Reasoning Core는 수학, 논리, 계획, 상태 추적, 형식 언어, 구조화된 데이터, 게임, 인과관계, 코드 등 9개 분야 50개 생성기를 포함한다.  
- 의미 점수화(semantic scoring), 난이도 제어, 태스크별 평가기를 도입하여 유틸리티를 극대화했다.  
- 3B 파라미터 모델 기준 DROP, LogiQA, ARC-Challenge에서 최고 평균 성능을 달성했으며, 모든 비교 컬렉션을 능가했다.  
- 데이터 생성 과정 전반에 걸쳐 모델 보조 검토, 인간 판정, 회귀 테스트를 적용해 미묘한 불일치를 발견하고 개선했다.

## 문제 정의(Problem)
절차적 생성(Procedural generation)은 합성 추론 문제를 대량으로 생성해 모델을 학습시키는 장점이 있으나, completion-supervised(완성 감독) 미세조정에 활용된 사례는 제한적이었다. 기존 Procedural Warmup, Reasoning Gym, SynLogic 등 컬렉션의 효용을 일관된 비교 프로토콜 아래 평가하고, 더 광범위하고 품질 높은 데이터셋 설계 방안을 모색할 필요가 있다.

## 제안 방법(Method)
Reasoning Core는 다음 요소들을 결합해 설계되었다.
- 9개 분야, 50개의 절차적 생성기(procedural generators)
- 생성된 문제에 대한 의미 점수화(semantic scorers) 및 난이도 조정 도구
- 태스크별 자동 평가기(task evaluators)
  
이후 네 가지 베이스 모델 설정(파라미터 크기 및 구조)과 여러 훈련 기간(training durations)에 걸쳐 동일한 completion-supervised 프로토콜로 Reasoning Core와 기존 컬렉션을 비교했다. 추가로 모델 보조 검토, 인간 판정(human adjudication), 회귀 테스트(regression testing)를 포함하는 감사(audit) 과정을 통해 생성·렌더링·정답·점수화 단계 간 미묘한 불일치를 검출·수정했다.

## 핵심 기여/차별점(Contributions)
- 50개 생성기를 아우르는 광범위한 절차적 추론 데이터셋 ‘Reasoning Core’ 공개  
- 동일 조건(completion-supervised) 하에서 기존 세 컬렉션 대비 DROP, LogiQA, ARC-Challenge 최고 평균 성능 달성  
- 생성 과정 전반에 모델 보조 검토, 인간 판정, 회귀 테스트를 포함한 체계적 감사 메커니즘 도입  

## 한계/리스크(Limitations)
- 초록 기준으로는 어떤 베이스 모델 구성 및 훈련 기간이 구체적으로 사용되었는지 확인 불가  
- 의미(validity) 점수화만으로는 학습 유용성을 보장하지 못하며, 난이도 보정 및 목표(target) 크기가 중요함을 지적하나 관련 메트릭 세부치는 미공개  
- 감사 과정에서 드러난 미묘한 불일치는 데이터 안정성에 대한 지속적 관리가 필요함

## 실무 적용 아이디어(Practical Takeaways)
- 모델 미세조정 데이터셋 설계 시 다양한 분야의 절차적 생성기를 조합해 폭넓은 문제 유형 포트폴리오 구축  
- 의미 점수화 및 난이도 제어 도구를 포함해 학습 데이터 품질을 정량적으로 관리  
- 배포 전 모델 보조 검토, 인간 판정, 회귀 테스트를 통합한 감사 파이프라인 구축으로 데이터·평가 체계 일관성 확보  

## 메타 정보
- 저자: Damien Sileo, Valentin Lacombe, Dimitri Kachler  
- 발행일: 초록 기준으로는 확인 불가  
- 카테고리: 인공지능(AI), 머신러닝, 절차적 생성, 추론

## 참고 링크
[https://arxiv.org/abs/2608.05148v1](https://arxiv.org/abs/2608.05148v1)
