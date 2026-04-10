# 정확성 인증의 계산 경계  
**부제:** Toward a Tractability Frontier for Exact Relevance Certification  

## 한 줄 결론  
효율적으로 검증 가능한 구조적 술어만으로는 정확한 관련성 인증의 계산 경계를 완전하게 분류할 수 없음을 증명했다.  

## TL;DR (요약)  
정확한 관련성 인증은 좌표 구조화된 결정 문제에서 최적 행동에 필요한 좌표를 식별하는 과제다.  
논문은 유한 원시(primitive) 기반을 허용하는 계산 가능성(family)에서도 최적화-몫(optimizer-quotient) 실현 가능성이 최대여서, 몫 형태만으로 경계를 규정하기 어렵다고 지적한다.  
메타-불가능성 정리를 통해, 정확한 인증을 강제하는 폐쇄(closed under) 법칙 하에서 불변하는 효율적 구조 술어도 계산 경계를 완전 분류할 수 없음을 보였다.  
네 가지 장애(obstruction) 가족—지배-쌍 농축(dominant-pair concentration), 마진 은폐(margin masking), 유령-행동 농축(ghost-action concentration), 덧셈/상태별 오프셋 농축(additive/statewise offset concentration)—에 대한 동일 궤도 불일치를 구성하여 불가능성을 입증했다.  

## 문제 정의(Problem)  
Exact relevance certification은 다차원 좌표로 구성된 결정 문제(coordinate-structured decision problem)에서 최적 행동(optimal action)을 결정하는 데 필수적인 좌표만을 정확히 판별하는 문제를 다룬다.  
이를 계산적으로 분류하기 위해서는 문제 인스턴스의 구조적 특성을 표현하는 효율적 술어(structural predicate)가 필요하나, 최적화-몫 실현 가능성이 최대(maximal)인 경우가 존재하여 단일한 몫 형태(quotient shape)만으로 계산 가능성의 경계를 정의하기 어렵다.  

## 제안 방법(Method)  
- 정확한 관련성 인증이 강제하는 폐쇄(closed under closure laws) 법칙 하에서 불변(invariant)하는 효율적 구조 술어를 가정하고 메타-불가능성 정리(meta-impossibility theorem)를 증명  
- 영 왜곡(zero-distortion) 요약, 몫 엔트로피(quotient entropy) 상한, 지원 수(support-counting) 기법을 활용하여 구조적 수렴(structural convergence)을 분석  
- 네 가지 장애(obstruction) 가족(지배-쌍 농축, 마진 은폐, 유령-행동 농축, 덧셈/상태별 오프셋 농축)에 대해 액션-독립(action-independent), 쌍-대상(pair-targeted) 아핀(affine) 증명(witness)을 사용한 동일 궤도(same-orbit) 불일치를 구성  

## 핵심 기여/차별점(Contributions)  
- 메타-불가능성 정리 제시: 효율적으로 검증 가능한 구조적 술어만으로 정확한 관련성 인증의 계산 가능성 경계를 완전 분류할 수 없음을 보임  
- 영 왜곡 요약, 몫 엔트로피 상한, 지원 수 계산을 결합한 구조적 수렴 분석을 통해 정확성 인증의 폐쇄 법칙이 자연스러운 이유를 설명  
- 네 가지 장애 가족(obstruction families)에 대한 동일 궤도 불일치 구성을 통해 폐쇄-폐도메인(closure-closed domain) 상 올바른 판별기도 완전 분류에 실패함을 입증  

## 한계/리스크(Limitations)  
- 초록 기준으로는 구체적 알고리즘의 시간·공간 복잡도나 실제 데이터셋 적용 여부 확인 불가  
- 결과가 폐쇄-폐도메인(closure-closed domain)에 한정되므로, 해당 조건이 성립하지 않는 도메인에 대한 확장성은 미확인  
- 구조 술어와 증명 방식(action-independent, pair-targeted affine witnesses)의 범위 외 적용 가능성은 초록만으로 확인 불가  

## 실무 적용 아이디어(Practical Takeaways)  
- 구조 기반 판별기(descriptor)를 설계할 때, 정확한 관련성 인증의 계산 경계에 대한 메타 불가능성을 염두에 두고 근사 혹은 휴리스틱 기법을 병행 고려  
- 문제 도메인 모델링 단계에서 폐쇄성(closure) 검증을 우선 수행하여, 이후 구조 술어 판별기의 적용 가능 범위를 명확히 정의  
- 네 가지 장애 요인(obstruction families)을 참고하여, 해당 패턴이 의도치 않게 발생하지 않도록 데이터 및 문제 설정을 점검  

## 메타 정보
- 저자: Tristan Simas  
- 발행일: 2026년 4월 (arXiv v1)  
- 카테고리: arXiv preprint (구체적 카테고리 초록 기준으로는 불가)  

## 참고 링크  
[https://arxiv.org/abs/2604.07349v1](https://arxiv.org/abs/2604.07349v1)
