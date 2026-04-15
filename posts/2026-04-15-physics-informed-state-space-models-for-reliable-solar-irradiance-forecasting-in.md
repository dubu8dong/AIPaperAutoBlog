# 물리 기반 태양광 예보모델

**부제:** Physics-Informed State Space Models for Reliable Solar Irradiance Forecasting in Off-Grid Systems

## 한 줄 결론
대기 및 천체 역학 제약을 내재화한 경량 물리 기반 네트워크가 오프그리드 태양광 방사 조도 예측의 위상 지연과 야간 오작동을 해소한다.

## TL;DR (요약)
- 기존 딥러닝 태양광 예측 모델은 구름 변화 시 심각한 위상 지연과 야간에도 출력을 예측하는 이상(anomaly)을 보임.  
- Thermodynamic Liquid Manifold Network는 15개 기상·기하 변수 데이터를 쿱만 연선 리만 다양체에 투영해 복잡한 기후 동역학을 선형화함.  
- 스펙트럴 보정 모듈과 열역학 α-게이트로 대기 투명도와 이론적 맑은 하늘 모델을 결합, 천체 기하학 준수를 강제함.  
- 반건조 기후 5년 검증에서 RMSE 18.31 Wh/m², 상관계수 0.988, 야간 오류 제로, 고주파 전이 응답 30분 이내를 달성함.

## 문제 정의(Problem)
오프그리드 자율 태양광 시스템의 안정적 운영에는 기상 및 천체 물리 법칙을 준수하는 고신뢰 예측이 필수적이다. 그러나 기존 데이터 기반 딥러닝 모델은 클라우드 트랜지언트(rapid transient) 구간에서 심각한 시간 위상 지연(phase lag)을 보이고, 야간에도 물리적으로 불가능한 전력 생산을 예측하는 치명적 이상 현상을 나타낸다.

## 제안 방법(Method)
Thermodynamic Liquid Manifold Network를 도입하여 다음 과정을 수행한다.
- 입력되는 15개 기상(예: 기온, 습도, 구름광학두께) 및 태양 기하 변수(예: 일일 태양 고도)를 쿱만(Koopman) 선형화된 리만 다양체(Riemannian manifold)로 사상(mapping)  
- 스펙트럴 보정(Spectral Calibration) 유닛을 통해 대기 광학 특성을 보정  
- 곱셈적 열역학 α-게이트(Thermodynamic Alpha-Gate)로 실시간 대기 투명도 정보와 이론적 맑은 하늘(clear-sky) 경계 모델을 융합  
- 천체 기하학 규칙을 구조화하여 야간 예측값을 완전히 차단하고, 클라우드 변동 시 실질적 제로 위상 지연을 유지

## 핵심 기여/차별점(Contributions)
- 물리적 천체 기하학 및 대기 열역학 제약을 네트워크 구조에 직접 통합  
- 15개 변수의 쿱만 선형화를 통한 복잡한 기후 동역학 리만 다양체 사상  
- 초경량(63,458개 학습 파라미터) 모델로 야간 오류 제로 및 고주파 전이에 30분 이하 응답 보장

## 한계/리스크(Limitations)
- 검증은 반건조(semi-arid) 기후 5년 데이터에 한정되어 일반 타 기후대 적용성은 확인 불가  
- 초록 기준으로 학습·추론 연산 시간, 하드웨어 요구사항 등 세부 성능 정보는 제공되지 않음  
- 모델의 데이터 소스 편향(bias) 및 이상 상황에서의 안정성 검증 결과는 초록에서 확인 불가

## 실무 적용 아이디어(Practical Takeaways)
- 에지(edge) 디바이스 제어를 위한 경량 물리 기반 모델 구조 설계  
- 실시간 대기 광학 정보와 이론 모델을 결합해 야간 예측 차단 및 위상 지연 최소화  
- 쿱만 연선 변환을 활용해 복잡한 동적 시스템을 비교적 단순한 선형 네트워크로 모델링

## 메타 정보
- 저자: Mohammed Ezzaldin Babiker Abdullah  
- 발행일: 2026년 4월 (arXiv Preprint)  
- 카테고리: Solar Irradiance Forecasting, Physics-Informed Machine Learning

## 참고 링크
[https://arxiv.org/abs/2604.11807v1](https://arxiv.org/abs/2604.11807v1)
