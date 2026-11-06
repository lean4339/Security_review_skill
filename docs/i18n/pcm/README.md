# Security review and learning

Naijá / Nigerian Pidgin · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

Learn OWASP, write code wey safe pass, and review commits for any project. This skill also cover MCP, LLM apps, agents and skill packages.

## How to install

Copy security-review folder put inside your project .agents/skills/ directory. Call the skill from the project wey you wan work on.

## Examples

```text
$security-review Review this commit and stay active for the next ones.
$security-review Help me build this feature with functional tests and security tests.
$security-review Teach me MCP security with quiz; ask one question at a time.
```

## How e work and limits

The skill go check current official sources, explain problems and fixes, and tell you which tests e really run. As you dey code, e go help test correct use and actions wey no get permission. E go adjust lessons based on your answers.

E dey active only inside the agent session; e no dey watch Git after the session end. Na AI make this translation; native speaker never review am.

## Sources

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
