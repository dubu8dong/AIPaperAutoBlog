# 피싱·쿠싱 첨부 탐지 데이터셋
**부제:** CIC-Trap4Phish: A Unified Multi-Format Dataset for Phishing and Quishing Attachment Detection

## 한 줄 결론
CIC-Trap4Phish는 Word·Excel·PDF·HTML·QR 코드 5개 포맷에 대해 실행 없는 정적 특징과 CNN·경량 언어 모델을 결합해 피싱·쿠싱 첨부파일을 탐지한다.

## TL;DR (요약)
- 사이버 공격에서 악성 이메일 첨부파일은 문서 포맷에 숨긴 악성 코드나 URL로 사용자를 속인다.  
- 기존 방어는 향상되었지만, 다양한 포맷을 아우르는 통합 데이터셋 부재로 첨단 모델 학습에 한계가 있다.  
- CIC-Trap4Phish는 Word, Excel, PDF, HTML, QR 코드 포함 5개 포맷의 악·양성 샘플을 수집했다.  
- 실행-불필요 정적 특징(구조·어휘·메타데이터) 선택과 머신러닝, CNN 및 경량 언어 모델로 높은 탐지 정확도를 보였다.

## 문제 정의(Problem)
피싱 공격자는 이메일 첨부파일에 악성 코드나 악의적인 URL을 숨겨 사용자 시스템을 감염시키고 민감 정보를 탈취한다.  
문서 파일(Word, Excel, PDF, HTML)과 QR 코드 이미지에 대한 기존 보안 솔루션은 점차 개선되고 있지만, 여전히 첨부파일 안의 숨겨진 위협을 완벽히 탐지하기 어렵다.  
또한, 피싱·쿠싱(Quishing)을 모두 포함하는 다양한 포맷의 악·양성 샘플을 통합한 공개 데이터셋이 부족하여 머신러닝·딥러닝 모델 학습에 제약이 있다.

## 제안 방법(Method)
1. 데이터셋 구축  
   - Word 문서, Excel 시트, PDF, HTML 페이지, QR 코드 이미지 등 5개 포맷의 악·양성 샘플을 수집·라벨링하여 통합 데이터셋(CIC-Trap4Phish)을 생성  
2. 실행-불필요 정적 특징 추출  
   - 문서 포맷별로 구조적(Structural), 어휘적(Lexical), 메타데이터(Metadata) 기반 지표를 추출  
   - SHAP(Shapley Additive Explanations) 분석과 피처 중요도(Feature Importance)를 결합해 각 포맷별 핵심 특징을 선별  
3. 머신러닝 모델 학습  
   - 선택된 특징 집합으로 Random Forest, XGBoost, Decision Tree 등 경량 모델을 훈련  
4. QR 코드 기반 탐지  
   - 이미지 기반: Convolutional Neural Networks(CNN)을 활용해 QR 코드 이미지 내 패턴 식별  
   - URL 기반: QR 코드 디코딩 후 경량 언어 모델로 URL 텍스트를 분석  

## 핵심 기여/차별점(Contributions)
- 다섯 가지 첨부파일 포맷(Word, Excel, PDF, HTML, QR 코드)을 아우르는 통합 악·양성 데이터셋 제공  
- 실행 없이 구조·어휘·메타데이터 특징을 추출하고 SHAP 기반 선택을 통해 모델 경량화  
- Random Forest, XGBoost, Decision Tree 및 CNN·경량 언어 모델을 결합해 높은 탐지율 달성  

## 한계/리스크(Limitations)
초록 기준으로는 실제 기업 환경에서의 시스템 통합 성능, 신종 포맷 대응 여부 등 구체적인 한계나 운영 리스크가 명시되지 않아 확인 불가.

## 실무 적용 아이디어(Practical Takeaways)
- 이메일 보안 솔루션에 문서 포맷별 정적 특징 추출 모듈을 통합해 첨부파일 선제 분석 도입  
- QR 코드 첨부파일에 대해 이미지·URL 이중 분석 워크플로우를 구축해 탐지 신뢰도 강화  
- SHAP 기반 피처 선택으로 머신러닝 모델을 경량화하고 필터링 속도 및 자원 효율을 개선  

## 메타 정보
- 저자: Fatemeh Nejati, Mahdi Rabbani, Mansur Mirani, Gunjan Piya, Igor Opushnyev, Ali A. Ghorbani, Sajjad Dadkhah  
- 발행일: 2026년 2월 (arXiv preprint)  
- 카테고리: 정보보안, 머신러닝

## 참고 링크
[https://arxiv.org/abs/2602.09015v1](https://arxiv.org/abs/2602.09015v1)
