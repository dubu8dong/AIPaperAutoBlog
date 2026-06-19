# 모달 이해를 위한 능동 비전 에이전트

**부제:** Native Active Perception as Reasoning for Omni-Modal Understanding

## 한 줄 결론
OmniAgent는 POMDP 기반 능동 지각을 통해 영상 이해 비용을 길이 독립적으로 최적화하며 개방형 모델 중 SOTA 성능을 달성한다.

## TL;DR (요약)
OmniAgent는 패시브 프레임 처리의 한계를 벗어나 영상 길이에 상관없이 필요할 때만 멀티모달 정보를 선택적으로 추출하는 능동적 인식 프레임워크다.  
에이전틱 감독 미세조정(Agentic Supervised Fine-Tuning)과 TAURA 기반 에이전틱 강화학습(Agentic Reinforcement Learning with Turn-aware Adaptive Uncertainty Rescaled Advantage)을 결합해 효과적인 추론 루프를 설계했다.  
추론 턴(turn)을 늘릴수록 성능이 향상되는 긍정적 테스트타임 스케일링을 확인했으며, 다수 벤치마크에서 개방형 모델 최고 성능을 기록했다.  

## 문제 정의(Problem)
- 기존 장기 영상 이해 모델은 모든 프레임을 균일하게 처리하는 “모두 보기(watch-it-all)” 패러다임을 따른다.  
- 영상 길이가 길어질수록 계산 비용이 선형으로 증가해 실시간 또는 대규모 처리에 비효율적이다.  
- 상호작용형(interactive) 프레임워크들은 사전 전체 스캔(global pre-scan)에 의존해 맥락 비용(context cost)이 여전히 영상 길이에 종속된다.  

## 제안 방법(Method)
OmniAgent는 부분 관찰 마르코프 결정 과정(Partially Observable Markov Decision Process, POMDP) 기반의 반복적 Observation-Thought-Action 사이클로 영상 이해를 재정의한다.
1. Observation: 온디맨드(on-demand) 오디오-비주얼 힌트를 선택적으로 획득  
2. Thought: 획득한 힌트를 텍스트 메모리로 축적하고 추론  
3. Action: 다음 관찰 동작 결정  

이를 위해 두 가지 방법을 도입했다.
- Agentic Supervised Fine-Tuning: best-of-N 궤적(trajectory) 합성을 통한 초기 능동 지각 부트스트래핑 및 이중 단계 품질 검증  
- Agentic Reinforcement Learning with TAURA(Turn-aware Adaptive Uncertainty Rescaled Advantage): 턴별(entropy) 불확실도 정보를 이용해 핵심 전환점(turn)에 보상을 집중  

## 핵심 기여/차별점(Contributions)
- 최초의 네이티브 능동 지각 기반 옴니-모달 에이전트 프레임워크 제안  
- 이중 단계 품질 제어를 갖춘 에이전틱 감독 미세조정 기법으로 초기 궤적 생성을 안정화  
- TAURA 전략을 활용한 에이전틱 강화학습으로 중요한 턴에 중점을 둔 효과적인 신용할당 실현  

## 한계/리스크(Limitations)
- 초록 기준으로는 모델 학습 시 요구되는 계산 자원, 수렴 속도 및 안정성 등 구체적 한계를 확인하기 어렵다.  
- 실제 환경에서 다양한 노이즈나 미리 정의되지 않은 인터랙션 방식에 대한 견고성 검증 정보는 부족하다.  

## 실무 적용 아이디어(Practical Takeaways)
- 영상 길이에 구애받지 않는 능동 샘플링 메커니즘을 통해 클라우드 기반 처리 비용을 크게 절감할 수 있다.  
- POMDP 기반 Observation-Thought-Action 루프를 적용해 멀티모달 AI 파이프라인의 유연성을 높일 수 있다.  
- 턴 수준의 불확실도 분석을 도입해 비디오 QA, 보안 모니터링 등 실시간 의사결정 시스템에 응용할 수 있다.  

## 메타 정보
- 저자: Zhenghao Xing, Ruiyang Xu, Yuxuan Wang 외  
- 발행일: 2026년 6월  
- 카테고리: 멀티모달 AI / 컴퓨터 비전  

## 참고 링크
[https://arxiv.org/abs/2606.19341v1](https://arxiv.org/abs/2606.19341v1)
