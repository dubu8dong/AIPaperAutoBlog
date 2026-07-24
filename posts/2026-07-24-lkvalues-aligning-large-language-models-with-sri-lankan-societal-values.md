# 스리랑카 사회가치 LLM 정렬
**부제:** LKValues: Aligning Large Language Models with Sri Lankan Societal Values

## 한 줄 결론
스리랑카 고유의 사회적 가치에 기반한 데이터셋과 벤치마크를 통해 다국어 대형언어모델(LLM)의 문화적 편향을 완화하고 가치 정렬을 개선할 수 있음을 보였다.

## TL;DR (요약)
- 서구 중심 값에 치우친 기존 LLM이 스리랑카 현지 가치에 부합하지 않아 실용적 한계를 드러냈다.  
- 205명 응답자를 대상으로 삼개 언어 설문을 수행해 40개 사회적 가치를 도출하고, 150k 지침-시나리오 코퍼스(LKvaluesIT)와 1,000문항 평가 벤치마크(LKvaluesBench)를 구축했다.  
- 다양한 상용·오픈소스 LLM을 평가하고, Qwen 계열·Aya-Expanse 모델을 파인튜닝해 스리랑카 가치 반영 성능 향상을 확인했다.  
- 모델 크기와 최신성에도 불구하고 여전히 저자원 언어 및 문화적 정렬 격차가 존재하며, 미세조정 효과는 모델 패밀리별로 다르게 나타났다.

## 문제 정의(Problem)
대형언어모델(LLM)은 가치 정렬(value alignment) 과정에서 주로 서구권 기준을 반영하도록 설계되었기 때문에, 스리랑카처럼 고유의 문화·사회적 맥락이 중요한 다언어·다문화 사회에서는 현지 가치를 적절히 다루지 못한다. 특히 시넬하어(Sinhala) 등 공식 언어에 대한 벤치마크와 데이터셋이 없어, 문화적으로 민감한 평가 및 파인튜닝이 불가능한 상황이다.

## 제안 방법(Method)
저자들은 스리랑카 사회의 고유 가치를 반영하기 위해 세 가지 단계를 제안했다.  
1. 삼개 언어(영어·시넬하어·타밀어) 설문조사를 통해 205명의 응답자 의견을 수집하고, 기존 글로벌 프레임워크와 LLM 유도(local constructs)를 융합해 40개의 다수 지지 가치(majority-endorsed values)를 도출했다.  
2. 이 가치를 바탕으로 영어·시넬하어 뉴스 텍스트에서 시나리오 기반 지침-응답 쌍 150,000개로 구성된 LKvaluesIT 데이터셋을 생성했다.  
3. 1,000개 문항으로 구성된 평가용 벤치마크 LKvaluesBench를 구축하고, 상용 및 오픈소스 LLM의 현지 가치 정렬 성능을 측정했다. 또한 Qwen3.5-4B-Base·Qwen3.5-9B-Base·Aya-Expanse-8B-Base 세 모델을 미세조정하여 개선 효과를 분석했다.

## 핵심 기여/차별점(Contributions)
- 스리랑카 사회적 가치에 특화된 첫 서베이 기반 리소스 스위트(LKValues) 제안  
- 150k 규모 다국어 지침-시나리오 코퍼스(LKvaluesIT) 및 1,000문항 평가 벤치마크(LKvaluesBench) 공개  
- 다양한 LLM 평가 및 오픈소스 모델 파인튜닝을 통한 현지 가치 정렬 개선 가능성 입증

## 한계/리스크(Limitations)
- 설문 응답자(205명)의 표본이 전체 스리랑카 인구를 대표하는지 여부는 초록 기준으로는 확인 불가  
- 파인튜닝 성능 향상 폭이 모델 패밀리에 따라 상이해, 일관된 개선을 보장하기 어려움  
- 시넬하어·영어 중심이며 타밀어 분량 및 질에 대한 세부 정보는 초록 기준으로는 확인 불가

## 실무 적용 아이디어(Practical Takeaways)
- 다국어 서비스에 LLM을 도입할 때, 현지 문화·사회적 가치 반영을 위해 유사한 가치 설문 기반 데이터 구축을 고려  
- 파인튜닝 시 국가·언어별 맞춤 지침-시나리오 코퍼스를 활용해 가치 편향을 줄이고 응답의 타당성을 높일 수 있음  
- 배포 전 LKvaluesBench와 유사한 평가용 벤치마크로 문화적 민감도를 검증하여 리스크를 사전 제거

## 메타 정보
- 저자: Nethmi Muthugala, Supryadi, Surangika Ranathunga, Nisansa de Silva, Ruijie Tao, Ovindu Gunatunga, Pengyun Zhu, Shaowei Zhang, Jingting Zheng, Deyi Xiong  
- 발행일: 2026년 7월 (arXiv preprint 기준)  
- 카테고리: 가치 정렬(Value Alignment), 자연어처리(NLP)

## 참고 링크
[https://arxiv.org/abs/2607.20410v1](https://arxiv.org/abs/2607.20410v1)
