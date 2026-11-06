# Security_review_skill

[🌐 Documentación en 32 idiomas](docs/i18n/README.md) · [Evaluación y casos testigo](evals/README.md)

Skill reutilizable para estudiar OWASP, escribir código seguro y revisar commits de cualquier proyecto con las técnicas vigentes del Top 10. Este repositorio distribuye la skill; el trabajo se realiza sobre el proyecto desde el que se la invoca. También permite estudiar sin repositorio.

## Uso

La skill está en [`security-review/SKILL.md`](security-review/SKILL.md). Copiá la carpeta `security-review` a la ubicación de skills de tu agente. En Codex puede instalarse para un proyecto en `.agents/skills/security-review/`.

Ejemplos de invocación desde el proyecto que querés revisar:

```text
$security-review revisá este commit y quedá activa para los próximos.
$security-review revisá el commit <SHA> de /ruta/al/proyecto.
$security-review revisá cada commit de <base>..<head>.
$security-review enseñame OWASP con ejercicios en Python.
$security-review haceme un cuestionario sobre autorización, de a una pregunta.
$security-review acompañame mientras implementamos este endpoint y explicame los controles de seguridad.
$security-review programemos esta funcionalidad y después preguntame sobre las decisiones de seguridad.
$security-review escribí tests de funcionamiento y de seguridad para este endpoint.
$security-review revisá este servidor MCP y proponé tests de abuso de herramientas.
$security-review enseñame seguridad de agentes de IA con un cuestionario.
```

La skill adapta su trabajo al pedido: revisión, desarrollo acompañado, estudio o una combinación. Consulta la versión estable vigente de OWASP y las guías pertinentes. En revisión, analiza el commit indicado (o `HEAD`) y continúa con los siguientes commits que el agente crea u observa en ese proyecto, manteniendo el seguimiento por SHA. Cada nueva invocación puede apuntar a otro repositorio.

Entrega evidencia, severidad, categoría OWASP, corrección propuesta y validación para cada hallazgo. Aplica técnicas de revisión y pruebas al código; las modificaciones se realizan cuando la tarea incluye corregirlo.

Durante el desarrollo participa desde el diseño: incorpora controles en el código, explica las decisiones y verifica su comportamiento antes del commit. En estudio propone ejemplos, ejercicios y cuestionarios adaptados al nivel; por defecto pregunta de a una y devuelve una explicación después de cada respuesta. Los cuestionarios no son un requisito para seguir programando.

También ayuda a escribir y ejecutar tests de funcionamiento y de seguridad. En las revisiones indica al desarrollador qué casos faltan, qué deben comprobar y dónde agregarlos. Si está implementando la funcionalidad, agrega las pruebas pertinentes dentro de esa tarea. Distingue siempre los tests ejecutados de los que solo están propuestos.

## Activación y continuidad

La skill queda activa en el contexto de la sesión hasta que se la desactive. Una skill es un conjunto de instrucciones: no recibe eventos de Git por sí sola cuando el agente no está ejecutándose. Para commits externos a la sesión, el agente o la integración que la invoque debe proporcionarle el repositorio y el SHA. Este paquete no instala hooks, servicios ni monitores en el repositorio que contiene la skill.

## Fuentes

Para proyectos de IA también selecciona [referencias específicas de MCP, LLM, agentes y skills](security-review/references/ai-security.md), con sus estados de publicación y casos de prueba. Incluye guías para estudiar y verificar permisos, herramientas, memoria e instrucciones externas.

La referencia verificada el 5 de noviembre de 2026 es [OWASP Top 10:2025](https://top10.owasp.org/2025/). La skill exige volver a comprobar la edición vigente y leer las técnicas pertinentes en fuentes oficiales, sin congelar la revisión en esa edición.
