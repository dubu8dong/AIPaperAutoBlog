# 소형 확산 LLM 교차 증류
**부제:** Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models

## 한 줄 결론
TIDE는 확산형 대형 언어 모델의 서로 다른 아키텍처 간 교차 증류를 최초로 제안하여, 0.6B 모델에서도 성능 향상을 입증한다.

## TL;DR (요약)
- 확산 대형 언어 모델(dLLM)은 병렬 디코딩과 양방향 문맥이 가능하지만 대규모 매개변수가 필요하다.  
- 기존 증류 방법은 동일 아키텍처 내에서만 동작하며, 교차-아키텍처 전이는 다루지 못한다.  
- TIDE 프레임워크는 TIDAL, CompDemo, Reverse CALM 세 모듈로 구성된 최초의 교차 아키텍처 dLLM 증류 기법이다.  
- 8B/16B 교사 모델을 0.6B 학생 모델로 증류 시 AR 기본 모델 대비 평균 1.53점 향상, 코딩 평가 HumanEval 48.78점 획득.

## 문제 정의(Problem)
확산형 대형 언어 모델(dLLM)은 생성 품질을 유지하면서도 병렬 디코딩과 양방향 문맥 활용이 가능한 장점이 있다. 그러나 최첨단 dLLM은 경쟁 성능을 위해 수십억 개의 매개변수를 요구하며, 이는 실제 서비스 환경에서의 비용과 지연으로 이어진다. 모델 증류(distillation) 기법은 학생 모델에 교사 모델의 지식을 이전하여 학습 속도나 추론 효율을 개선하지만, 기존 연구는 동일 아키텍처 내의 증류만을 다루며 아키텍처, 어텐션 메커니즘, 토크나이저가 다른 교사-학생 모델 간에는 적용되지 않는다.

## 제안 방법(Method)
논문에서는 TIDE라는 교차 아키텍처 dLLM 증류 프레임워크를 제시한다.  
1. TIDAL: 학습 진행도(training progress)와 확산 시점(diffusion timestep)에 따라 증류 강도를 조정하여 교사 모델의 노이즈 의존 신뢰도를 반영한다.  
2. CompDemo: 보완적 마스킹(complementary mask splitting)을 통해 교사 모델의 문맥을 풍부히 하여 강한 마스킹 하에서도 예측 성능을 향상시킨다.  
3. Reverse CALM: 청크(chunk) 단위 가능도 정합(likelihood matching)을 역전시킨 교차 토크나이저 목표 함수를 사용해 경계가 있는 그래디언트를 유지하고, 양쪽 끝 노이즈를 필터링한다.  
이 세 모듈을 결합해, 8B 파라미터의 dense 모델 및 16B 파라미터의 MoE(혼합 전문가) 모델 두 가지 교사로부터 0.6B 파라미터 학생 모델로 증류를 수행한다.

## 핵심 기여/차별점(Contributions)
- 최초의 교차 아키텍처 확산형 LLM 증류 프레임워크 TIDE 제안  
- TIDAL, CompDemo, Reverse CALM 세 모듈로 노이즈 의존 신뢰도, 강화된 마스킹 문맥, 토크나이저 차이 대응  
- 8B/16B 교사 모델 증류 시 0.6B 학생 모델이 여러 벤치마크에서 평균 1.53점, 코딩 생성(HumanEval)에서 대폭 향상 성능 확인  

## 한계/리스크(Limitations)
- 초록 기준으로는 실험에 사용된 모델 구성 외 추가 아키텍처나 토크나이저 간 일반화 여부를 확인할 수 없다.  
- 계산 비용 및 학습 시간, 대규모 데이터 요구량 등의 실용적 리소스 측면은 미제공돼 리스크 평가가 불가하다.  
- 평가가 8개 벤치마크에 국한되어 있으며, 다양한 도메인으로의 확장성은 초록 상으로 확인 불가하다.  

## 실무 적용 아이디어(Practical Takeaways)
- dLLM 기반 시스템에서 모델 경량화 시 교차 아키텍처 증류를 고려하여 추론 비용 절감 가능  
- TIDAL의 동적 증류 강도 조절을 통해 노이즈 의존 학습 안정화 전략 마련  
- CompDemo 및 Reverse CALM 모듈을 토크나이저 변경이나 마스킹 강도 조절 등 다양한 증류 작업에 활용  

## 메타 정보
- Authors: Gongbo Zhang, Wen Wang, Ye Tian, Li Yuan  
- Publication date: 2026년 4월 (arXiv v1)  
- Category: arXiv preprint  

## 참고 링크
[https://arxiv.org/abs/2604.26951v1](https://arxiv.org/abs/2604.26951v1)
