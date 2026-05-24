# 볼록 최적화 기반 토크나이저
**부제:** Tokenisation via Convex Relaxations

## 한 줄 결론
ConvexTok은 토크나이저 설계를 선형 계획(Linear Programming)으로 풀어 언어 모델의 bits-per-byte를 개선하고 최적성 보증을 제공한다.

## TL;DR (요약)
- 기존 BPE(Byte-Pair Encoding)와 Unigram 알고리즘은 어휘 구성에서 지역 최적화만 수행하는 탐욕적(Greedy) 방식이다.
- ConvexTok은 토크나이저 구축을 선형 계획 문제로 공식화하고 볼록 최적화(Convex Optimization) 기법으로 해결한다.
- Intrinsic 토크나이징 지표와 언어 모델의 bits-per-byte(BpB)를 일관되게 개선한다.
- 최적에서 얼마나 벗어났는지 하한(lower bound)으로 인증(certify)할 수 있으며, 공통 어휘 크기에서 1% 이내의 최적성을 보인다.

## 문제 정의(Problem)
자연어 처리(NLP) 파이프라인에서 토크나이제이션(Tokenisation)은 필수 단계다. 흔히 사용되는 BPE(Byte-Pair Encoding)나 Unigram 토크나이저는 탐욕적 알고리즘으로, 토큰을 생성할 때局部局所(local) 최적 선택에만 집중해 어휘 집합 전체에 대한 최적성은 보장하지 못한다. 이로 인해 언어 모델의 압축 효율(예: bits-per-byte)과 downstream 태스크 성능이 잠재적으로 최적보다 떨어질 수 있다.

## 제안 방법(Method)
논문은 토크나이저 구축을 선형 계획(linear program)으로 모델링하고, 이를 풀기 위해 볼록 최적화 도구를 활용한다.  
1. 어휘 집합과 토큰화 규칙을 결정 변수로 정의.  
2. 토큰화 비용( 예: 인코딩 비트 수) 및 제약 조건을 선형 제약으로 표현.  
3. 기존 탐욕적 방법 대신 Convex Optimization Solver를 이용해 전역 최적화 문제(global optimization problem)를 해결.  
4. ConvexTok이라 명명된 알고리즘을 통해 최적화된 어휘를 도출.

## 핵심 기여/차별점(Contributions)
- 토크나이저 설계를 탐욕적 알고리즘이 아닌 선형 계획 문제로 공식화  
- Convex Optimization을 적용한 새로운 토크나이저 ConvexTok 제안  
- 어휘 크기에 따른 최적성 하한(lower bound)을 제공해 최적화 정도를 인증(certify) 가능

## 한계/리스크(Limitations)
- ConvexTok은 intrinsic(metric) 관점에서 일관된 개선을 보이나, downstream 태스크 성능 향상은 덜 일관적임  
- 초록 기준으로는 계산 비용(computational cost)이나 대규모 적용 시 효율성에 대한 정보는 확인 불가

## 실무 적용 아이디어(Practical Takeaways)
- 언어 모델 사전 구축 단계에서 BPE/Unigram 대신 ConvexTok을 도입해 bits-per-byte 개선을 노려볼 것  
- 제공된 하한(lower bound)을 참고해 원하는 어휘 크기에서 최적성 보증을 확인하며 설정값을 조정  
- 다운스트림 태스크별 성능 변화를 모니터링하여 실제 효과를 검증하고 도입 여부를 판단  

## 메타 정보
- 저자: Jan Tempus, Philip Whittington, Craig W. Schmidt, Dennis Komm, Tiago Pimentel  
- 발표일: 2026년 5월 (arXiv v1 기준)  
- 카테고리: Computation and Language (cs.CL)

## 참고 링크
[https://arxiv.org/abs/2605.22821v1](https://arxiv.org/abs/2605.22821v1)
