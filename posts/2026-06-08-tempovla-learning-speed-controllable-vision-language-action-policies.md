# TempoVLA 속도 제어 로봇

**부제:** TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies

## 한 줄 결론
TempoVLA는 궤적 재타이밍과 속도 조건화를 결합해 단일 비전-언어-액션(Vision-Language-Action, VLA) 모델의 실행 속도를 유연하게 제어한다.

## TL;DR (요약)
TempoVLA는 로봇 조작 과정에서 저위험 단계는 빠르게, 고위험 단계는 느리게 동작하도록 속도를 조절할 수 있는 VLA 모델이다.  
데이터 측면의 가변 속도 궤적 증강(Variable-Speed Trajectory Augmentation, VSTA)으로 기존 시연 데이터를 다양한 속도로 재타이밍하며 운동 시맨틱을 보존한다.  
모델 측면의 속도 조건화 메커니즘으로 원하는 속도 정보를 정책에 직접 입력해 실행 시 유연한 속도 변화를 가능하게 한다.  
시뮬레이션 및 실제 로봇 실험에서 양방향 속도 제어를 달성했으며, 기본 1× 속도 성능도 VSTA로 향상되었다.

## 문제 정의(Problem)
- 로봇 조작은 빠른 이동(transit) 단계와 느리고 정밀해야 하는 접촉(contact) 단계가 번갈아 발생한다.  
- 기존 비전-언어-액션 모델(VLA)은 시연 데이터를 통해 학습된 단일 속도를 그대로 유지하며, 단계별 위험도에 따른 속도 조절 기능이 없다.  
- 모델 압축, 키-값 캐시(Key-Value cache) 재활용, 강화학습 등을 통한 속도 개선 시도는 항상 하나의 고정 속도에서 다른 고정 속도로 이동할 뿐, 감속(deceleration)은 거의 연구되지 않았다.

## 제안 방법(Method)
TempoVLA는 데이터 측과 모델 측 두 축으로 속도 제어를 구현한다.
- 데이터 측: Variable-Speed Trajectory Augmentation (VSTA)
  - 시연 궤적을 목표 속도에 맞춰 재타이밍(re-timing)한다.
  - 속도를 높일 때는 동작을 병합(merge), 낮출 때는 분할(split)해 궤적 길이를 조정하되, 원본 운동 시맨틱을 보존한다.
  - 통계적으로 요청된 속도에 근접하며 모션 오류는 미미하다.
- 모델 측: 속도 조건화(conditioning) 메커니즘
  - 정책(policy) 네트워크의 입력으로 명시적인 속도 값을 추가로 공급한다.
  - 학습 시 서로 다른 속도 조건을 함께 맞추며, 실행 시 원하는 속도로 동작하도록 제어한다.

## 핵심 기여/차별점(Contributions)
- 데이터 증강: VSTA를 통해 시연 데이터만으로 임의의 속도 궤적을 생성, 운동 시맨틱 손실 없이 속도 제어를 가능하게 함  
- 속도 조건화: 단일 VLA 모델 구조 내에 속도 정보를 주입해 다중 속도 학습 및 실행을 지원  
- 동적 속도 제어: 대형 멀티모달 모델과 협업해 저위험 구간은 가속, 고위험 구간은 감속하는 위험 기반(dynamic risk-aware) 속도 조절 구현

## 한계/리스크(Limitations)
- 초록 기준으로는 추가적인 제약 사항이나 실패 사례가 명시되지 않아 구체적 한계 파악이 불가하다.

## 실무 적용 아이디어(Practical Takeaways)
- 로봇 조작 데이터 파이프라인에 VSTA를 도입해 다양한 속도의 학습 데이터를 자동 생성  
- 기존 VLA 모델 입력에 속도 파라미터를 추가, 속도 조건화를 통해 실행 단계에서 속도 가변성 확보  
- 위험도 추정 모듈(예: 충돌 확률 예측)과 연동해 저·고위험 구간별 동적 속도 조절 시스템 설계

## 메타 정보
- 저자: Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding  
- 발행일: 2026년 6월 (arXiv v1 기준)  
- 카테고리: 로봇 제어, 멀티모달 학습

## 참고 링크
[https://arxiv.org/abs/2606.06491v1](https://arxiv.org/abs/2606.06491v1)
