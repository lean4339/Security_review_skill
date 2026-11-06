# Revisão de segurança e aprendizado

Português · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

Estude OWASP, escreva código mais seguro e revise commits de qualquer projeto. A skill também abrange MCP, aplicações LLM, agentes e pacotes de skills.

## Instalação

Copie a pasta security-review para o diretório .agents/skills/ do projeto. Invoque a skill a partir do projeto em que deseja trabalhar.

## Exemplos

```text
$security-review Revise este commit e continue ativa para os próximos.
$security-review Ajude-me a implementar esta funcionalidade com testes funcionais e de segurança.
$security-review Ensine-me segurança MCP com um questionário, uma pergunta por vez.
```

## Comportamento e limites

A skill consulta fontes oficiais atuais, explica os problemas e as correções e informa quais testes realmente executou. Durante o desenvolvimento, ajuda a testar usos legítimos e ações não autorizadas. Adapta as aulas às suas respostas.

Ela permanece ativa durante a sessão do agente; não monitora o Git depois que a sessão termina. Esta tradução foi gerada por IA e não foi revisada por um falante nativo.

## Referências

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
