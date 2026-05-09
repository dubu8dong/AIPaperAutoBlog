# 동영상 생성용 제로샷 카메라·모션 제어
**부제:** ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation

## 한 줄 결론
영상 확산 모델을 활용한 ActCam은 깊이(depth)와 포즈(pose) 조건을 두 단계로 조합해 제로샷으로 일관된 카메라 및 3D 모션 제어를 달성한다.

## TL;DR (요약)
- 비디오 생성에서 배우의 모션과 카메라 궤적을 동시에 정밀 제어하는 문제를 다룬다.  
- ActCam은 사전 학습된 이미지-투-비디오 확산 모델에 깊이와 포즈 조건을 공급해 프레임별 카메라 파라미터를 제어한다.  
- 초기 단계에는 깊이와 포즈를 모두 사용해 구조적 일관성을 확보하고, 이후 단계에서 깊이를 제거해 고주파 모션 디테일을 강화한다.  
- 벤치마크 및 인간 평가에서 기존 포즈 단독 제어 대비 카메라 고수 및 모션 충실도 측면에서 우수함을 보였다.

## 문제 정의(Problem)
- 예술적 목적의 비디오 생성에서는 배우의 모션(performance)과 카메라 시네마토그래피(cinematography)를 함께 제어해야 함.  
- 기존 확산 모델은 주로 프레임별 포즈(pose) 제어에 초점을 두고 있어 복합적인 카메라 움직임을 반영하기 어려움.  
- 제로샷(zero-shot)으로 새로운 장면(scene)에 모션을 옮기고, 프레임마다 내·외부 카메라 파라미터(intrinsic/extrinsic)를 세밀 조정하는 방법이 요구됨.

## 제안 방법(Method)
- 사전 학습된 이미지-투-비디오(image-to-video) 확산 모델을 기반으로 함. 해당 모델은 장면 깊이(depth)와 배우 포즈(pose)를 입력 조건(conditioning)으로 지원.  
- 입력으로는 원본 소스 비디오의 모션과 목표 카메라 궤적(target camera motion)을 사용.  
- 프레임별로 기하학적 일관성을 유지하는 포즈 및 깊이 맵을 생성하고, 두 단계(two-phase) 조건 스케줄링을 도입:  
  1. 초기 denoising 단계: sparse depth와 pose를 모두 조건으로 사용해 장면 구조를 강제함.  
  2. 후반부 단계: depth 조건을 제거하고 pose-only로 고주파 모션 디테일을 정제함.  
- 하나의 샘플링 프로세스로 joint camera·motion 제어를 수행해 추가 학습 없이 제로샷으로 결과를 생성.

## 핵심 기여/차별점(Contributions)
- 제로샷 환경에서 프레임별 내·외부(intrinsic/extrinsic) 카메라 파라미터를 동시에 제어할 수 있는 메커니즘 제안.  
- 기하학적 일관성을 보장하는 depth+pose 기반 조건 생성 및 two-phase denoising 스케줄링 도입.  
- 대규모 벤치마크 및 사람 평가에서 기존 포즈 제어 및 타 카메라 제어 방법 대비 카메라 고수(camera adherence)와 모션 충실도(motion fidelity)를 향상.

## 한계/리스크(Limitations)
- 제안 방법은 기저(pretrained) 이미지-투-비디오 확산 모델의 성능과 한계에 종속됨.  
- 실시간 처리 속도나 고해상도 지원 여부는 초록 기준으로는 확인 불가.  
- 복잡한 장면이나 다중 배우(multi-character) 환경에서의 성능은 초록 기준으로는 확인 불가.

## 실무 적용 아이디어(Practical Takeaways)
- GPU 기반 클라우드 인퍼런스 환경에서 ActCam 파이프라인을 구축해 다양한 시네마틱 연출 실험 가능.  
- 기존 비디오 후처리 워크플로우에 포즈·깊이 추출 모듈을 추가해 joint camera·motion 제어 기능을 확장.  
- 두 단계 스케줄링을 커스텀하여 구조적 안정성 및 디테일 표현 간 밸런스를 조정하는 사용자 정의 가능.

## 메타 정보
- 저자(Authors): Omar El Khalifi, Thomas Rossi, Oscar Fossey, Thibault Fouque, Ulysse Mizrahi, Philip Torr, Ivan Laptev, Fabio Pizzati, Baptiste Bellot-Gurlet  
- 발행일(Published): 2026년 5월 (arXiv v1)  
- 카테고리(Category): Computer Vision and Pattern Recognition (cs.CV)

## 참고 링크
[https://arxiv.org/abs/2605.06667v1](https://arxiv.org/abs/2605.06667v1)
