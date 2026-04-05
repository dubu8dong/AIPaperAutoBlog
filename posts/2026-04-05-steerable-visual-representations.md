# 언어로 제어하는 비주얼 표현

**부제:** Steerable Visual Representations

## 한 줄 결론
비전 트랜스포머 내부에 자연어 프롬프트를 조기 결합해 시각 표현의 steerability를 확보하면서도 기본적인 표현 품질을 유지한다.

## TL;DR (요약)
- 사전 학습된 비전 트랜스포머(ViT)는 이미지 검색·분류·분할 등에 범용적으로 활용되나, 가장 두드러진 시각 단서에만 집중해 특정 객체 강조가 어렵다.  
- 기존 비전-언어 모델은 주로 후결합(late fusion)을 사용해 표현이 언어 중심으로 치우치며, 일반적인 비주얼 태스크 성능이 저하될 수 있다.  
- 본 논문은 경량 크로스어텐션을 활용해 자연어 프롬프트를 ViT 인코더 내부 레이어에 삽입하는 early fusion 방식을 제안한다.  
- 글로벌(global)·로컬(local) 수준에서 representational steerability를 평가하는 새로운 벤치마크를 도입하고, 이상 탐지 및 개인화 객체 분류에서 전용 기법과 동등 또는 우수한 성능을 보인다.  
- 모델은 제로샷 상황에서도 분포 밖(out-of-distribution) 작업에 일반화하는 능력을 입증한다.

## 문제 정의(Problem)
사전 학습된 비전 트랜스포머(DINOv2, MAE 등)는 이미지에서 가장 두드러진(salient) 단서를 중심으로 범용 특징을 추출해, 검색(retrieval), 분류(classification), 분할(segmentation) 등 다양한 다운스트림 태스크에 활용된다.  
그러나 사용자가 특정 객체나 덜 강조된 개념으로 초점을 이동하려 해도, 해당 표현을 유도하는 수단이 없어 인터랙티브 제어나 맞춤형 분석이 어려운 한계가 있다.  
반면 멀티모달 대형 언어 모델(LLM)은 자연어 프롬프트로 지시가 가능하나, 생성된 표현은 언어 중심으로 편중되어 일반적인 비주얼 태스크 성능이 저하될 수 있다.

## 제안 방법(Method)
- 비주얼 인코더의 각 레이어에 경량 크로스어텐션 모듈을 삽입해, 자연어 프롬프트 토큰과 이미지 특징(feature) 간 상호작용을 조기에 결합(early fusion)한다.  
- 크로스어텐션 모듈은 글로벌(global)·로컬(local) 수준에서 텍스트 지시에 따른 표현 변화를 유도하며, 추가 파라미터는 최소화했다.  
- 학습 단계에서는 기존 사전 학습된 ViT 위에 자연어-시각 통합을 위한 미세 조정(fine-tuning)을 수행하며, 자가 감독(self-supervised) 학습 손실을 활용해 레이블 없는 데이터에서도 steerability를 확보한다.  
- 새로운 벤치마크에는 특정 객체에 집중(seeking), 무관 영역 무시(ignore) 평가 등이 포함되며, 표현의 steerability를 정량화한다.

## 핵심 기여/차별점(Contributions)
- 경량 크로스어텐션 기반 early fusion 구조 제안: 비주얼 인코더 내부 레이어에 자연어 지시 주입으로 steerability 확보.  
- representational steerability 벤치마크 도입: 글로벌·로컬 수준의 객체 집중 능력 및 무시 능력을 평가할 수 있는 지표 개발.  
- 다중 다운스트림 태스크 성능 검증: 이상 탐지(anomaly detection) 및 개인화 객체 분류(personalized object discrimination)에서 전용 기법과 동등하거나 우수한 성능, 제로샷 out-of-distribution 일반화 능력 입증.

## 한계/리스크(Limitations)
초록 기준으로는 모델의 연산 비용 증가량, 실시간 응답성, 다양한 언어 및 도메인에 대한 범용성 등 상세한 한계는 확인 불가.

## 실무 적용 아이디어(Practical Takeaways)
- 클라우드 기반 비전 서비스에 크로스어텐션 모듈을 추가해 자연어 프롬프트로 이미지 검색·분석 기능을 고도화.  
- 이상 탐지 시스템에 steerable 표현을 도입해 특정 결함 유형에 민감하게 반응하는 감시 모델을 구축.  
- 개인화 상품 추천 파이프라인에서 고객 언어 지시에 따라 강조할 시각 특징을 조정해 추천 품질 개선.

## 메타 정보
- 저자: Jona Ruthardt, Manu Gaur, Deva Ramanan, Makarand Tapaswi, Yuki M. Asano  
- 발행일: arXiv preprint 2604.02327v1 (2026년 4월)  
- 카테고리: Computer Vision, Machine Learning

## 참고 링크
[https://arxiv.org/abs/2604.02327v1](https://arxiv.org/abs/2604.02327v1)
