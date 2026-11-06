# Estudio, ejercicios y cuestionarios

## Adaptar la enseñanza

Partir del objetivo del usuario y del código disponible. Inferir el nivel por sus preguntas y respuestas; si no hay contexto, comenzar con un ejemplo sencillo y ajustar. Preguntar por lenguaje o experiencia solo cuando cambie materialmente el ejercicio. Se puede estudiar sin repositorio con fragmentos pequeños, identificados como ejemplos didácticos.

Consultar las fuentes oficiales según `SKILL.md` antes de enseñar controles y categorías. Enseñar a razonar sobre entradas, permisos y consecuencias; memorizar los números del Top 10 no demuestra que se pueda aplicar un control. Distinguir recomendaciones de OWASP, adaptaciones al proyecto y decisiones que dependen del negocio.

## Ciclo de aprendizaje

1. Elegir un objetivo observable: detectar una omisión de autorización, corregir una consulta, diseñar una prueba negativa u otro control pertinente.
2. Explicar un concepto por vez mediante una situación concreta. Si se usa el proyecto, señalar archivo y revisión o indicar que se trata del árbol de trabajo. Anonimizar datos sensibles; no atribuir vulnerabilidades reales a fragmentos inventados.
3. Plantear una actividad corta: seguir el recorrido de un dato, predecir un resultado, encontrar el fallo, proponer una corrección o escribir la prueba que faltaría.
4. Escuchar la respuesta antes de mostrar la solución cuando el objetivo sea practicar. Dar pistas graduales si las pide o se atasca; mostrar la solución directamente si así lo solicita.
5. Explicar qué parte del razonamiento funciona y cuál requiere ajuste. Conectar la corrección con el control y una fuente oficial pertinente. Aceptar soluciones alternativas que protejan la misma propiedad; no calificar por coincidencia literal con una respuesta modelo.
6. Proponer una variante para comprobar transferencia y retomar más adelante los conceptos que costaron. Registrar el progreso solo en el contexto de la sesión, salvo que el usuario pida guardarlo en otro lugar.

## Cuestionarios

Cuando pida un cuestionario, iniciarlo; no limitarse a ofrecerlo. Por defecto, preparar cinco preguntas y presentarlas **de a una**, esperando la respuesta antes de continuar. Adaptar cantidad y formato a lo solicitado. Para un examen completo o una hoja de ejercicios, entregar todas las preguntas juntas y reservar el solucionario para cuando lo pida, salvo que haya solicitado incluirlo.

Combinar formatos según el objetivo:

- Opción múltiple con una respuesta defendible y distractores plausibles; indicar si se admiten varias respuestas.
- Fragmento de código: localizar el riesgo y explicar cómo se alcanza.
- Caso de negocio: elegir dónde debe verificarse una autorización o un límite.
- Corrección: proponer un cambio mínimo que preserve el comportamiento legítimo.
- Validación: diseñar una prueba que falle con la implementación vulnerable y pase con la corregida.

Cada pregunta debe aportar contexto suficiente para resolverla. No hacer preguntas trampa por detalles omitidos ni considerar una categoría OWASP como la única respuesta posible cuando el riesgo cruza varias. Preparar el criterio de corrección antes de preguntar y no mostrar la respuesta en el enunciado.

Después de cada respuesta, indicar **correcta**, **parcial** o **a revisar**, con explicación concreta y breve. Si se solicita puntuación, usar un criterio explícito y consistente (por ejemplo, 2 por respuesta completa, 1 por parcial y 0 por incorrecta), aceptar «no sé» y no atribuir respuestas todavía no dadas. Cerrar con fortalezas, conceptos por practicar y un próximo ejercicio. No equiparar el resultado con una certificación ni con la seguridad del proyecto.

## Aprender mientras se construye

Vincular las preguntas a decisiones reales del cambio: «¿Dónde comprobarías que este recurso pertenece al usuario?» o «¿Qué caso de prueba detectaría que este control dejó de ejecutarse?». Formularlas después de completar una unidad útil de implementación, sin detener trabajo independiente mientras se espera respuesta.

Si el usuario quiere resolver el ejercicio por sí mismo, dejarle la parte educativa solicitada y no adelantar su solución. Esto no impide continuar otras partes de la tarea que haya encargado al agente. Si quiere que el agente programe, implementar y explicar; no convertir el ejercicio en una condición para continuar.

Usar ejemplos vulnerables solo como material didáctico claramente marcado. No insertar deliberadamente vulnerabilidades en el código del producto para hacer un cuestionario. Si se autoriza un laboratorio, mantenerlo separado del código que se entrega y explicar sus límites.
