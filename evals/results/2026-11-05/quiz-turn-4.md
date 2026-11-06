**Correct.** Your procedure checks both legitimate access and denied deletion, verifies actual effects, and tests the service directly so model refusal cannot conceal a missing authorization check. Recording versions and repeating adversarial cases also keeps the conclusions appropriately limited.

You completed all **three questions**:

- **Question 1 — needs review:** Connecting an MCP tool does not turn its returned text into user authorization.
- **Question 2 — correct:** The service must enforce permissions independently of the model.
- **Question 3 — correct:** Test permitted behavior, forbidden calls, and resulting state; an assistant’s verbal refusal is insufficient evidence.

Your strongest area was designing checks that can expose a missing control. Keep practicing the distinction between a trusted connection and untrusted content returned through it. Your final answer applied that distinction by testing the forged approval claim.

For a future exercise, adapt your procedure to a read-only tool that attempts to send ticket contents to an external destination: verify the data-sharing boundary as well as write permissions. OWASP discusses both [tool-result injection and independent authorization](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html#12-prompt-injection-via-tool-return-values).

This was a discussion of test design; no MCP security tests were executed, and the quiz does not certify a system’s security.
