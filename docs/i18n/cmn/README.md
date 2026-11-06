# 安全审查与学习

普通话 / 简体中文 · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

学习 OWASP，编写更安全的代码，并审查任何项目的提交。本技能也涵盖 MCP、大语言模型应用、智能体和技能包。

## 安装

将 security-review 文件夹复制到项目的 .agents/skills/ 目录。在需要处理的项目中调用。

## 示例

```text
$security-review 审查这次提交，并继续审查本会话中的后续提交。
$security-review 帮助我实现这个功能，并编写功能测试和安全测试。
$security-review 用测验教我 MCP 安全，每次只问一个问题。
```

## 行为与限制

技能会查询最新官方资料，解释发现的问题和修复方法，并说明实际执行了哪些测试。开发时，它会帮助验证正常操作和未经授权的操作，并根据你的回答调整教学。

技能仅在智能体会话中保持启用，会话结束后不会持续监控 Git。本译文由人工智能生成，尚未经母语使用者审校。

## 参考资料

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
