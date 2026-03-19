# 비디오 모델 추론 메커니즘 해부

**부제:** Demystifing Video Reasoning

## 한 줄 결론
비디오 확산 모델의 추론은 프레임 간 순차 처리 대신 디퓨전 단계별 denoising 과정을 통해 Chain-of-Steps로 이루어짐을 밝혔다.

## TL;DR (요약)
- 확산 기반 비디오 생성 모델이 보이는 추론 능력의 내부 메커니즘을 분석  
- 기존 Chain-of-Frames(CoF) 가설을 대신해 Chain-of-Steps(CoS)를 제시  
- working memory·self-correction·perception before action 등 emergent behavior를 규명  
- Diffusion Transformer 레이어별 기능 분화를 관찰하고, 훈련 없는 앙상블 전략을 시범 도입  

## 문제 정의(Problem)
최근 확산(diffusion) 기반 비디오 생성 모델에서 복잡한 추론 능력이 예상외로 나타나고 있다. Prior work는 Chain-of-Frames(CoF) 메커니즘을 통해 프레임 간 순차 처리가 추론 과정을 이끈다고 가정했으나, 실제 내부 동작 원리를 체계적으로 검증한 연구는 부족하다.

## 제안 방법(Method)
저자들은 정성적 분석(qualitative analysis) 및 목표 지향 프로빙(targeted probing) 실험을 통해 비디오 모델의 내부 추론 과정을 추적했다. 각 denoising 단계별 중간 출력을 관찰하여 Chain-of-Steps(CoS) 메커니즘을 도출하고, 다음과 같은 emergent reasoning behavior를 확인했다.  
- Working memory: 중간 해답을 지속 참조  
- Self-correction 및 enhancement: 잘못된 중간 해답 복구  
- Perception before action: 초기 단계에서 의미론적 정보 구축, 이후 구조적 조작 수행  
또한 Diffusion Transformer 내부 레이어별 활성화 패턴을 분석해 초기 레이어의 인지 정보 처리, 중간 레이어의 추론 수행, 말단 레이어의 정보 통합 기능을 밝혀냈다. 마지막으로 동일 모델을 서로 다른 랜덤 시드로 구동해 latent trajectory를 앙상블함으로써 별도 훈련 없이도 추론 성능을 개선하는 proof-of-concept 전략을 제안했다.

## 핵심 기여/차별점(Contributions)
- Chain-of-Frames 가설을 대체하는 Chain-of-Steps(CoS) 메커니즘 규명  
- Working memory, self-correction, perception before action 등 3가지 emergent reasoning behavior 확인  
- Diffusion Transformer 레이어별 기능 분화 분석 및 훈련 없는 latent 앙상블 전략 제시  

## 한계/리스크(Limitations)
- 다양한 비디오 생성 아키텍처 및 실제 환경에서 CoS 메커니즘의 일반화 여부는 초록 기준으로는 확인 불가  
- 제시된 training-free 앙상블의 성능 향상 폭 및 계산 비용 효율성은 초록 기준으로는 확인 불가  
- Emergent behavior 분석이 정성적 관찰 기반이며, 정량적 검증 범위는 초록에서 불명확  

## 실무 적용 아이디어(Practical Takeaways)
- 디퓨전 단계별 중간 출력을 모니터링해 모델 추론 흐름을 시각화·디버깅  
- 동일 확산 모델을 다른 랜덤 시드로 실행하여 latent trajectory 앙상블 적용 검토  
- Diffusion Transformer 각 레이어별 역할에 맞춘 모듈 최적화 및 커스터마이징 전략 모색  

## 메타 정보
- 저자: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
- 발행일: 초록 기준으로는 확인 불가  
- 카테고리: 초록 기준으로는 확인 불가  

## 참고 링크
[https://arxiv.org/abs/2603.16870v1](https://arxiv.org/abs/2603.16870v1)
