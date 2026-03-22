# FinTradeBench 금융추론평가

**부제:** FinTradeBench: A Financial Reasoning Benchmark for LLMs

## 한 줄 결론
FinTradeBench는 금융 기초정보와 거래 신호를 결합해 대형 언어 모델의 수치·시계열 추론 한계를 드러낸다.

## TL;DR (요약)
- FinTradeBench는 나스닥(NASDAQ-100) 상위 기업 10년치 데이터를 기반으로 1,400개 금융추론 문제를 제공한다.  
- 문제 유형은 기초재무(fundamentals-focused), 거래신호(trading-signal-focused), 하이브리드(cross-signal)로 구성된다.  
- 전문가 검증, 다중 모델 응답 생성, 셀프 필터링, 수치 감사, 인간-LLM 심사 정렬을 거친 신뢰성 확보 프레임워크를 제시한다.  
- 14종의 대형 언어 모델(LLM, Large Language Model)을 제로샷 및 검색 보강(retrieval-augmented) 환경에서 평가한 결과, 텍스트 기반 기초 추론은 개선되지만 거래신호 추론 능력에는 제한이 확인되었다.  

## 문제 정의(Problem)
실제 금융 의사결정은 기업의 재무제표와 가격 동향에서 파생된 거래 신호를 종합해 판단해야 하는 복합적 과제이다. 그러나 기존 금융 질의응답 벤치마크는 주로 기업의 대차대조표 등 정적 재무정보만 다루며, 주가 움직임을 포함한 시계열적 거래 신호나 이들 간 상호작용을 평가하지 못한다.  

## 제안 방법(Method)
FinTradeBench는 다음 요소로 구성된다.  
- 데이터셋: NASDAQ-100 기업을 대상으로 10년치 재무제표·거래 데이터에서 1,400개 문항 추출  
- 문제 유형:  
  1) 기초재무(fundamentals-focused)  
  2) 거래신호(trading-signal-focused)  
  3) 하이브리드(cross-signal reasoning)  
- 신뢰성 확보(캘리브레이션-스케일링) 프레임워크:  
  1) 전문가가 설계한 시드 질문  
  2) 다중 모델 응답 생성 후 내·외부 셀프 필터링  
  3) 수치 감사(numerical auditing)  
  4) 인간-LLM 간 심사 결과 정렬(alignment)  
- 평가: 14종 LLM에 제로샷(zero-shot) 및 검색 보강(retrieval-augmented) 프롬프트 적용  

## 핵심 기여/차별점(Contributions)
- 금융 기초재무 정보와 시계열 거래신호를 결합한 최초의 대규모 금융 추론 벤치마크  
- 전문가·LLM 셀프 필터링·수치 감사·인간-LLM 심사 정렬을 통합한 신뢰성 확보 파이프라인  
- 14개 LLM의 제로샷 및 검색 보강 결과를 비교·분석해 시계열 및 수치 추론의 난제를 강조  

## 한계/리스크(Limitations)
- 현 대형 언어 모델이 거래신호 중심 문항에서 제한된 성능을 보여 금융 시계열 분석 능력은 여전히 개선이 필요하다.  
- 벤치마크가 NASDAQ-100 기업에 한정돼 다른 시장·자산군 일반화 여부는 초록 기준으로는 확인 불가.  
- 경제적 비용, 모델 학습·추론 환경 등 인프라 측면 리스크는 초록 기준으로는 확인 불가.  

## 실무 적용 아이디어(Practical Takeaways)
- 투자 전략 자동화 시스템에 금융 기초정보뿐 아니라 거래신호 모듈을 별도 평가 체계로 통합해 성능 병목 요인 파악  
- 검색 보강(retrieval-augmented) 접근법을 통해 텍스트 기반 재무정보 추론은 개선하되, 시계열 신호는 별도 특화 모델 도입 고려  
- 캘리브레이션-스케일링 프레임워크를 참고해 자체 도메인 벤치마크 설계 시 전문가 검증과 수치 감사 단계를 포함  

## 메타 정보
- 저자: Yogesh Agrawal, Aniruddha Dutta, Md Mahadi Hasan, Santu Karmaker, Aritra Dutta  
- 발행일: 초록 기준으로는 확인 불가  
- 카테고리: 초록 기준으로는 확인 불가  

## 참고 링크
[https://arxiv.org/abs/2603.19225v1](https://arxiv.org/abs/2603.19225v1)
