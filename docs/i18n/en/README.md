# Security review and learning

English · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

Study OWASP, build safer code, and review commits in any project. This skill also covers MCP, LLM applications, agents, and skills.

## Installation

Copy the security-review folder into your project's .agents/skills/ directory. Invoke it from the project you want to work on.

## Examples

```text
$security-review Review this commit and stay active for the next ones.
$security-review Help me implement this feature with functional and security tests.
$security-review Teach me MCP security with a quiz, one question at a time.
```

## Behavior and limits

The skill checks current official sources, explains findings and fixes, and reports which tests actually ran. During development it helps write tests for valid use and unauthorized actions. It adapts lessons to your answers.

It stays active within the agent session; it does not monitor Git after the session ends. This translation is AI-generated and has not been reviewed by a native speaker.

## References

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
