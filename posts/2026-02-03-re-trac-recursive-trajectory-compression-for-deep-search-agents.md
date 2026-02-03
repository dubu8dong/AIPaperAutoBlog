# 반복 궤적 압축으로 탐색 효율화

**부제:** RE-TRAC: REcursive TRAjectory Compression for Deep Search Agents

## 한 줄 결론
Re-TRAC은 각 궤적 후 구조화된 상태 표현을 기반으로 반복적 반영과 전역 계획을 수행해 ReAct 대비 15–20% 성능 향상과 탐색 효율화를 달성한다.

## TL;DR (요약)
- Re-TRAC은 ReAct 프레임워크의 선형적 한계를 보완하기 위해 고안된 에이전트 구조다.
- 각 탐색 궤적 이후 증거, 불확실성, 실패, 향후 계획을 요약하는 구조화된 상태 표현(State Representation)을 생성한다.
- 이를 바탕으로 후속 궤적을 전역적으로 계획하여 반복적 성찰(Reflective Planning)을 수행한다.
- 실험에서 ReAct 대비 BrowseComp 벤치마크에서 15–20% 성능 향상을 보였으며, 도구 호출과 토큰 사용량은 점진적으로 감소했다.

## 문제 정의(Problem)
대형 언어 모델(Large Language Model, LLM) 기반 딥 리서치 에이전트는 주로 ReAct(Reasoning and Acting) 프레임워크를 따른 선형적 설계를 사용한다. 이 방식은
- 이전 상태로의 복귀가 어려워 신규 분기(branch) 탐색이 제한되고  
- 긴 컨텍스트에서 전역(global) 인식이 부족해  
- 지역 최적(local optimum)에 머무르거나 중복 탐색이 발생해  
탐색 효율이 떨어지는 문제가 있다.

## 제안 방법(Method)
Re-TRAC(REcursive TRAjectory Compression)는 교차 궤적 탐색(cross-trajectory exploration)을 지원하는 에이전트 프레임워크다.
- 각 탐색 궤적(run) 종료 시 증거, 불확실성, 실패 요인, 향후 계획을 포함한 구조화된 상태 표현(state representation)을 생성  
- 후속 궤적은 이 상태 표현을 입력으로 받아 전역 관점에서 계획을 재수립  
- 반복적 성찰(iterative reflection)을 통해 점진적으로 목표에 수렴하는 탐색 경로를 모색  
- 대형 모델 외에도 소규모 모델을 대상으로 Re-TRAC-aware 감독 학습(supervised fine-tuning) 기법을 도입  

## 핵심 기여/차별점(Contributions)
- 교차 궤적 탐색을 위한 구조화된 상태 표현(State Representation) 개념 제안  
- 상태 표현 기반 반복적 반영(Reflective Planning)을 통한 전역 탐색 전략 수립  
- 대형 모델에서 BrowseComp 벤치마크 15–20% 성능 향상 및 도구 호출·토큰 사용량 감소, 소형 모델 감독 학습 기법 제시  

## 한계/리스크(Limitations)
- 메모리 및 계산 오버헤드: 각 궤적 후 상태 표현 생성과 활용에 따른 추가 비용은 초록에서 확인 불가  
- 일반화 가능성: BrowseComp 외 다른 벤치마크나 실제 복잡 환경에서의 성능은 초록 기준으로는 확인 불가  
- 소형 모델용 Re-TRAC-aware 감독 학습의 세부 구현 및 효과는 초록에서 구체적으로 확인 불가  

## 실무 적용 아이디어(Practical Takeaways)
- LLM 기반 탐색 에이전트 설계 시 각 탐색 단계 후 상태 요약을 통해 전역 목표와 연관 지어 계획을 동적으로 재조정  
- 반복적 성찰 메커니즘을 도입해 도구 호출 횟수 및 토큰 사용량을 최적화  
- 자원 제약이 있는 소형 모델 환경에서는 감독 학습 기법으로 Re-TRAC 구조를 학습시켜 성능을 강화  

## 메타 정보
- 저자: Jialiang Zhu, Gongrui Zhang, Xiaolong Ma, Lin Xu, Miaosen Zhang, Ruiqi Yang, Song Wang, Kai Qiu, Zhirong Wu, Qi Dai, Ruichun Ma, Bei Liu, Yifan Yang, Chong Luo, Zhengyuan Yang, Linjie Li, Lijuan Wang, Weizhu Chen, Xin Geng, Baining Guo  
- 발표일: 2026-02  
- 카테고리: AI 에이전트, 탐색 알고리즘, 대형 언어 모델(LLM)  

## 참고 링크
[https://arxiv.org/abs/2602.02486v1](https://arxiv.org/abs/2602.02486v1)
