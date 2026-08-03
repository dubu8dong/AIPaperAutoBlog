# 휴머노이드 회피 안전 제어 프레임워크

**부제:** PAC-MAN: Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball

## 한 줄 결론
온보드 카메라 기반 거리 정보와 제어 장벽 함수 강화학습을 결합한 PAC-MAN 프레임워크는 휴머노이드 로봇의 전신 회피 동작을 실환경에서 95% 성공률로 구현한다.

## TL;DR (요약)
- PAC-MAN은 제어 장벽 함수(Control Barrier Function) 기반 강화학습(RL)에 온보드 센싱을 통합해 휴머노이드의 회피 안전성을 보장한다.  
- 학습 시 각 관절 링크별 장벽 가이던스를 적용하고, 실전 배치 시에는 머리부 착탈 카메라의 깊이 지도만을 사용해 공을 감지한다.  
- 시뮬레이션 벤치마크에서 특권 상태 오라클(privileged state oracle) 성능에 근접하고, 실제 Unitree G1 로봇에 제로-샷(zero-shot)으로 적용해 95% 성공률을 달성했다.  
- 관찰 가능성에 따라 Joint-CBF 구조 성능이 크게 달라지며, 고정 카메라만으로는 제어 장벽 효과가 저하된다.  

## 문제 정의(Problem)
휴머노이드 로봇이 던져지는 물체를 전신으로 회피할 때, 전체 관절(whole-body)의 안전성을 보장하면서 실제 배치 환경의 제한된 센서 정보만으로도 실시간 회피 동작을 수행하는 것은 여전히 도전 과제이다. 특히, 실험실에서는 모션 캡처나 시스템 전역 상태를 활용한 회피 제어가 가능하지만, 현장 배치 시 온보드 카메라와 깊이 센서 등 제한된 정보만으로도 동일한 수준의 안전성과 반응성을 달성해야 한다.

## 제안 방법(Method)
1. Perception-Aware CBF-RL (PAC-MAN) 프레임워크  
   - 제어 장벽 함수(Control Barrier Function, CBF)와 강화학습(Reinforcement Learning, RL)을 결합해 학습 단계에서 안전 제약을 가이드함.  
   - 학습 시점에는 시뮬레이션상 특권 상태(privileged state)를 사용해 각 관절 링크(link)에 대한 충돌 회피 여유(clearance)를 평가하는 Joint-CBF 구조를 활용.  
2. 온보드 센싱 통합  
   - 배치(runtime) 시에는 헤드마운트 카메라로부터 얻은 세그멘테이션 마스크(segmentation-masked depth)만을 입력으로 활용.  
   - 실제 사용 가능한 센서 정보로도 학습된 정책이 작동하도록 zero-shot 전이 적용.  
3. Adversarial Motion Prior  
   - 강화학습 중 불안정한 회피 동작을 방지하기 위해 적대적 운동 사전(adversarial motion prior)을 도입, 비현실적 자세 변화를 규제.  

## 핵심 기여/차별점(Contributions)
- 온보드 관측에 민감한 CBF-RL 통합: 제한된 센서 정보만으로도 전체 관절 회피 안전성을 유지하는 PAC-MAN 구조 제안  
- 실험적 검증: 시뮬레이션의 any-link contact 벤치마크에서 특권 오라클에 근접한 성능을 보이며, 실제 로봇에 zero-shot 배치 시 95% 회피 성공률 달성  
- 관찰 가능성의 영향 분석: Joint-CBF와 Link-CBF 구조의 성능 변화를 비교, 고정 카메라 사용 시 추가 하드웨어(짐벌)나 런타임 필터링이 필요함을 규명  

## 한계/리스크(Limitations)
- Joint-CBF는 정확한 공 위치 관측이 가능할 때 최상의 성능을 보이나, 고정 카메라 단독 사용 시 학습 가이던스(direction)로만 활용하면 성능이 크게 저하된다.  
- 관찰 정확도를 높이기 위해 짐벌 또는 특권 런타임 필터가 필요하며, 이로 인한 시스템 복잡도 증가는 회피 정책의 일반화에 제약이 될 수 있다.  

## 실무 적용 아이디어(Practical Takeaways)
- CBF 기반 안전 가이드라인을 강화학습 정책에 직접 통합해, 복잡한 전신 로봇 제어에도 안전 제약을 유지하며 학습할 수 있다.  
- 실제 배치 환경의 센서 체계(고정 카메라, 깊이 센서)에 맞춘 정책 전이를 고려해, zero-shot 배치가 가능한 구조를 설계할 것.  
- 관측 불확실성 대비책으로 운동 사전 모델이나 추가 필터링(짐벌, 런타임 필터)을 함께 도입해 제어 성능 저하를 방지해야 한다.  

## 메타 정보
- 저자: Lizhi Yang, Junheng Li, Aaron D. Ames  
- 발행일: 2026-07-xx (arXiv 제출일 기준)  
- 카테고리: 로보틱스(Robotics), 강화학습(Reinforcement Learning), 안전 제어(Safety Control)  

## 참고 링크
[https://arxiv.org/abs/2607.28623v1](https://arxiv.org/abs/2607.28623v1)
