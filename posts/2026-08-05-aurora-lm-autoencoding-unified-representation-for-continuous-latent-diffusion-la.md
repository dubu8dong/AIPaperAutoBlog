# 연속 잠재 확산 언어 모델 AURORA

**부제:** AURORA-LM: Autoencoding Unified Representation for Continuous-Latent Diffusion Language Modeling

## 한 줄 결론
고용량 디코딩 가능한 연속 잠재 표현과 블록 인과 확산 구조를 결합해 텍스트 생성 성능을 크게 개선한 모델이다.

## TL;DR (요약)
- 기존 텍스트 생성은 이산 토큰에 의존해 왔으나 AURORA-LM은 디코딩 가능한 고용량 연속 잠재(latent)를 유지하며 직접 확산(diffusion) 분포를 학습한다.
- Query-based 인코더-디코더로 생성된 prefix-aligned 연속 잠재 시퀀스를 Block-causal Diffusion Transformer가 블록 단위 좌→우 생성 및 병렬 디노이징 방식으로 모델링한다.
- 노이즈 입력 경로만 제한하고 깨끗한 잠재 전체를 예측 대상으로 삼아 표현 용량을 보전한다.
- 노이즈 레벨 분포를 잠재 폭(width)에 맞춰 보정하고 self-trajectory consistency로 훈련·추론 간 도메인 격차를 줄인다.
- OpenWebText 자유 생성 및 XSum 요약 평가에서 기존 연속·확산 기반 언어 모델 대비 우수한 성능을 달성했다.

## 문제 정의(Problem)
텍스트 생성을 위한 기존 언어 모델은 이산 토큰(discrete tokens)에 기반해 왔으며, 이미지나 오디오처럼 연속 잠재 공간을 활용한 generative 모델링과 격차가 존재한다.  
일부 continuous language model은 디코딩용으로 설계되지 않은 임베딩 공간을 그대로 사용하거나 확산 모델 학습을 위해 잠재 표현을 압축하면서 토큰 수준의 충실도를 희생한다.  
그 결과 텍스트 생성과 디코딩 과정을 동시에 만족시키는 고용량 연속 잠재 표현 학습이 어려운 상태이다.

## 제안 방법(Method)
AURORA-LM은 텍스트 잠재 표현의 구축과 그 분포 모델링 과정을 명확히 분리한다.  
1) Query-based Encoder-Decoder를 통해 디코딩 가능한 고용량, prefix-aligned 연속 잠재 시퀀스를 생성한다.  
2) Block-causal Diffusion Transformer는 flow matching 기반 확산 학습을 활용해 블록 단위로 좌→우 순차적으로 잠재를 생성하며 각 블록 내 위치를 병렬로 디노이징한다.  
3) 표현 학습 난이도 증가를 보완하기 위해 노이즈 입력 경로만 제약하고 깨끗한 잠재 전체를 예측 대상으로 유지하여 디코더가 마주하는 용량을 줄이지 않는다.  
4) 잠재 시퀀스 폭(width)에 맞춰 노이즈 레벨 분포를 보정하고, 훈련 시 독립적으로 표본화된 노이즈와 추론 시 반복적 디노이징 절차 간 self-trajectory consistency를 도입해 도메인 차이를 최소화한다.

## 핵심 기여/차별점(Contributions)
- decodable 고용량 연속 잠재 표현과 확산 기반 분포 모델링을 별도 모듈로 분리하여 충실도를 유지하면서 확산 학습을 수행  
- Block-causal Diffusion Transformer 설계로 블록 단위 좌→우 생성 및 병렬 디노이징을 통해 효율적 시퀀스 생성 지원  
- 노이즈 레벨 분포 보정 및 self-trajectory consistency 기법으로 훈련·추론 간 도메인 격차를 해소

## 한계/리스크(Limitations)
- 고용량 잠재 표현이 확산 모델 학습 대상이 되면서 학습 난이도가 상승할 수 있음  
- 실험이 Ascend NPU 환경에만 국한되어 다른 하드웨어에서의 성능 및 효율성은 확인 불가  
- 다른 언어, 도메인으로의 일반화 가능성 및 미세조정(fine-tuning) 특성은 초록 기준으로는 확인 불가

## 실무 적용 아이디어(Practical Takeaways)
- 기존 토큰 기반 생성 파이프라인에 continuous-latent 확산 모델 구조를 모듈 형태로 통합해 성능 및 품질 개선을 시도  
- Query-based 인코더-디코더와 Block-causal Diffusion Transformer를 참조해 시퀀스 생성 시스템의 병렬화 및 효율성 강화  
- 노이즈 레벨 분포 보정 및 self-trajectory consistency 기법을 활용해 확산 모델의 학습 안정성과 추론 일관성 확보

## 메타 정보
- 저자: Jiajun Liang, Yucheng Liao, Yukang Cao, Jiazhe Wei, Ken Li, Wende Tan, Jiankun Zhang, ZY Cui, Jingkang Yang, Liucheng Guo, Shiqi Yang, B. Yang, Caifeng Shan, Ziwei Liu, Chenyang Si  
- 발행일: 2026년 8월 (arXiv preprint)  
- 카테고리: Language Modeling, Diffusion Models, Generative AI, Continuous Latent

## 참고 링크
[https://arxiv.org/abs/2608.02602v1](https://arxiv.org/abs/2608.02602v1)
