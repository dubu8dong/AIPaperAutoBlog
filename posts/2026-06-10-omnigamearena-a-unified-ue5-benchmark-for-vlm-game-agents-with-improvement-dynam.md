# 통합 UE5 VLM 게임 벤치

**부제:** OmniGameArena: A Unified UE5 Benchmark for VLM Game Agents with Improvement Dynamics

## 한 줄 결론
OmniGameArena는 UE5 기반 게임 환경에서 다양한 비전-언어 모델(VLM) 에이전트를 통합 평가하고, 개선 역학 곡선을 통해 성과 향상을 체계적으로 추적하는 벤치마크 프레임워크다.

## TL;DR (요약)
- 12개의 UE5 게임으로 Solo, PvP, Coop 환경을 구성하고 통합된 행동 인터페이스를 제공  
- 개선 역학 곡선(Improvement Dynamics Curve, IDC)을 활용해 에이전트 성과 변화를 라운드별로 관찰  
- IDC는 도구 활용 리플렉터 대형 언어 모델(LLM)이 자율적으로 스킬 프롬프트를 다중 라운드에서 개선  
- 12개 VLM 에이전트의 콜드스타트 초기 성과와 4개 상위 에이전트의 성과 향상 다이내믹스를 보고  

## 문제 정의(Problem)
- 기존 VLM(비전-언어 모델) 기반 게임 벤치마크는 (에이전트, 게임) 조합마다 단일 초기 점수만 보고  
- 주로 단일 에이전트의 Solo 플레이에 집중하며 PvP 또는 협동(Cooperative) 환경은 부족  
- 상용 VLM, 오픈소스 VLM, 특화 게임 정책 등 이질적 에이전트 클래스 간 비교를 위한 통일된 프로토콜 부재  

## 제안 방법(Method)
- Unreal Engine 5(UE5)로 새로 개발한 12개 게임: Solo 7개, PvP 3개, Coop 2개 환경 구축  
- 모든 게임에 통일된 행동(action) 인터페이스(api) 제공으로 에이전트 간 공정 비교 지원  
- Improvement Dynamics Curve(IDC):  
  - 도구 사용(tool-using) 리플렉터 LLM이 bounded skill prompt를 자율 반영(reflection)하며 다중 라운드 개선  
  - 콜드스타트 점수 외에 라운드별 점수 변화와 학습된 스킬의 파생(held-out) 과제 성능 관찰 지표 추가  
- 12개 VLM 에이전트를 콜드스타트 리더보드에 올리고, 상위 4개 에이전트에 IDC 적용 결과 보고  

## 핵심 기여/차별점(Contributions)
- UE5 기반 Solo/PvP/Coop 환경을 포함하는 12개 게임으로 구성된 단일 벤치마크 프레임워크 제공  
- Improvement Dynamics Curve(IDC) 제안: 에이전트 자기 반영을 통한 스킬 프롬프트 자율 개선 메커니즘  
- 상용 VLM, 오픈소스 VLM, 특화 게임 정책 등 이질적 에이전트 클래스에 대한 통일된 평가 프로토콜 확립  

## 한계/리스크(Limitations)
- 12개 게임 모두 Unreal Engine 5 기반으로, 타 게임 엔진이나 실제 서비스 환경 일반화 미확인  
- IDC 적용 결과는 4개 상위 에이전트에 한정 보고되었으며, 전체 에이전트 성능 향상 범위 파악 불충분  
- 복잡한 협동 및 PvP 전략 요소 분석을 위한 세부 메트릭이나 추가 사회적·윤리적 리스크는 초록 기준으로는 확인 불가  

## 실무 적용 아이디어(Practical Takeaways)
- 신규 VLM 게임 에이전트 개발 시 OmniGameArena로 초기(콜드스타트) 및 self-improvement 평가 파이프라인 구축  
- IDC의 리플렉터 LLM 기반 프롬프트 개선 루프를 채택해 에이전트 학습 자동화 및 반복적 최적화  
- Solo, PvP, Coop 유형별 통일 인터페이스 덕분에 개발·테스트 CI/CD 파이프라인에 벤치마크 통합이 용이  

## 메타 정보
- 저자: Mingxian Lin, Shengju Qian, Yuqi Liu, Yi-Hua Huang, Yiyu Wang, Wei Huang, Yitang Li, Fan Zhang, Zeyu Hu, Lingting Zhu, Xin Wang, Xiaojuan Qi  
- 발행일: 확인 불가 (arXiv 제출일 미제공)  
- 카테고리: 벤치마크, 비전-언어 모델, 게임 AI  

## 참고 링크
[https://arxiv.org/abs/2606.09826v1](https://arxiv.org/abs/2606.09826v1)
