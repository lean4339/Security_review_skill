# セキュリティレビューと学習

日本語 · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

OWASPを学び、より安全なコードを書き、任意のプロジェクトのコミットをレビューできます。このスキルはMCP、LLMアプリ、エージェント、スキルパッケージも対象にします。

## インストール

security-reviewフォルダーをプロジェクトの.agents/skills/ディレクトリーにコピーしてください。作業対象のプロジェクトから呼び出します。

## 使用例

```text
$security-review このコミットをレビューし、以降のコミットも継続して確認してください。
$security-review この機能の実装と、機能テストおよびセキュリティテストの作成を手伝ってください。
$security-review MCPのセキュリティをクイズで教えてください。一度に一問ずつ出してください。
```

## 動作と制限

最新の公式資料を確認し、問題と修正方法を説明し、実際に実行したテストを報告します。開発中は正当な操作と権限のない操作のテストを支援し、回答に応じて学習内容を調整します。

スキルが有効なのはエージェントのセッション内です。終了後にGitを監視することはありません。この翻訳はAI生成で、母語話者による校閲は受けていません。

## 参考資料

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
