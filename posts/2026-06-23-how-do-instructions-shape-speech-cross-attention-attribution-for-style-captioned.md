# TTS 스타일 어텐션 해부

**부제:** How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech

## 한 줄 결론
자연어 스타일 캡션이 TTS(텍스트-투-스피치) 음성 생성에 미치는 영향은 크로스-어텐션 어트리뷰션을 통해 계층별·단계별로 정량화할 수 있다.

## TL;DR (요약)
- 스타일 캡션을 활용한 표현형 TTS에서 개별 단어가 음성 특성에 미치는 영향을 분석하는 것이 목적이다.  
- DAAM(Diffusion Activation Attribution Mapping) 프레임워크를 음성 확산 모델에 처음 적용해, 25개 레이어와 24개 확산 단계에서 토큰별 히트맵을 추출한다.  
- 120개의 스타일 캡션과 30개의 텍스트 조합(총 3,600회 분석)으로 실험한 결과, 스타일 토큰은 전역적 제어, F0 및 에너지와의 상관관계, 특정 단계·레이어에서 중요도가 극대화됨을 확인했다.  

## 문제 정의(Problem)
스타일 캡션형 TTS 시스템은 자연어 지시문으로 음색·템포·감정 등 음성 특성을 제어한다. 그러나 개별 단어 수준에서 어떻게 음향 출력에 기여하는지 불분명하여, 실패 모드 진단과 세밀한 컨트롤을 위해 내부 작동 원리 규명이 필요하다.

## 제안 방법(Method)
- DAAM(Diffusion Activation Attribution Mapping) 프레임워크를 음성 확산(스피치 디퓨전) 모델에 처음 도입.  
- CapSpeech-TTS를 대상으로, 25개 레이어(layer)와 24개 ODE(Ordinary Differential Equation) 확산 단계별로 입력 캡션의 각 토큰에 대한 크로스-어텐션 기여도를 히트맵 형태로 추출.  
- 120개의 스타일 캡션(style caption)과 30개의 텍스트(transcript) 조합을 실험해 총 3,600회 샘플을 분석하고, 시간 축 분산(variance), 주기성 특징(F0), 에너지 및 어텐션 엔트로피(entropy) 등 주요 지표와의 상관관계를 조사.

## 핵심 기여/차별점(Contributions)
- 스타일 캡션형 음성 확산 모델에 DAAM 기반 크로스-어텐션 어트리뷰션을 적용한 최초 연구  
- 스타일 토큰이 컨텐츠·기능(function) 토큰 대비 시간적 분산이 낮아 전역 구속(global conditioning) 역할을 함을 정량적으로 입증  
- 스타일 어텐션이 기본 주파수(F0) 및 에너지와 유의한 상관관계를 보이며, 초기 확산 단계와 심층 레이어에서 중요도가 최고점을 찍는 현상을 발견  

## 한계/리스크(Limitations)
- CapSpeech-TTS에 한정된 실험으로, 다른 TTS 아키텍처 또는 비확산(different paradigm) 모델로의 일반화는 초록 기준으로는 확인 불가  
- 25개 레이어와 24개 단계에서 어트리뷰션을 수행하는 과정의 계산 비용 및 실시간 적용 가능성에 대한 언급은 없음  
- 사용자 경험(청취자 평가)이나 직접적인 음성 품질 개선 실험은 포함되지 않음  

## 실무 적용 아이디어(Practical Takeaways)
- TTS 개발 시 크로스-어텐션 어트리뷰션을 도입해 스타일 단어의 영향력을 레이어·단계별로 시각화하고, 컨트롤 파라미터 튜닝에 활용  
- 어텐션 기반 지표(F0·에너지 연관성)를 모니터링하여 스타일 표현이 과다 혹은 과소 조정되는 단계 식별  
- 특정 레이어(예: 17층)와 초기 ODE 단계에서 스타일 중요도가 극대화된다는 점을 고려해, 경량화된 어텐션 모듈이나 프루닝(pruning) 전략을 설계  

## 메타 정보
- 저자: Nityanand Mathur, Hamees Sayed, Wasim Madha, Apoorv Singh, Sameer Khurana, Akshat Mandloi, Sudarshan Kamath  
- 발행일: 2026년 6월 (arXiv v1)  
- 카테고리: Audio and Speech Processing (eess.AS), Machine Learning (cs.LG)  

## 참고 링크
[https://arxiv.org/abs/2606.20532v1](https://arxiv.org/abs/2606.20532v1)
