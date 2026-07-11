# 실세계 적극형 에이전트 평가
**부제:** UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks

## 한 줄 결론
UniClawBench는 5가지 핵심 능력 기반으로 실세계 동적 환경에서 적극형 에이전트를 라이브 Docker 컨테이너로 평가하는 최초의 벤치마크다.

## TL;DR (요약)
- 기존 벤치마크는 모의 환경과 단일 턴 평가에 의존해 실제 응용에서 문제 원인을 분석하기 어렵다.  
- UniClawBench는 Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, Cross-Platform Coordination의 5가지 능력을 중심으로 400개의 이중언어 과제를 설계했다.  
- 라이브 Docker 컨테이너와 단계별 Completion 체크포인트를 통한 fine-grained 평가 방식을 도입해 동적 실행 환경에서 성능을 측정한다.  
- Executor, Hidden Supervisor, User Agent로 구성된 폐쇄형 루프 평가 전략으로 다중 턴 인간 피드백을 모사한다.  

## 문제 정의(Problem)
최근 대형 언어 모델(LLM)과 멀티모달 대형 언어 모델(MLLM)의 발전으로 일상 도구를 작동하고 사용자를 지원하는 적극형(프록시브) 에이전트가 활발히 연구되고 있다. 그러나 기존 벤치마크는 주로 샌드박스 환경에서 단일 턴 평가를 수행하며, 시나리오 기반 과제 카테고리가 여러 능력을 혼합해 에이전트 실패 원인을 분리하기 어렵다는 한계를 가진다. 이러한 평가 방식은 실제 동적 환경에서 에이전트의 상호작용과 문제 해결 과정을 제대로 측정하지 못하며, 여러 모델 능력의 기여도를 명확히 파악하기 어려워 연구와 실무 적용에서 제약을 초래한다.

## 제안 방법(Method)
UniClawBench는 실제 운영 환경을 모사하기 위해 다음과 같은 구조로 벤치마크를 설계했다.
- 5가지 기본 모델 능력 중심: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, Cross-Platform Coordination  
- 각 능력별로 400개의 이중언어(영어·중국어) 실세계 과제를 제작해 다양한 도메인을 포괄  
- 과제 수행을 위해 라이브 Docker 컨테이너 상에서 에이전트를 실행하고, 각 단계별 Completion 체크포인트를 통해 세밀한 진행 상황을 평가  
- 폐쇄형 루프 평가 전략: Executor 에이전트, Hidden Supervisor 에이전트, User 에이전트를 구성해 다중 턴으로 인간 피드백을 시뮬레이션하되, 평가 기준은 비공개로 유지해 오염을 방지  
- 다양한 최신 언어 모델과 멀티모달 모델을 서로 다른 에이전트 프레임워크(플러그인 기반, 프롬프트 기반 등)와 결합해 능력 분리를 시도하고, 모델 성능과 프레임워크 설계의 상호효과를 분석  

## 핵심 기여/차별점(Contributions)
- 적극형 에이전트를 실제 동적 환경에서 평가하기 위한 최초의 능력 중심 범용 벤치마크 제안  
- 라이브 Docker 컨테이너 기반 세분화된 단계별 체크포인트 평가로 과제 수행 과정을 정밀하게 측정  
- Executor, Supervisor, User로 구성된 폐쇄형 루프 평가 전략을 통해 다중 턴 인간 피드백을 현실감 있게 시뮬레이션  

## 한계/리스크(Limitations)
- 초록 기준으로는 벤치마크의 과제 다양성 및 실제 운영 환경과의 격차, 평가 자동화의 정확도 등에 대한 구체적인 검증 결과를 확인할 수 없다.

## 실무 적용 아이디어(Practical Takeaways)
- 도구 기반 에이전트 평가 시 모의 환경 대신 컨테이너 기반 라이브 수행 방식을 도입해 실제 운영 조건을 모사해 볼 것  
- 모델 능력별 모듈화를 통해 문제 원인 분석이 가능하도록 과제 디자인 및 평가 체크포인트를 구성할 것  
- 사용자와 감독자 역할을 분리한 폐쇄 루프 평가 전략을 적용해 다중 턴 상호작용 품질을 정량적으로 측정할 것  

## 메타 정보
- 저자: Zhekai Chen, Chengqi Duan, Kaiyue Sun, Bohao Li, Yuqing Wang, Manyuan Zhang, Xihui Liu  
- 발표일: 2026-07 (arXiv v1 기준)  
- 카테고리: arXiv preprint  

## 참고 링크
[https://arxiv.org/abs/2607.08768v1](https://arxiv.org/abs/2607.08768v1)
