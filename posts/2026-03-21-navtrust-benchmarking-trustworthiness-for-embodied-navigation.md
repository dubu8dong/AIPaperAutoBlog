# 내비게이션 신뢰도 평가
**부제:** NavTrust: Benchmarking Trustworthiness for Embodied Navigation

## 한 줄 결론
NavTrust는 RGB, Depth, 자연어 지시문 손상을 통합한 최초의 벤치마크로, 최신 Embodied Navigation 모델의 강인성 취약점을 체계적으로 드러냅니다.

## TL;DR (요약)
- 기존 Vision-Language Navigation 및 Object-Goal Navigation 연구는 정상 조건 성능에만 집중합니다.
- NavTrust는 현실적인 RGB·Depth 왜곡과 지시문 변형을 생성해 하나의 프레임워크에서 평가합니다.
- 7개 최첨단 모델 평가 결과, 손상 환경에서 성능이 대폭 하락함을 확인했습니다.
- 네 가지 완화 전략(데이터 증강, 적응형 정규화, 앙상블, 손상 인식)을 실험하여 강인성 향상 효과를 분석했습니다.
- 실제 모바일 로봇 배포 실험을 통해 시뮬레이션과 유사한 성능 개선 결과를 얻었습니다.

## 문제 정의(Problem)
Embodied Navigation은 두 가지 주요 과제로 나뉩니다.  
1) Vision-Language Navigation(VLN): 자연어 지시를 따라 경로를 탐색  
2) Object-Goal Navigation(OGN): 지정된 대상 객체로 이동  

그러나 기존 연구는 주로 “정상(nominal) 환경”에서의 성능에 집중해, 실제 환경에서 자주 발생하는 입력 모드 손상(corruption)을 무시해 왔습니다.  
- RGB(컬러 영상): 노이즈, 블러, 밝기·대비 변화  
- Depth(깊이 정보): 점 손실, 왜곡, 거리 오차  
- 자연어 지시문: 철자 오류, 구문 재배열, 축약 등  

이로 인해 실제 로봇 시스템에 적용 시 예측하지 못한 성능 저하가 발생하고, 신뢰성 있는 내비게이션 구현이 어렵습니다.

## 제안 방법(Method)
NavTrust는 다음 단계를 거쳐 Embodied Navigation 에이전트의 신뢰성을 평가합니다.

1. 손상 시나리오 정의  
   - RGB: 가우시안 노이즈, 모션 블러, 조명 변화  
   - Depth: 랜덤 점 제거, 거리 왜곡, 스케일 오차  
   - 지시문: 철자 오류 삽입, 문장 순서 바꾸기, 동의어 치환  

2. 통합 벤치마크 구축  
   - VLN 및 OGN 데이터셋에 동일한 손상을 일관성 있게 적용  
   - 손상 강도별 구간을 설정해 단계별 성능 측정  

3. 모델 평가  
   - Uni-NaVid, ETPNav 등 7개 최신 에이전트 대상으로 손상 환경별 내비게이션 성공률, SPL(Success weighted by Path Length) 등 지표 비교  

4. 완화 전략 적용  
   - 데이터 증강(Data Augmentation)  
   - 적응형 정규화(Adaptive Normalization)  
   - 모델 앙상블(Ensemble Learning)  
   - 손상 인식 모듈(Corruption-aware Module)  

5. 실제 로봇 실험  
   - 모바일 로봇 플랫폼에 모델 배포  
   - 시뮬레이션 손상과 유사한 현실 환경 오염 조건에서 성능 재검증  

## 핵심 기여/차별점(Contributions)
- 다양한 RGB·Depth·지시문 손상을 통합 적용한 최초의 Embodied Navigation 신뢰성 벤치마크  
- 7개 최첨단 모델 평가를 통해 현실적 손상 시 성능 저하 지점을 체계적으로 식별  
- 4가지 완화 전략 비교 분석 및 실제 로봇 실험을 통한 타당성 검증  

## 한계/리스크(Limitations)
- 시뮬레이션 기반 손상과 실제 환경 잡음 간에는 완전한 일치가 어려울 수 있습니다.  
- 제안된 완화 기법이 모든 유형의 손상에 대해 보편적 개선을 보장하는지는 추가 연구가 필요합니다.  
- 손상 생성 매개변수, 완화 전략 상세 구현 등은 초록 기준으로는 확인 불가합니다.

## 실무 적용 아이디어(Practical Takeaways)
- 개발 중인 로봇 내비게이션 시스템에 RGB/Depth 손상 시나리오를 추가해 테스트 커버리지 확대  
- 자연어 지시 처리 모듈에 지시문 오탈자·구문 변형 자동 생성 기능을 결합해 견고성 검증  
- 제안된 완화 기법(데이터 증강, 적응형 정규화, 앙상블 등)을 프로토타입에 적용해 성능 변화를 모니터링  

## 메타 정보
- 저자: Huaide Jiang, Yash Chaudhary, Yuping Wang, Zehao Wang, Raghav Sharma, Manan Mehta, Yang Zhou, Lichao Sun, Zhiwen Fan, Zhengzhong Tu, Jiachen Li  
- 발행일: 초록 기준으로는 확인 불가  
- 카테고리: arXiv – 로보틱스, 인공지능, 컴퓨터 비전  

## 참고 링크
[https://arxiv.org/abs/2603.19229v1](https://arxiv.org/abs/2603.19229v1)
