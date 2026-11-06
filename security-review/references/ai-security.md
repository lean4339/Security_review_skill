# OWASP para MCP, LLM, agentes y skills

Consulta inicial: 2026-11-05. Estas referencias amplían la revisión, el desarrollo y el estudio cuando el objetivo incluya IA. Comprobar su estado al usarlas y leer las secciones pertinentes; no asumir que todas las publicaciones OWASP tienen la misma madurez.

## Selección de fuentes

| Componente | Fuente oficial | Estado observado y uso |
| --- | --- | --- |
| Servidor o cliente MCP | [MCP Top 10](https://owasp.org/projects/mcp-top-10) | Identificadores MCP01–MCP10 de 2025; su roadmap indica beta y pruebas piloto, aunque la ficha del proyecto diga Production. Usar como catálogo de riesgos del ecosistema MCP. |
| Agente que planifica y ejecuta acciones | [Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | Recurso publicado el 9 de diciembre de 2025 para la edición 2026. Cubre objetivos del agente, herramientas, identidad, memoria y coordinación. |
| Aplicación con LLM o recuperación de contexto | [GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) | La página publica la edición 2026. El PDF descargable aún tiene marcadores de fecha editorial: registrar esa inconsistencia si se cita la fecha del documento. Leer su taxonomía, sin reutilizar números de 2025. |
| Paquetes de skills, cargadores y scripts | [Agentic Skills Top 10](https://owasp.org/projects/agentic-skills-top-10) | Ficha 1.0-2026, proyecto en incubación. Su [sitio](https://owasp.github.io/www-project-agentic-skills-top-10/) también declara desarrollo activo. Orienta la revisión de esta capa; no implica que sus propuestas de formato sean requisitos de Codex u otros agentes. |

Leer además las guías prácticas según el caso:

- [MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html): contratos de herramientas, transporte, aislamiento y permisos.
- [AI Agent Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html): ejecución, memoria, coordinación y validación adversarial.
- [Secure Coding with AI](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html): dependencias sugeridas, instrucciones del repositorio y evidencia de tests generados por IA.

## Aplicación a MCP

Separar host, cliente, servidor y servicio final. Revisar identidad y permisos en el punto de ejecución, alcance de tokens y aislamiento entre servidores. Inspeccionar entradas, resultados y definiciones completas de herramientas: sus anotaciones no hacen cumplir permisos. El transporte stdio tampoco limita por sí solo el acceso del proceso al equipo.

Para HTTP/OAuth, contrastar los controles con la revisión del protocolo implementada, incluyendo destinatario del token y validación de origen cuando corresponda. No exigir firmas por mensaje como requisito universal de MCP. Un hash de definición puede detectar cambios de metadatos, pero no garantiza que el servidor conserve su comportamiento.

Fuente de estos criterios: [MCP Security](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html). Las siguientes son adaptaciones para probar el proyecto:

- Ejecutar una operación permitida y repetirla con identidad sin alcance: debe rechazarse sin efectos.
- Cambiar parámetros o anotaciones de una herramienta de prueba: comprobar cómo se detecta y trata el cambio de confianza.
- Introducir instrucciones en una respuesta de herramienta: verificar que no habiliten otra herramienta ni filtren un secreto sintético.

## Aplicación a agentes y LLM

Separar las propuestas del modelo de los controles que autorizan su ejecución. Revisar permisos efectivos, límites de pasos y reintentos, aislamiento de memoria, destinos de datos y delegación. Cuando el producto use aprobaciones para acciones sensibles, comprobar que cubran la acción y los argumentos reales y que no puedan reutilizarse fuera de su alcance. Estas verificaciones del producto no agregan pedidos de aprobación a la tarea actual.

Fuente: [AI Agent Security](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html). Casos de prueba adaptados:

- Documento recuperado que intenta cambiar la tarea: no debe producir una llamada prohibida.
- Memoria del usuario A seguida de una consulta de B: no deben cruzarse datos privados.
- Acción con argumentos alterados después de autorizarla: no debe ejecutarse bajo esa autorización.
- Herramienta que falla repetidamente: el agente debe respetar el límite configurado.

No basta con que el modelo responda «no puedo»: observar llamadas, argumentos y efectos. Separar tests deterministas de permisos y validación de las evaluaciones del comportamiento del modelo. En estas últimas, registrar versión, configuración, casos, repeticiones y fallos observados; una ejecución exitosa no demuestra inmunidad a inyección. Los fixtures y destinos deben ser de prueba y sin secretos reales.

## Código y tests producidos por IA

Contrastar paquetes y APIs sugeridos con fuentes oficiales antes de incorporarlos. Inspeccionar cambios en instrucciones persistentes y tests eliminados o debilitados. Ejecutar las pruebas: una respuesta que afirma haberlas ejecutado no es evidencia. Revisar que las aserciones comprueben el requisito y no reproduzcan el defecto del código generado.

Fuente: [Secure Coding with AI](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Coding_with_AI_Cheat_Sheet.html). Para controles críticos, indicar qué verificación independiente se realizó o sigue pendiente; no asumir independencia porque el mismo agente relea su resultado, ni lanzar otros agentes automáticamente.

## Enseñanza y mapeo

Usar casos del proyecto para practicar quién controla cada dato, quién decide los permisos y qué observación demuestra un bloqueo. Adaptar los cuestionarios de `learning.md`: por ejemplo, distinguir una instrucción en un documento de una autorización para ejecutar una herramienta.

Identificar cada hallazgo con marco y edición comprobados. Por ejemplo, el PDF LLM 2026 ubica la agencia excesiva en LLM03 y el manejo indebido de salidas en LLM10; no conservar los números de 2025. Si solo se leyó la página de presentación, consultar la categoría antes de asignar un identificador detallado.
