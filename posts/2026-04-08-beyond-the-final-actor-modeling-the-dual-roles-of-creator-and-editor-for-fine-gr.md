# 세밀한 LLM 생성 텍스트 검출

**부제:** Beyond the Final Actor: Modeling the Dual Roles of Creator and Editor for Fine-Grained LLM-Generated Text Detection

## 한 줄 결론
RACE는 생성자(Creator)와 편집자(Editor)의 특징을 분리해 네 가지 텍스트 유형을 정밀 검출하는 방법을 제시한다.

## TL;DR (요약)
- 기존의 이진·삼진 분류 방식은 LLM(대형 언어 모델) 활용 양태를 세밀히 구분하지 못해 정책 적용에 한계가 있다.  
- 본 연구는 순수 인간, 순수 LLM, 인간 작성 후 LLM이 편집한 텍스트, LLM 작성 후 인간이 편집한 텍스트 등 네 가지 클래스를 엄격히 구분한다.  
- 제안 기법 RACE는 수사 구조 이론(Rhetorical Structure Theory) 기반의 논리 그래프와 담화 단위(EDU: Elementary Discourse Unit) 특징을 활용해 생성자와 편집자의 서명(Signature)을 분석한다.  
- 12개의 기존 기법을 상회하는 성능과 낮은 오탐율을 보이며, LLM 규제 및 콘텐츠 정책 집행에 실질적 도움을 준다.

## 문제 정의(Problem)
- LLM 생성 텍스트 검출 분야는 전통적으로 인간/LLM 텍스트 이분법(Binary) 또는 세분화(Ternary) 분류를 다뤄왔다.  
- 그러나 LLM이 인간 텍스트를 다듬거나, 인간이 LLM 텍스트를 후가공한 경우 등 협업 형태가 증가하며, 각 양태마다 정책 대응이 달라야 하는 실정이다.  
- 본 연구는 네 가지 클래스(순수 인간, 순수 LLM, 인간작성+LLM편집, LLM작성+인간편집)를 엄격히 구분하는 Fine-Grained Detection 문제를 정의한다.

## 제안 방법(Method)
- RACE(Rhetorical Analysis for Creator-Editor Modeling)는 두 가지 관점으로 텍스트를 분석한다.  
  1. 생성자(Creator) 관점: 수사 구조 이론(Rhetorical Structure Theory, RST)을 통해 텍스트의 논리 관계를 그래프 형태로 모델링.  
  2. 편집자(Editor) 관점: Elementary Discourse Unit(EDU) 단위로 추출한 문장 수준 특징(어휘·구문·담화적 표시)을 활용.  
- 두 관점에서 얻은 특징을 결합해 네 가지 클래스에 대한 분류기를 학습한다.  
- 실험에는 12개의 기존 베이스라인과 비교 평가를 수행했으며, 특히 오탐(False Alarm)율을 낮추는 데 집중했다.

## 핵심 기여/차별점(Contributions)
- 생성자와 편집자 역할을 분리해 분석하는 이중 모델링(Dual Roles Modeling) 프레임워크 제안  
- RST 기반 논리 그래프와 EDU 수준 담화 특징의 융합으로 Fine-Grained Detection 성능 향상  
- 네 가지 협업 형태를 엄격히 구분하는 분류 문제 설정 및 12개 베이스라인 대비 우수한 성능 검증

## 한계/리스크(Limitations)
- 평가 데이터셋의 규모와 도메인 커버리지가 다양하지 않을 수 있음(초록 기준으로는 확인 불가)  
- 모델 실시간 적용 시 RST 분석 등의 전처리 비용이 높을 가능성  
- 다국어 환경이나 다른 LLM 모델에 대한 일반화 성능은 초록에서 확인 불가

## 실무 적용 아이디어(Practical Takeaways)
- 콘텐츠 정책 엔진에 RACE 기반 모듈을 추가해 LLM 협업 양태별 맞춤 조치 자동화  
- 문서 생성 파이프라인에 RST 분석을 연계, 인간 작성문 보정 여부를 실시간 모니터링  
- 보안 감사 로그에 편집자·생성자 분석 결과를 함께 기록해 내부 위·변조 탐지 강화

## 메타 정보
- 저자: Yang Li, Qiang Sheng, Zhengjia Wang, Yehan Yang, Danding Wang, Juan Cao  
- 발행일: 확인 불가 (arXiv preprint v1)  
- 카테고리: 확인 불가 (arXiv 기준)

## 참고 링크
[https://arxiv.org/abs/2604.04932v1](https://arxiv.org/abs/2604.04932v1)
