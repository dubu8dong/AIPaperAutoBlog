# 단계적 사고 흐름으로 확산 모델 강화

**부제:** EndoCoT: Scaling Endogenous Chain-of-Thought Reasoning in Diffusion Models

## 한 줄 결론
EndoCoT는 반복적 사고 정제와 최종 상태 정합을 통해 MLLM 기반 확산 모델에 단계적 추론을 부여해 평균 92.1% 정확도로 기존 대비 8.3% 포인트 성능 향상을 보였다.

## TL;DR (요약)
멀티모달 대형 언어 모델(MLLM, Multimodal Large Language Models)을 확산 프레임워크의 텍스트 인코더로 사용할 때, 단일 단계 인코딩으로는 충분한 사고 흐름이 활성화되지 않고, 디코딩 과정에서 가이드가 고정되어 복잡한 작업 분해가 어렵다.  
Endogenous Chain-of-Thought(EndoCoT)는 반복적 사고 정제 모듈과 최종 사고 상태 정합 모듈을 통해 은닉 사고 상태를 점진적으로 다듬어, DiT(Diffusion transformer)의 노이즈 제거 과정에 단계적 추론을 적용한다.  
Maze, TSP, VSP, Sudoku 벤치마크에서 평균 92.1% 정확도를 기록해 최강 베이스라인 대비 8.3% 포인트 성능 향상을 달성했다.

## 문제 정의(Problem)
멀티모달 대형 언어 모델(MLLM, Multimodal Large Language Models)을 확산 프레임워크에 텍스트 인코더로 통합할 때 다음 두 가지 문제가 발생한다:
- 사고 깊이 부족: 단일 단계 인코딩으로는 사고 흐름(Chain-of-Thought, CoT)을 활성화하지 못해, 복잡한 작업에 대한 정교한 지시를 생성하기 어렵다.
- 고정된 디코딩 가이드: 확산 트랜스포머(DiT, Diffusion transformer)는 디코딩 과정 중 가이드가 변하지 않아, 올바른 인코딩이 있어도 단계적으로 작업을 분해하며 노이즈 제거를 수행하기 힘들다.

## 제안 방법(Method)
Endogenous Chain-of-Thought(EndoCoT)는 위 문제를 해결하기 위해 두 가지 주요 모듈을 도입한다:
1. 반복적 사고 가이드(iterative thought guidance) 모듈  
   - MLLM의 은닉 사고(latent thought) 상태를 여러 차례 추론하며 정제해, 깊이 있는 Chain-of-Thought를 활성화한다.  
2. 최종 사고 정합(terminal thought grounding) 모듈  
   - 정제된 최종 은닉 사고 상태를 실제 정답(ground-truth)과 정합시켜, 사고 궤적이 텍스트 감독 하에 유지되도록 한다.  
이후 두 모듈을 거친 은닉 사고 상태를 DiT의 단계별 노이즈 제거 과정에 가이드로 투입해, 복잡한 지시를 순차적으로 실행한다.

## 핵심 기여/차별점(Contributions)
- EndoCoT 프레임워크 제안: MLLM 은닉 사고 상태를 반복 정제해 Chain-of-Thought를 활성화  
- 최종 사고 정합 모듈 도입: 추론된 사고 궤적을 텍스트 감독하에 정답과 일치시켜 정확도 보장  
- 단계별 사고 가이드를 DiT의 노이즈 제거 과정에 연결해, 복잡 작업을 차례로 해결

## 한계/리스크(Limitations)
- 실세계 대규모 데이터셋 및 응용 환경에서의 성능 검증 여부: 초록 기준으로는 확인 불가  
- 반복 정제·정합 모듈 도입에 따른 연산 비용 및 추론 지연: 초록 기준으로는 확인 불가  
- 다양한 MLLM·확산 모델 조합에 대한 일반화 가능성: 초록 기준으로는 확인 불가  

## 실무 적용 아이디어(Practical Takeaways)
- Diffusion 기반 클라우드 AI 서비스에 EndoCoT 모듈을 추가해 복잡 워크플로우 단계별 지시 처리 기능 강화  
- 이미지 기반 경로 탐색·퍼즐 해결 등 단계적 추론이 필요한 응용 도메인에 적용  
- MLLM 텍스트 인코더 확장 시 반복 정제 및 정합 구조를 참고해 성능 최적화  

## 메타 정보
- 저자: Xuanlang Dai, Yujie Zhou, Long Xing, Jiazi Bu, Xilin Wei, Yuhong Liu, Beichen Zhang, Kai Chen, Yuhang Zang  
- 발행일: 2026년 3월 (arXiv v1)  
- 카테고리: AI, 머신러닝, 컴퓨터 비전, 확산 모델  

## 참고 링크
[https://arxiv.org/abs/2603.12252v1](https://arxiv.org/abs/2603.12252v1)
