# 3D 실내 장면 심볼릭 평가

**부제:** SceneCritic: A Symbolic Evaluator for 3D Indoor Scene Synthesis

## 한 줄 결론
SceneCritic은 구조화된 공간 온톨로지를 활용해 3D 실내 레이아웃의 의미·방위·기하학적 일관성을 안정적으로 평가한다.

## TL;DR (요약)
- 기존에는 대형 언어 모델(LLM) 또는 비전-언어 모델(VLM)을 이용해 렌더링된 장면을 평가했으나, 시점·프롬프트·환각 현상에 민감하여 평가가 불안정하다.  
- SceneCritic은 SceneOnto라는 구조화된 공간 온톨로지를 기반으로, 층평면(floor-plan) 수준 레이아웃의 제약조건을 심볼릭하게 검증한다.  
- 객체 간 의미적 관계, 방향 정렬, 충돌 및 거리 제약을 동시에 검사하며, 위반 사항과 적합 배치를 세부적으로 식별한다.  
- 다양한 비평자 모달리티(rule-based, LLM-based, VLM-based)를 이용한 반복 개선 실험에서, SceneCritic이 인간 판단과 가장 높은 정렬도를 보였다.

## 문제 정의(Problem)
3D 실내 장면 합성을 위한 모델들은 중간 구조물(layout, scene graph)을 생성한 뒤 이를 렌더링하여 시각적 평가를 받는다. 이때 LLM 또는 VLM 기반 평가자가 렌더된 이미지를 통해 점수를 매기는데,  
- 시점(viewpoint)에 따라 결과가 달라지고  
- 프롬프트(prompt)의 문구에 민감하며  
- 모델 환각(hallucination)에 취약하다  

는 문제가 있다. 이러한 불안정성은 실제로 생성된 장면의 공간적 타당성(spatial plausibility)과 평가자의 특성 중 어느 쪽이 결과를 좌우하는지 판별을 어렵게 만든다.

## 제안 방법(Method)
본 연구는 2단계로 구성된다.  
1. SceneOnto 구축  
   - 3D-FRONT, ScanNet, Visual Genome의 실내 장면 사전(prior)을 집계해 의미, 방향, 기하학 제약을 표현하는 구조화된 공간 온톨로지(SceneOnto)를 설계.  
2. SceneCritic 평가기 개발  
   - SceneOnto를 기반으로 층평면 수준 레이아웃을 입력받아  
     - 객체 수준(object-level): 충돌(collision), 거리(distance) 등 물리적 제약 점검  
     - 관계 수준(relationship-level): 의미적 관계(예: 책상 위에 책), 방향 정렬(예: 의자가 책상 앞을 향함) 검증  
   - 구체적인 위반 유형과 성공 배치 사례를 식별해 리포트 형태로 출력  
3. 반복 개선(iterative refinement) 실험  
   - rule-based critic: 충돌 제약만 피드백  
   - LLM critic: 레이아웃을 텍스트로 변환해 피드백  
   - VLM critic: 렌더링 이미지를 입력으로 피드백  
   - 세 모달리티별로 모델이 구조를 어떻게 수정하는지 비교 분석

## 핵심 기여/차별점(Contributions)
- SceneOnto: 다양한 데이터셋(3D-FRONT, ScanNet, Visual Genome)의 공간 사전을 통합한 3D 실내 장면 온톨로지  
- SceneCritic: 온톨로지 기반 제약조건으로 의미·방위·기하학 일관성을 동시에 검증하고 위반 지점을 구체적으로 식별  
- 실험 결과:  
  - Symbolic critic이 VLM 평가자보다 인간 판단과 높은 정렬(Alignment)을 달성  
  - 텍스트 기반 LLM이 VLM을 능가하는 의미적 레이아웃 품질 보임  
  - 이미지 기반 VLM 조정 모달리티가 의미·방위 보정에 가장 효과적

## 한계/리스크(Limitations)
- 평가 대상이 층평면(floor-plan) 수준 레이아웃에 한정된다. 실제 3D 모델 전체(포인트 클라우드나 메시 수준) 검증 여부는 초록 기준으로는 확인 불가  
- SceneOnto 온톨로지의 완전성(completeness) 및 일반화 범위(generalization)는 초록만으로 판단하기 어렵다  
- 반복 개선 실험의 계산 비용 및 대규모 데이터셋 확장성은 초록 기준으로 확인할 수 없다

## 실무 적용 아이디어(Practical Takeaways)
- 3D 설계 파이프라인에 SceneCritic 유사 심볼릭 평가기를 도입해 초기 레이아웃 검수 자동화  
- SceneOnto 방식으로 도메인별 공간 규칙(semantic, orientation, collision)을 온톨로지 형태로 정립  
- 다양한 비평자 모달리티(rule/LLM/VLM)를 조합한 반복 개선 워크플로우로 모델 학습 또는 시뮬레이션 품질 향상

## 메타 정보
- 저자: Kathakoli Sengupta, Kai Ao, Paola Cascante-Bonilla  
- 발행일: 2026년 4월 (arXiv v1)  
- 카테고리: 컴퓨터 비전(Computer Vision), 3D 장면 합성(3D Scene Synthesis)

## 참고 링크
[https://arxiv.org/abs/2604.13035v1](https://arxiv.org/abs/2604.13035v1)
