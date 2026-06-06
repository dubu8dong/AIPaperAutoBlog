# 휴머노이드 전신제어 HANDOFF
**부제:** HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers

## 한 줄 결론
컴팩트한 작업-제어 인터페이스와 멀티-티처 증류를 결합해 휴머노이드 전신제어의 범용성과 성능을 향상시켰다.

## TL;DR (요약)
- HANDOFF는 명시적이고 컴팩트한 작업-제어(command space) 인터페이스를 제안한다.  
- 멀티-티처 Kullback–Leibler(KL) 증류와 문맥 조건부 게이팅(context-conditioned gating)을 도입해 세 가지 전문가 모델을 하나의 학생 모델로 통합한다.  
- 제안된 혼합 전문가(Mixture-of-Experts) 구조는 모션 추적, 보행, 낙상 복구를 모두 지원한다.  
- Unitree G1 로봇에서 SOTA 수준의 속도 추적을 달성하고 넓은 조작 워크스페이스를 확보했으며, VLM 기반 자연어 플래너와 함께 하드웨어 실험을 시연했다.  

## 문제 정의(Problem)
휴머노이드 로봇을 실제 환경에 배치하려면 작업 계획(task planning)과 전신 제어(whole-body control)를 연결하는 명령(command) 인터페이스의 설계가 핵심이다. 기존 전신 제어기는 일반적으로 밀집된 자세‧공간 참조(kinematic or spatial references)를 필요로 하며, 이는 작업 의미(task semantics)에서 자동으로 합성하기 어렵다. 그 결과 플래너와 제어기 간 통합이 복잡해지고, 다양한 조작(manipulation) 스킬을 효율적으로 수행하기 어렵다.

## 제안 방법(Method)
- 컴팩트하고 명시적인 작업-제어 인터페이스를 정의하여 직관성, 일반성, 모듈성, 표현력(expressiveness)을 확보한다.  
- 세 가지 상호보완적 교사 모델(모션 추적, 보행, 낙상 복구)로부터 학생 모델로 지식을 전이하는 멀티-티처 Kullback–Leibler(KL) 증류를 수행한다.  
- 문맥 조건부 게이팅(context-conditioned gating) 메커니즘을 통해 상황에 맞는 전문가 경로를 선택하며, 전체를 하나의 Mixture-of-Experts 학생 네트워크로 통합한다.  
- Unitree G1 플랫폼에서 속도 추적(velocity tracking) 성능을 측정하고 조작(workspace) 범위를 평가했다.  
- VLM(Visual Language Model) 기반 에이전틱 플래너(agentic planner)를 통해 자연어로 지시된 작업을 데이터 수집 없이 바로 실행하는 하드웨어 실험을 수행했다.

## 핵심 기여/차별점(Contributions)
- 컴팩트한 작업-제어 인터페이스를 통해 플래너와 제어기 간 통합 복잡도를 낮추고 다양한 조작 스킬을 표현 가능하게 함  
- 멀티-티처 KL 증류 및 문맥 조건부 게이팅을 결합한 Mixture-of-Experts 구조로 세 가지 전문화된 기능을 하나의 모델에 통합  
- Unitree G1에서 SOTA 수준의 속도 추적 성능과 넓은 조작 워크스페이스를 달성하고, 자연어 기반 실시간 하드웨어 시연을 통해 실용성을 입증  

## 한계/리스크(Limitations)
- 초록 기준으로는 모델의 일반화 성능, 안전성 검증, 다른 플랫폼 이식성 등에 대한 상세한 한계점 확인 불가  

## 실무 적용 아이디어(Practical Takeaways)
- 컴팩트한 작업-제어 인터페이스 설계를 통해 플래너와 제어기 간 사양 차이를 줄이고 개발 효율을 높일 수 있다.  
- 멀티-티처 증류 방식을 도입해 목적별로 전문화된 컨트롤러를 하나의 범용 모델로 통합하는 전략을 적용해보자.  
- 문맥 조건부 게이팅을 활용해 런타임 상황에 따라 모드를 자동 전환하도록 구현하면 안전성과 유연성을 동시에 개선할 수 있다.  

## 메타 정보
- 저자: Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin, Georgia Gkioxari, Aaron Ames  
- 발행일: 2026년 6월 (arXiv preprint)  
- 카테고리: Robotics, Control, Machine Learning  

## 참고 링크
[https://arxiv.org/abs/2606.06493v1](https://arxiv.org/abs/2606.06493v1)
