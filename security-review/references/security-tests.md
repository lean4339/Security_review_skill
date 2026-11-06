# Tests de funcionamiento y de seguridad

Para proyectos con MCP, LLM o agentes, complementar estos casos con [ai-security.md](ai-security.md). Cubrir tanto la tarea legítima del agente como las acciones que no debería poder ejecutar, observando los efectos reales.

## Diseñar pruebas que comprueben comportamiento

Leer las suites y convenciones existentes antes de agregar tests. Elegir el nivel que pueda observar el control real: unidad para una decisión aislada; integración para permisos, persistencia y middleware; extremo a extremo cuando la protección dependa del flujo completo. No reemplazar con un mock el control cuya eficacia se quiere comprobar.

Para cada caso, especificar preparación, actor, acción, resultado esperado y efecto observable. Usar datos sintéticos y entornos locales o de prueba autorizados. Evitar carga destructiva y sistemas productivos; para límites y agotamiento de recursos, preferir umbrales pequeños configurables y simulación controlada.

Un test funcional demuestra que un uso legítimo produce el resultado correcto. Un test de seguridad demuestra que una acción fuera de las reglas no obtiene datos, permisos o efectos indebidos. Una misma prueba puede cubrir ambas propiedades si sus aserciones lo demuestran: no duplicarla solo por la etiqueta.

## Elegir casos según el cambio

| Cambio | Funcionamiento legítimo | Seguridad y aserciones adicionales |
| --- | --- | --- |
| Lectura o modificación de recursos | El propietario obtiene o modifica su recurso. | Otro usuario o tenant no puede hacerlo cambiando el identificador. Comprobar ausencia de datos ajenos y de cambios persistidos; usar el código de rechazo definido por la API. |
| Roles y operaciones administrativas | Un rol autorizado ejecuta la operación. | Un rol inferior, aun autenticado, no puede ejecutarla ni asignarse permisos mediante campos extra. |
| Autenticación y sesiones | Credenciales válidas habilitan el flujo esperado. | Tokens alterados, expirados o revocados se rechazan según el mecanismo implementado; no se crea una sesión ni se realiza la operación protegida. |
| Consultas, plantillas o comandos | Entradas normales producen el resultado previsto. | Entradas que podrían interpretarse como instrucciones se tratan como datos o se rechazan; verificar el efecto real, no solo un código HTTP. |
| Transacciones, pagos o acciones repetibles | Una solicitud válida produce el efecto acordado. | Reintentos, duplicados o concurrencia no violan las invariantes del negocio. Comprobar estado final, contadores o saldos con datos sintéticos. |
| Archivos y rutas | Un archivo permitido se procesa correctamente. | Nombres manipulados, tamaño excesivo o formatos prohibidos no escapan del destino permitido ni dejan archivos o efectos indebidos. |
| Webhooks y entradas firmadas | Un mensaje auténtico se procesa. | Firma ausente o incorrecta y alteración del cuerpo impiden el procesamiento. Probar repetición cuando el protocolo requiera protección contra ella. |
| Dependencias externas y excepciones | La respuesta válida permite completar la operación. | Timeouts y errores no omiten controles, filtran secretos ni dejan una operación parcialmente aplicada; verificar rollback y límites de reintento cuando correspondan. |

Seleccionar solo las filas pertinentes. Contrastar los controles con las fuentes OWASP y la documentación oficial del framework; no inventar requisitos de expiración, códigos de respuesta o reglas de negocio para hacer que una prueba pase.

## Indicación concreta para quien desarrolla

Ejemplo didáctico, que debe adaptarse a los archivos y convenciones del proyecto:

> Agregá tests de seguridad además de los de funcionamiento para modificar pedidos. Ya verificamos que el propietario puede editar. Falta probar que el usuario B no puede modificar el pedido de A cambiando el ID, y que el pedido permanece intacto después del rechazo. Ubicalo en la suite de integración del endpoint.

Si no se comprobó la cobertura existente, no decir «ya verificamos». Si el agente tiene a cargo la implementación, convertir esta indicación en tests y ejecutarlos.

## Comprobar que el test es útil

- Verificar que pasa por la ruta o función relevante y que sus aserciones detectan la infracción, incluso si el servidor devuelve un error después de producir un efecto indebido.
- Para una regresión, demostrar que falla con el defecto anterior cuando se pueda hacerlo de forma aislada sin cambiar el árbol de trabajo del usuario. Si no se hizo esa comparación, declararlo.
- Mantener casos deterministas: controlar tiempo, datos y servicios externos cuando sea apropiado; no simular justamente la autorización o validación que se está probando.
- Ejecutar las suites pertinentes y registrar el resultado real. Si faltan dependencias o servicios, explicar el impedimento y dejar el comando reproducible; no contar un test escrito como aprobado.

En modo estudio, pedir al usuario que proponga primero un caso de abuso o una aserción y explicar luego qué detecta el test. En modo implementación, escribir y verificar las pruebas sin convertir el cuestionario en un bloqueo.
