# 安全審查同學習

粵語 / 繁體中文 · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

學習 OWASP、寫更安全嘅程式碼，同埋審查任何專案嘅 commit。呢個 skill 亦涵蓋 MCP、LLM 應用、AI 代理同 skill 套件。

## 安裝

將 security-review 資料夾複製去專案嘅 .agents/skills/ 目錄。喺你想處理嘅專案入面呼叫佢。

## 例子

```text
$security-review 幫我審查呢個 commit，之後嘅 commit 都繼續跟進。
$security-review 幫我實作呢個功能，連同功能測試同安全測試一齊做。
$security-review 用問答教我 MCP 安全，每次只問一條問題。
```

## 運作同限制

Skill 會查閱最新官方資料，解釋發現嘅問題同修正方法，並講清楚實際跑過邊啲測試。寫程式嗰陣會協助測試正常使用同未獲授權嘅操作，亦會按你嘅答案調整教學。

佢只會喺代理工作階段入面保持啟用；階段結束後唔會繼續監察 Git。呢份翻譯由 AI 產生，未經母語使用者校對。

## 參考資料

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
