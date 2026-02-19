# 인식 기반 휴머노이드 파쿠르

**부제:** Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching

## 한 줄 결론
시각 기반 모션 매칭과 강화학습 증류를 결합해 휴머노이드 로봇이 자율적으로 장시간 파쿠르 동작을 수행할 수 있음을 보였다.

## TL;DR (요약)
- 모션 매칭(Motion Matching)을 통해 사람의 원자 단위 이동 기술을 특징 공간(nearest‐neighbor)에서 연속 연결하여 장시간 경로를 생성한다.  
- 생성된 궤적에 맞춰 모션 트래킹 강화학습 테크닉으로 전문가(expert) 정책을 학습하고, DAgger와 강화학습을 결합해 단일 심층 학생(student) 정책으로 증류(distillation)한다.  
- 온보드(depth) 센서와 이산(discrete) 2D 속도 명령만으로 장애물을 인식해 넘기·오르기·도약·구르기 기술을 선택 수행한다.  
- Unitree G1 휴머노이드 로봇 실험에서 최대 1.25m 높이(로봇 신장 대비 96%) 장애물 등 실제 환경에서 장시간·다중 장애물 파쿠르를 시연했다.  

## 문제 정의(Problem)
최근 휴머노이드 로코모션 연구는 다양한 지형에서 안정적 보행 성능을 보였으나, 여전히 인간처럼 민첩하고 적응력 있는 동적 동작을 재현하는 데 제약이 있다.  
특히 복잡한 환경에서의 파쿠르(parkour) 동작은
- 낮은 레벨의 제어 안정성뿐 아니라  
- 인간과 유사한 운동 표현성(expressiveness)  
- 장시간 스킬 조합(long‐horizon skill composition)  
- 시각 기반 의사결정(perception‐driven decision‐making)  
요구사항을 동시에 충족해야 한다.  

## 제안 방법(Method)
1. Motion Matching 기반 스킬 체인 구성  
   - 휴먼 모션 데이터에서 추출한 원자 단위 스킬(atomic human skills)을 특징(feature) 공간에서 최근접 이웃(nearest‐neighbor) 탐색으로 연결  
   - 부드러운 전이(smooth transition)를 유지하는 장시간(k‐horizon) 기하학 경로를 생성  
2. 전문가 정책 학습  
   - 생성된 궤적을 따라 움직이는 모션 트래킹(Motion‐Tracking) 강화학습(reinforcement learning)으로 전문가(expert) 수준의 서브정책(sub‐policy) 획득  
3. 증류(Distillation) 및 단일 정책 통합  
   - DAgger(Data Aggregation) 기법과 강화학습을 결합  
   - 깊이(depth) 센서 입력과 이산 2D 속도 명령만 사용하는 멀티스킬 학생(student) 단일 정책으로 통합  
4. 자율·인식 기반 실행  
   - 온보드(depth) 센서로 장애물 기하학과 높이를 판단  
   - 넘기(step over), 오르기(climb onto), 도약(vault), 구르기(roll off) 중 적절한 스킬 선택  
   - 실시간 폐쇄형(closed‐loop) 피드백으로 장애물 변화에 적응  

## 핵심 기여/차별점(Contributions)
- 휴먼 원자 스킬을 특징 공간에서 모otion Matching 방식으로 연결해 복합/장시간 파쿠르 경로를 생성  
- DAgger와 강화학습을 결합한 증류 파이프라인으로 멀티스킬 강화학습 전문가 정책을 단일 학생 정책으로 통합  
- 실세계 Unitree G1 로봇에서 최대 1.25m(96% 신장) 장애물 등 난이도 높은 환경을 포함한 다중 장애물 파쿠르 성능 검증  

## 한계/리스크(Limitations)
초록 기준으로는 특정 환경 조건 외 일반화 성능, 학습 데이터 요구량, 정책 적용 중 안전성 한계 등을 확인할 수 없다.

## 실무 적용 아이디어(Practical Takeaways)
- 모션 매칭 기반 스킬 체인 모듈을 도입해 다양한 인간 모션 데이터를 로봇 제어에 활용하는 파이프라인 구축  
- DAgger와 강화학습 증류 기법으로 여러 전문가 정책을 단일 정책으로 통합해 실행 효율성 증대  
- 온보드(depth) 센서와 경량화된 2D 속도 제어 인터페이스로 실제 로봇 시스템에 자율 장애물 회피 기능 적용  

## 메타 정보
- 저자: Zhen Wu, Xiaoyu Huang, Lujie Yang, Yuanhang Zhang, Koushil Sreenath, Xi Chen, Pieter Abbeel, Rocky Duan, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, C. Karen Liu  
- 발행일: 확인 불가 (arXiv preprint)  
- 카테고리: 확인 불가  

## 참고 링크
[https://arxiv.org/abs/2602.15827v1](https://arxiv.org/abs/2602.15827v1)
