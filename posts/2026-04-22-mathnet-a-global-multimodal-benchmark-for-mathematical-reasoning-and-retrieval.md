# 글로벌 수학 추론·검색 벤치마크

**부제:** MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval

## 한 줄 결론
MathNet은 올림피아드 수준의 대규모 다국어·멀티모달 수학 문제 데이터셋과 최초의 수학 문제 검색 벤치마크를 함께 제공한다.

## TL;DR (요약)
- MathNet은 47개국, 17개 언어, 30,676개의 전문가 작성 올림피아드급 수학 문제(문제 및 해설 포함)로 구성된 대규모 데이터셋이다.  
- 세 가지 과제(문제 풀이, 수학 인지 검색, 검색 보강 문제 풀이)를 정의해 생성 모델 및 임베딩 기반 검색 모델 성능을 평가한다.  
- 최신 생성 모델은 78.4%(Gemini-3.1-Pro) 및 69.3%(GPT-5) 정확도로 여전히 도전 과제로 남아 있으며, 임베딩 모델은 동치 문제 검색에서 낮은 성능을 보인다.  
- 검색 보강 생성(Retrieval-Augmented Generation)은 검색 품질에 민감하며, DeepSeek-V3.2-Speciale로 최대 12% 성능 향상을 확인했다.  

## 문제 정의(Problem)
기존 수학 추론 벤치마크는 데이터 규모, 언어 커버리지, 과제 다양성 측면에서 제약이 크며, 수학 문제 검색 평가 기준이 부재하다. 수학 문제 해결 능력을 포괄적으로 평가하고, 구조적 및 수학적 동치 문제 검색을 위한 표준화된 벤치마크가 필요하다.

## 제안 방법(Method)
MathNet은 다음 요소로 구성된다.
- 47개국 및 17개 언어로 진행된 수학 올림피아드 대회(지난 20년)에서 수집한 30,676개의 문제와 해설.  
- 전문가가 큐레이션한 수학적 동치 및 구조적으로 유사한 문제 쌍으로 구성된 검색 벤치마크.  
- 세 가지 평가 과제(Task) 정의:  
  1. Problem Solving: 생성 모델의 수학 문제 풀이 성능 평가  
  2. Math-Aware Retrieval: 임베딩 기반 검색 모델의 동치 문제 검색 성능 평가  
  3. Retrieval-Augmented Problem Solving: 검색 결과를 활용한 생성 모델의 성능 평가  

## 핵심 기여/차별점(Contributions)
- 대규모(30,676문제), 다국어(17개 언어), 멀티모달(텍스트·수식 이미지) 올림피아드급 수학 문제 데이터셋 공개  
- 수학 문제의 동치·유사 문제 검색을 위한 최초의 인간 전문가 큐레이션 기반 검색 벤치마크 제공  
- 생성 모델과 검색 모델을 통합 평가하는 Retrieval-Augmented Generation 과제 및 검색 품질의 영향 분석  

## 한계/리스크(Limitations)
- 데이터셋이 올림피아드 수준 문제에 한정되어 있어, 중·저등급 수학 문제나 실무 수학 응용 과제로의 일반화 여부는 초록 기준으로는 확인 불가  
- Retrieval-Augmented Generation 성능이 검색 결과 품질에 크게 의존하며, 고품질 검색 시스템 구축에 필요한 비용 및 인프라 요구사항은 초록에서 확인 불가  

## 실무 적용 아이디어(Practical Takeaways)
- 대규모 수학 추론 모델 성능 비교를 위해 MathNet 문제를 테스트셋으로 활용할 수 있다.  
- 수학적 동치 검색 엔진 개발 시 MathNet 검색 벤치마크를 활용해 알고리즘 성능을 객관적으로 평가 가능하다.  
- Retrieval-Augmented Generation 파이프라인 설계 시 검색 품질 관리(인덱싱, 임베딩, 부트스트랩 전략)가 전체 성능에 미치는 영향을 고려해야 한다.  

## 메타 정보
- 저자: Shaden Alshammari, Kevin Wen, Abrar Zainal, Mark Hamilton, Navid Safaei, Sultan Albarakati, William T. Freeman, Antonio Torralba  
- 발행일: 2026년 4월 (arXiv v1)  
- 카테고리: Multimodal AI, Mathematical Reasoning, Information Retrieval  

## 참고 링크
[https://arxiv.org/abs/2604.18584v1](https://arxiv.org/abs/2604.18584v1)
