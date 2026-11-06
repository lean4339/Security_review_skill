# 보안 검토와 학습

한국어 · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

OWASP를 배우고 더 안전한 코드를 작성하며 모든 프로젝트의 커밋을 검토하세요. 이 스킬은 MCP, LLM 애플리케이션, 에이전트와 스킬 패키지도 다룹니다.

## 설치

security-review 폴더를 프로젝트의 .agents/skills/ 디렉터리에 복사하세요. 작업할 프로젝트에서 스킬을 호출하세요.

## 예시

```text
$security-review 이 커밋을 검토하고 다음 커밋에도 계속 활성 상태를 유지해 줘.
$security-review 기능 테스트와 보안 테스트를 포함해 이 기능을 구현하도록 도와줘.
$security-review 퀴즈로 MCP 보안을 가르쳐 줘. 한 번에 한 문제씩 질문해 줘.
```

## 동작과 한계

스킬은 최신 공식 자료를 확인하고 발견한 문제와 수정 방법을 설명하며 실제로 실행한 테스트를 보고합니다. 개발 중에는 정상 사용과 권한 없는 동작을 테스트하도록 돕고, 답변에 맞춰 학습 내용을 조정합니다.

에이전트 세션 안에서만 활성 상태를 유지하며 세션 종료 후 Git을 감시하지 않습니다. 이 번역은 AI가 생성했으며 원어민의 검토를 받지 않았습니다.

## 참고 자료

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
