# Fuentes y técnicas OWASP

Última comprobación de esta referencia: 2026-11-05. La edición estable de aplicaciones web era **OWASP Top 10:2025**. Verificar la edición al revisar; usar los identificadores de la edición efectivamente consultada.

Para MCP, LLM, agentes y skills, consultar [ai-security.md](ai-security.md). Son marcos complementarios con versiones y estados propios.

## Fuentes que se deben leer

- [Proyecto Top 10](https://owasp.org/www-project-top-ten/): comprobar la edición estable vigente y seguir desde allí los enlaces de categorías.
- [Top 10:2025](https://top10.owasp.org/2025/): punto de partida verificado para las categorías de esta referencia.
- [Secure Code Review Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secure_Code_Review_Cheat_Sheet.html): consultar metodología de revisión del diff, flujos de datos y lógica de negocio.
- [Índice de Cheat Sheets](https://cheatsheetseries.owasp.org/IndexAlphabetical.html): seleccionar y leer guías de autorización, inyección, sesiones, criptografía, dependencias, logging o manejo de errores según el cambio.
- [Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/): elegir casos de prueba pertinentes y citar su versión. En la comprobación inicial, 4.2 era la versión publicada y 5.0 estaba en desarrollo.

El [índice de Cheat Sheets por Top 10](https://cheatsheetseries.owasp.org/IndexTopTen.html) todavía mapeaba categorías de 2021 al comprobarlo. Sus guías siguen siendo útiles, pero no copiar esos números como si fueran de 2025. Leer las guías enlazadas y mapear por el riesgo real.

## Guía de selección para 2025

Esta tabla es una orientación de revisión del proyecto, no una reproducción del estándar ni un reemplazo de sus páginas. Leer la categoría y las guías aplicables para ajustar los controles al framework y al flujo real.

| Categoría | Qué investigar en el cambio | Verificación concreta según el contexto |
| --- | --- | --- |
| A01:2025 Broken Access Control | Acceso a objetos de otro usuario o tenant, roles, controles del servidor, CSRF y destinos de solicitudes salientes. | Probar el mismo recurso con identidades y permisos diferentes; seguir el control hasta la operación protegida. |
| A02:2025 Security Misconfiguration | Valores predeterminados, debug, exposición de servicios, CORS y permisos de infraestructura. | Contrastar configuración efectiva con el entorno previsto; comprobar qué ve un cliente sin privilegios. |
| A03:2025 Software Supply Chain Failures | Dependencias resueltas, origen de artefactos, permisos de CI y pasos de construcción. | Leer lockfiles y workflows, verificar avisos oficiales aplicables y entradas controlables por contribuciones externas. |
| A04:2025 Cryptographic Failures | Datos sensibles, transporte, almacenamiento, contraseñas, claves y aleatoriedad. | Trazar la vida del dato y comprobar las primitivas y configuraciones usadas, sin mostrar secretos. |
| A05:2025 Injection | SQL/NoSQL, comandos, plantillas, HTML, rutas y entradas interpretadas como instrucciones. | Seguir la entrada hasta el intérprete; verificar parametrización y codificación específica del contexto. |
| A06:2025 Insecure Design | Invariantes de negocio, límites, abuso, concurrencia y confianza entre componentes. | Diseñar un caso de abuso del flujo modificado; comprobar operaciones repetidas, fuera de orden o concurrentes. |
| A07:2025 Authentication Failures | Inicio de sesión, recuperación, MFA, tokens, sesiones y cierre de sesión. | Revisar expiración, revocación, rotación y rutas alternativas con credenciales inválidas o vencidas. |
| A08:2025 Software or Data Integrity Failures | Datos serializados, actualizaciones, webhooks y artefactos que se aceptan como confiables. | Comprobar autenticidad antes del uso y respuesta ante datos alterados o repetidos cuando corresponda. |
| A09:2025 Security Logging and Alerting Failures | Eventos relevantes, alertas, trazabilidad, secretos y datos controlados por el atacante en logs. | Seguir un rechazo o acción sensible hasta su registro; comprobar que permite investigar sin filtrar credenciales. |
| A10:2025 Mishandling of Exceptional Conditions | Excepciones, agotamiento de recursos, fallos parciales, reintentos y estados inconsistentes. | Evaluar rutas de timeout y error; verificar limpieza, límites, rollback y denegación segura. |

## Evidencia y cobertura

Una búsqueda de patrones sirve para localizar candidatos. Antes de informar un problema, comprobar alcanzabilidad, controles previos, configuración relevante y efecto del cambio. Una prueba negativa debe poder diferenciar el control correcto del vulnerable.

Registrar para cada categoría si se revisó, no aplica o no se pudo verificar, con una razón breve. No rellenar el informe con recomendaciones genéricas: cada hallazgo debe conectar una línea o configuración del commit con una consecuencia concreta.
