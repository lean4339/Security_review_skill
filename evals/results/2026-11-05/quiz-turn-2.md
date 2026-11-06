**Needs review.** Connecting an MCP tool lets the assistant use that connection within your authorized task; it does not make every returned document or claim of approval trustworthy. A tool can return attacker-controlled text even when you deliberately connected it.

**B is correct.** Your request authorized summarizing, not sending the document elsewhere. The returned claim cannot grant that permission. The application must enforce authorization for subsequent tool calls independently of what the model reads or believes. [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html#12-prompt-injection-via-tool-return-values)

**Question 2 of 3 — choose one answer and briefly explain why.**

In another fictional example, an assistant should only read support tickets. Its MCP server also exposes a tool that deletes tickets. Which setup best enforces the intended restriction even if a malicious ticket persuades the model to try deleting one?

- **A.** Add “never delete tickets” to the model’s prompt, while keeping credentials that allow deletion.
- **B.** Give the server credentials restricted to reading tickets, and have the service reject deletion requests for that identity.
- **C.** Keep credentials that allow deletion, but rename the deletion tool “administrators only.”

Which option do you choose, and why?
