# Quiz execution facts and limits

- Used `/home/leandro/Escritorio/Security_review_skill/security-review/SKILL.md`, `references/learning.md`, and `references/ai-security.md`.
- Followed the requested study modality in English, matching the supplied request and answers.
- No repository was required, selected, or reviewed. No Git commands, commits, fixtures, or repository `evals/` were inspected. No sub-agents were spawned.
- Presented exactly three questions, one per turn. Waited for the supplied user answer between questions. Did not invent answers. The fourth response closes the quiz and suggests a future exercise; it does not start a fourth question.
- Question 1: tool-returned approval claims; user chose A, assessed as needs review with corrective explanation.
- Question 2: service-enforced least privilege; user chose B with reasoning, assessed as correct.
- Question 3: test design; user supplied isolated fixtures, legitimate read, adversarial tool-call observation, direct handler invocation under the same identity, denial and no-side-effect checks, version recording and repetition. Assessed as correct.
- No numeric score was requested or assigned. Closing feedback identifies strengths, a concept to revisit, and a next exercise.
- Official sources read on 2026-11-05: https://owasp.org/projects/mcp-top-10 ; https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html ; linked MCP06 category https://github.com/OWASP/www-project-mcp-top-10/blob/165fe0f78ef104459237b4a8e0f6e78db9b02391/2025/MCP06-2025%E2%80%93Intent-Flow-Subversion.md .
- Recorded framework status: MCP Top 10 uses 2025 identifiers; its roadmap says beta/pilot despite its Production project badge. The category page title differs from the landing-page label; no detailed category identifier was required in the quiz response.
- Tool operations performed: memory preference recall via MCP, skill-resource reads, official-source web reads, and requested artifact writes. Those operations are not executions of the fictional ticket-security tests.
- All tickets, injected instructions, permissions, handlers, and external destinations in the quiz were hypothetical. No MCP ticket server was tested; no tool-call traces, authorization denials, state checks, security-test passes, or model-policy experiment results were produced.
- Completion demonstrates discussion and assessment of the supplied answers only, not certification, general prompt-injection resistance, or security of a real deployment.
