# 효율적 경로 중계 온-폴리시 증류  
**부제:** Pass the Baton: Trajectory-Relayed On-Policy Distillation

## 한 줄 결론
Relay-OPD는 교사 모델의 짧은 개입으로 prefix 실패를 완화해 온-폴리시 증류 성능과 학습 효율을 동시에 개선한다.

## TL;DR (요약)
기존 온-폴리시 증류(On-Policy Distillation)는 학생 모델이 잘못된 prefix(초기 경로)를 생성하면 이후 생성이 모두 왜곡되는 prefix 실패 문제가 있다.  
Relay On-Policy Distillation(Relay-OPD)은 prefix 실패가 감지된 시점에 교사 모델이 잠시 개입(Relay)해 올바른 토큰 시퀀스를 생성한 뒤 학생 모델로 이어받게 한다.  
중계 예산(relay budget)을 제한해 학생 정책에서 과도하게 벗어나지 않으면서 중요한 초기 위치에 개입을 집중한다.  
수학적 추론 벤치마크 8종에서 표준 OPD 대비 평균 +5.73% 성능 향상과 훈련 시퀀스 길이 50% 이상 절감을 달성했다.

## 문제 정의(Problem)
온-폴리시 증류는 학생 모델의 자체 생성 경로(trajectory)에서 토큰 수준(token-level) 감독 신호를 즉시 얻어 학습한다.  
그러나 학생 모델이 초기(prefix)에서 잘못된 추론 방향으로 벗어나면 이후 모든 생성이 틀린 방향을 따라가면서 부정확한 감독 신호가 누적되고 계산 자원이 낭비되는 prefix 실패(prefix failure) 문제가 있다.  
이로 인해 증류 성능이 저하되고 학습 효율이 떨어진다.

## 제안 방법(Method)
Relay-OPD는 다음 단계로 동작한다.
- Prefix 실패를 유발하는 트리거 지점(trigger points)을 라벨 없이 자동 감지  
- 감지된 지점에서 교사 모델(teacher)을 일정 구간 개입(relay)시켜 올바른 토큰 시퀀스(teacher leg) 생성  
- 교사의 개입 구간 후 학생 모델(student)이 다시 토큰 생성을 이어가도록 전환  
- 전체 생성 경로(teacher leg + student 후속 생성)를 기반으로 학생 모델을 최적화  
- 중계 예산(relay budget)을 설정해 개입 횟수와 범위를 제한, 학생 정책에서 크게 벗어나지 않도록 설계  

## 핵심 기여/차별점(Contributions)
- 라벨 없는 prefix 실패 감지와 교사-학생 중계를 결합한 Relay-OPD 프레임워크 제안  
- 중계 예산(relay budget)으로 개입을 초기 위치에 집중시켜 학생 정책의 과도 이탈 방지  
- 8개 수학 추론 벤치마크에서 표준 OPD 대비 평균 +5.73% 성능 향상, FastOPD 대비 +1.49% 개선 및 학습 시퀀스 길이 50% 이상 절감  

## 한계/리스크(Limitations)
- 수학적 추론 벤치마크 외 다른 NLP 과제에서의 일반화 여부는 초록 기준으로는 확인 불가  
- prefix 실패 감지 로직과 relay budget 설정에 필요한 하이퍼파라미터 튜닝 비용 발생 가능  
- 교사 모델 개입으로 인한 계산 비용 증가 및 응답 지연 영향은 초록 기준으로는 확인 불가  

## 실무 적용 아이디어(Practical Takeaways)
- 온-폴리시 증류 도입 시 prefix 실패 모니터링 및 자동 감지 모듈을 함께 구축  
- Relay-OPD 방식을 참고해 교사 모델 개입 시점과 범위를 설정하는 트리거 로직 설계  
- relay budget을 실험적으로 조정해 성능 개선과 학습 비용 절감 사이의 최적 균형점 탐색  

## 메타 정보
- 저자: Haolei Xu, Xiaowen Xu, Haiwen Hong, Zixuan Ni, Hongxing Li, Yiwen Qiu, Weiming Lu, Yongliang Shen  
- 발행일: 초록 기준으로는 확인 불가  
- 카테고리: 자연어 처리(NLP), 강화 학습(RL), 모델 증류(Model Distillation)

## 참고 링크
[https://arxiv.org/abs/2607.26057v1](https://arxiv.org/abs/2607.26057v1)
