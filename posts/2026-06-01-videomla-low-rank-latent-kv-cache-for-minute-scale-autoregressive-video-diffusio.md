# 분 단위 비디오 확산 메모리 절감

**부제:** VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion

## 한 줄 결론
VideoMLA는 다중 헤드 잠재(Multi-Head Latent Attention, MLA) 키-값(Key-Value, KV) 캐시 구조를 도입해 영상 확산 모델의 KV 메모리를 92.7% 절감하면서 장기 스트리밍 성능을 유지한다.

## TL;DR (요약)
- VideoMLA는 공유된 저차원 콘텐츠 잠재 및 분리된 3차원 회전 위치 인코딩(Rotary Positional Encoding, 3D-RoPE) 키를 사용해 per-head KV 메모리를 계층당 토큰당 92.7% 감소시킨다.  
- 사전 학습된 비디오 어텐션이 저차원 스펙트럼 가정을 따르지 않지만, MLA 보틀넥이 효과적인 랭크를 결정하여 품질 손실 없이 압축을 가능하게 한다.  
- 스펙트럼 초기화와 랜덤 초기화를 비교한 결과, 두 방식 모두 MLA 보틀넥 내에서 랭크 예산을 최대한 활용하며 학습을 통해 적응이 이루어짐을 확인했다.  
- VBench 벤치마크에서 짧은/긴 호라이즌 모두 경쟁력 있는 생성 품질을 유지하고, 단일 B200 GPU에서 처리량을 1.23× 향상했다.

## 문제 정의(Problem)
- 분 단위 장기 스트리밍(autogressive) 비디오 확산 모델은 고정 크기 슬라이딩 윈도우(key-value, KV) 캐시를 사용하며, per-head KV 레이아웃이 메모리 사용량과 지연(latency)의 주요 병목을 형성한다.  
- 최근 연구들은 윈도우 내 토큰 선택이나 위치 인코딩 개선에 집중했으나, per-head KV 매트릭스 구조 자체는 거의 변하지 않았다.  
- 모델 크기와 시퀀스 길이가 증가함에 따라 비디오 확산 실시간 처리와 메모리 효율성 개선이 절실히 요구된다.

## 제안 방법(Method)
VideoMLA는 다음과 같은 핵심 구성요소로 per-head KV 캐시를 저차원 구조로 전환한다.  
- 공유 저차원 콘텐츠 잠재: 모든 어텐션 헤드에서 공유되는 저차원(latent) 키·값 표현으로, 토큰당 KV 메모리를 대폭 축소한다.  
- 분리된 3차원 회전 위치 인코딩(Rotary Positional Encoding, 3D-RoPE) 키: 비디오 시퀀스의 시공간 위치 정보를 3D RoPE 방식으로 인코딩하여 헤드 간 공유한다.  
이 구조를 통해 각 캐시 레이어에서 토큰당 KV 메모리가 92.7% 절감되며, 모델 품질 저하 없이 긴 호라이즌 스트리밍에도 적용 가능함을 보였다.  
추가로, 스펙트럼 기반 초기화와 랜덤 초기화를 적용해 MLA 보틀넥이 사전 학습된 스펙트럼(주파수)보다 유효 랭크를 결정함을 실험적으로 분석했다.

## 핵심 기여/차별점(Contributions)
- 비디오 확산에 Multi-Head Latent Attention(MLA) 구조를 최초 도입해 per-head key·value를 공유된 저차원 및 3D-RoPE 키로 대체, KV 메모리를 92.7% 절감.  
- 사전 학습된 비디오 어텐션이 저차원 스펙트럼 가정을 따르지 않음에도, MLA 보틀넥이 유효 랭크를 결정해 품질을 유지함을 규명.  
- VBench 벤치마크에서 짧은·긴 호라이즌 스트리밍 확산 성능을 경쟁력 있게 유지하며, 단일 B200 GPU에서 처리량을 1.23× 향상.

## 한계/리스크(Limitations)
- 본 초록에서는 메모리 절감 및 처리량 개선 수치는 제시되나, 생성 품질(예: PSNR, FID) 세부 수치는 확인 불가.  
- 제안된 구조의 일반화 성능은 VBench에 국한되어 있으며, 다른 대규모 비디오 데이터셋에서의 검증은 초록 기준으로 확인 불가.  
- 단일 B200 GPU에서의 처리량 향상 결과 외에 다양한 하드웨어 및 분산 환경에서의 성능은 초록만으로는 예측하기 어렵다.

## 실무 적용 아이디어(Practical Takeaways)
- 대규모 비디오 생성 파이프라인에서 per-head KV 캐시 메모리 병목 해소를 위해 저차원 잠재 공유 구조(MLA) 도입을 고려.  
- 3D-RoPE 위치 인코딩을 통합해 메모리 절감과 시공간 위치 민감도를 동시에 확보할 수 있음.  
- 모델 압축 후에도 실시간 스트리밍 환경에서 처리량을 개선해, 클라우드 인프라 비용 절감과 사용자 경험 향상을 도모할 수 있다.

## 메타 정보
저자: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag  
발행일: 2026-05 (arXiv preprint)  
카테고리: Video Diffusion, Model Compression, Attention Mechanisms

## 참고 링크
[https://arxiv.org/abs/2605.30351v1](https://arxiv.org/abs/2605.30351v1)
