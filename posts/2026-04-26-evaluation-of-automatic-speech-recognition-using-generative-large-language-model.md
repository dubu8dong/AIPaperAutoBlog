# ASR 평가, WER 넘어 LLM으로  
**부제:** Evaluation of Automatic Speech Recognition Using Generative Large Language Models

## 한 줄 결론
생성형 대형언어모델을 활용한 ASR 평가는 기존 WER 대비 인간 평가자와의 의미론적 일치도가 크게 향상된다.

## TL;DR (요약)
- 전통적인 ASR(Automatic Speech Recognition, 자동 음성 인식) 평가는 단어 오류율(Word Error Rate, WER)에 의존해 의미론적 민감도가 낮음.  
- Embedding 기반 의미 평가가 제안되었으나, 디코더 기반 대형언어모델(LLM: Large Language Model)은 충분히 탐구되지 않음.  
- 본 논문은 LLM을 활용해 (1) 가설 선택, (2) 생성 임베딩 거리 측정, (3) 오류 분류 방식 세 가지 평가법을 제안.  
- HATS 데이터셋에서 LLM은 92–94%의 인간 평가자 일치도를 기록해, WER(63%)와 기존 의미 메트릭을 모두 능가함.  

## 문제 정의(Problem)
기존 ASR 평가는 단어 오류율(WER)에 의존하나, 이는 문장 내 의미 변화에 둔감해 인간 평가자와의 일치도가 낮다. 의미 기반 평가를 위해 임베딩 기반 메트릭이 도입되었으나, 생성 능력을 갖춘 디코더 기반 대형언어모델의 활용 가능성은 충분히 검증되지 않았다.

## 제안 방법(Method)
본 연구에서는 디코더 기반 LLM을 ASR 평가 지표로 활용하기 위해 다음 세 가지 접근을 실험했다.
1. 가설 선택(Hypothesis Selection): 두 개의 ASR 출력 후보 중 더 나은 문장을 LLM을 통해 판별.  
2. 생성 임베딩 거리(Generative Embedding Distance): LLM의 내부 생성 임베딩을 활용해 원문과 후보 출력 간 의미적 거리를 계산.  
3. 오류 분류(Qualitative Error Classification): LLM 기반 분류를 통해 ASR 오류 유형을 해석 가능하게 제시.  
평가는 HATS 데이터셋을 대상으로 수행되었으며, WER 및 기존 임베딩 기반 메트릭과 비교했다.

## 핵심 기여/차별점(Contributions)
- LLM을 활용한 ASR 가설 선택 방식을 제안해 92–94%의 인간 평가자 일치도를 실증  
- 생성형 임베딩 기반 의미 거리 측정이 엔코더 모델과 유사한 성능을 보임을 확인  
- 오류 분류를 통해 해석 가능하고 의미론적 일관성을 확보한 ASR 평가 프레임워크 제시  

## 한계/리스크(Limitations)
- 평가가 HATS 데이터셋에 한정되어 있어 다른 데이터셋·도메인 적용성은 초록 기준으로는 확인 불가  
- LLM 운용에 따른 계산 비용 및 실시간 처리 가능성에 대한 언급은 없음  
- 다양한 언어 및 방언에 대한 성능 일반화 여부는 초록 기준으로는 확인 불가  

## 실무 적용 아이디어(Practical Takeaways)
- ASR 시스템 비교 평가 시 WER 외에 LLM 기반 가설 선택 방식을 병행 도입해 의미적 정확도 검증  
- 생성형 LLM의 임베딩 추출 기능을 기존 평가 파이프라인에 통합해 자동화된 의미론적 품질 지표 구축  
- 디코더 기반 LLM과 엔코더 기반 모델의 성능·비용 균형을 고려해 평가 메트릭 도입 전략 수립  

## 메타 정보
- 저자: Thibault Bañeras-Roux, Shashi Kumar, Driss Khalil, Sergio Burdisso, Petr Motlicek, Shiran Liu, Mickael Rouvier, Jane Wottawa, Richard Dufour  
- 발행일: 2026-04 (arXiv v1 기준)  
- 카테고리: 초록 기준으로는 확인 불가  

## 참고 링크
[https://arxiv.org/abs/2604.21928v1](https://arxiv.org/abs/2604.21928v1)
