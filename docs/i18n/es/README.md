# Revisión de seguridad y aprendizaje

Español · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

Estudiá OWASP, escribí código más seguro y revisá commits de cualquier proyecto. La skill también cubre MCP, aplicaciones LLM, agentes y paquetes de skills.

## Instalación

Copiá la carpeta security-review al directorio .agents/skills/ de tu proyecto. Invocala desde el proyecto sobre el que querés trabajar.

## Ejemplos

```text
$security-review Revisá este commit y quedá activa para los siguientes.
$security-review Ayudame a implementar esta funcionalidad con tests funcionales y de seguridad.
$security-review Enseñame seguridad MCP con un cuestionario, una pregunta por vez.
```

## Comportamiento y límites

La skill consulta fuentes oficiales vigentes, explica hallazgos y correcciones e indica qué tests ejecutó realmente. Durante el desarrollo ayuda a probar el uso legítimo y las acciones no autorizadas. Adapta las lecciones a tus respuestas.

Queda activa dentro de la sesión del agente; no monitorea Git después de cerrarla. Este texto fue generado por IA y no tiene revisión lingüística independiente.

## Referencias

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
