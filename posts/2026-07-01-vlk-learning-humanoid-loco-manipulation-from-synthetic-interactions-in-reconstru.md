# 합성장면 휴머노이드 동작 학습
**부제:** VLK: Learning Humanoid Loco-Manipulation from Synthetic Interactions in Reconstructed Scenes

## 한 줄 결론
재구성된 실내 장면에서 합성된 시각-언어-운동 데이터를 활용해 휴머노이드 로코-매니퓰레이션의 sim-to-real 성능을 확보했다.

## TL;DR (요약)
- 휴머노이드 로코-매니퓰레이션에는 이미지, 언어 지시, 전신 운동 궤적이 동기화된 대규모 데이터가 필요하다.  
- 본 연구는 3D Gaussian Splatting 기반 실내 장면 재구성과 합성 궤적 생성을 통해 48,000개의 시각-언어-운동(VLK) 데이터를 생성한다.  
- VLK 정책은 짧은 전신 운동 궤적을 예측하고, 전신 트래커를 통해 Unitree G1 로봇에 적용해 내비게이션 및 단일 객체 운반을 수행한다.  
- 합성된 데이터가 sim-to-real 인식 기반 로코-매니퓰레이션 학습에 효과적임을 실험적으로 입증했다.  

## 문제 정의(Problem)
휴머노이드 로코-매니퓰레이션은 로봇의 시점(egocentric) 영상, 언어 지시문, 그리고 전신 운동 궤적을 연결해 전신 동작을 생성해야 한다. 이를 위해 세 요소가 완벽히 동기화된 대규모 데이터셋이 필요하나, 기존에는 해당 튜플(시각·언어·운동)을 한꺼번에 제공하는 대규모 데이터 소스가 없다.

## 제안 방법(Method)
논문은 다음 단계로 구성된 합성 파이프라인을 제안한다.
1. 3D Gaussian Splatting 기법을 활용해 실내 환경을 메트릭 규모로 재구성  
2. 재구성된 장면과 특권(scene privileged) 정보를 이용해 내비게이션 및 객체 상호작용 궤적을 합성  
3. 궤적 생성 후 egocentric 관점에서 영상과 언어 명령을 렌더링해 시각-언어-운동(VLK) 데이터 48,000쌍을 자동 수집  
4. VLK 정책을 학습해 짧은 시간 프레임의 전신 운동 궤적을 예측  
5. 예측된 궤적을 전신 트래커(whole-body tracker)를 통해 Unitree G1 물리 휴머노이드에 시뮬-투-리얼(sim-to-real) 방식으로 실행  

## 핵심 기여/차별점(Contributions)
- 대규모 합성 시각-언어-운동(VLK) 데이터셋 48,000개를 무인간 개입으로 생성  
- 3D Gaussian Splatting 기반 장면 재구성과 특권 정보 활용 궤적 합성 파이프라인  
- VLK 정책과 전신 트래커의 결합을 통한 sim-to-real 휴머노이드 로코-매니퓰레이션 실험적 검증  

## 한계/리스크(Limitations)
실험이 Unitree G1 로봇과 단일 객체 운반 과제로 한정되어 있어, 다양한 로봇 플랫폼 및 복합 작업으로의 일반화는 초록 기준으로는 확인 불가하다. 또한 합성된 데이터가 실제 환경의 모든 변수를 담아내는지, 실시간 제어 성능과 견고성에 대한 평가는 초록만으로는 확인할 수 없다.

## 실무 적용 아이디어(Practical Takeaways)
- 3D Gaussian Splatting을 활용해 실내 환경을 빠르게 메트릭 스케일로 재구성하여 학습용 시뮬레이션 환경 구축  
- 합성 시나리오 기반 시각-언어-운동(VLK) 대규모 데이터를 생성해 소량의 실제 데이터로 보완  
- VLK 정책과 전신 트래커를 통합해 다양한 휴머노이드 플랫폼에서 sim-to-real 제어 파이프라인 설계  

## 메타 정보
- 저자: Yen-Jen Wang, Jiaman Li, Sirui Chen, Takara E. Truong, Pei Xu, Pieter Abbeel, Rocky Duan, Koushil Sreenath, Angjoo Kanazawa, Carmelo Sferrazza, Guanya Shi, Karen Liu  
- 발행일: 2026년 6월 (arXiv preprint 2606.30645v1)  
- 카테고리: Robotics (cs.RO), Computer Vision (cs.CV), Machine Learning (cs.LG)  

## 참고 링크
[https://arxiv.org/abs/2606.30645v1](https://arxiv.org/abs/2606.30645v1)
