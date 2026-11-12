# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona es un conjunto de 14 habilidades para trabajar en producto e ingeniería con agentes de
programación. Cada habilidad cubre una responsabilidad, como especificar, implementar o revisar
un cambio. Todas siguen los mismos ocho principios del ciclo, mantienen registros en
`docs/lusona/` del proyecto y terminan cada respuesta de trabajo con el estado, las evidencias
y la siguiente acción.

Para Claude Code, Codex, [Cursor](INSTALL.md#cursor), [agentes de programación de Xcode 27](INSTALL.md#xcode) y [Google Antigravity App, CLI e IDE](INSTALL.md#antigravity) · Versión del código fuente de esta copia de trabajo: **3.0.0**

> [!WARNING]
> No instales Lusona con Vercel Skills (`npx skills@latest`); usa la [instalación como plugin nativo](#instalación).

Por qué creamos Lusona Skills: [Why we built Lusona Skills](https://blog.lusona.com/blog/why-we-built-lusona-skills/).

Este README describe el código fuente de esta copia de trabajo. La instalación desde GitHub
usa el código incluido en commits y enviado al repositorio remoto; los cambios locales no
constituyen una versión publicada.

![Ciclo de trabajo de Lusona, principios y grupos de habilidades](plugins/lusona/assets/workflow-loop.svg)

El círculo muestra cómo continúa el trabajo: elegir, actuar, comprobar y repetir. Elige las
habilidades según la necesidad actual; cualquier habilidad puede seguir a otra.

## Índice

- [Principios del ciclo](#principios-del-ciclo)
- [Empezar y elegir una habilidad](#empezar-y-elegir-una-habilidad)
- [Autoridad y nivel de TDD](#autoridad-y-nivel-de-tdd)
- [Decisiones y revisiones](#decisiones-y-revisiones)
- [Evidencias y finalización](#evidencias-y-finalización)
- [Registros y reanudación](#registros-y-reanudación)
- [Respuestas y siguientes acciones](#respuestas-y-siguientes-acciones)
- [Instalación](#instalación)
- [Referencias](#referencias)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Desarrollo](#desarrollo)

## Principios del ciclo

El ciclo es la forma de trabajar de todas las habilidades: elegir la siguiente acción de alcance
acotado, ejecutarla, comprobar el resultado y repetir hasta alcanzar el resultado solicitado.
Su propósito es refinar el sistema y el diseño a medida que aumenta la comprensión. Todas las
habilidades aplican estos ocho principios, definidos en la
[guía del flujo de trabajo](plugins/lusona/references/workflow-guide.md#loop-principles).

| ID | Principio | Qué significa para ti |
| --- | --- | --- |
| P1 | Sin secuencia fija | El agente elige la siguiente habilidad según la necesidad pendiente. Cualquier habilidad puede seguir a otra, y cada cambio usa solo las habilidades que necesita el trabajo sin resolver. |
| P2 | Refinamiento | Cada iteración compara su resultado con el resultado previsto y distingue los hechos de los supuestos. Transmite a la siguiente iteración el resultado, las decisiones aceptadas, la autoridad, el nivel de TDD, las evidencias y la incertidumbre. |
| P3 | Las decisiones previas son datos de entrada | Cuando una nueva aportación contradice una decisión aceptada, el agente no rechaza la aportación ni ignora la decisión. Expone el conflicto y reconsidera la decisión contigo. |
| P4 | Invalidación registrada | Una decisión sustituida se marca con la fecha y la fuente, y conserva su justificación. Se actualizan los registros afectados para que concuerden, y un registro desactualizado no puede restablecer una elección sustituida. |
| P5 | Evidencias antes que afirmaciones | El agente solo afirma un comportamiento o la finalización a partir de comprobaciones observadas. Una comprobación obligatoria fallida o sin ejecutar impide dar el trabajo por terminado. |
| P6 | La autoridad sigue siendo del usuario | Las especificaciones, los planes, los ADR y los estados de la cola no autorizan la implementación. Cambiar los resultados aceptados, los contratos, el nivel de TDD o los compromisos de consecuencias importantes requiere tu decisión. |
| P7 | Continuar el trabajo acotado | El agente ejecuta la siguiente acción autorizada sin otro comando, deja de indagar cuando las respuestas no pueden cambiar la siguiente acción y pausa solo el trabajo afectado. |
| P8 | Cada respuesta indica la siguiente acción | Cada respuesta de trabajo termina con una siguiente acción y su responsable, o indica que no queda ninguna y por qué. |

## Empezar y elegir una habilidad

Empieza por **status** cuando te incorporas a un proyecto, reanudas el trabajo o decides qué
requiere atención. Evalúa los registros y las evidencias que puede leer, enumera todo el trabajo
pendiente conocido y recomienda la siguiente acción. También sirve cuando el proyecto aún no
tiene registros de Lusona. Pedir el estado no concede ni retira la autoridad para ejecutar.

Elige la habilidad que responda a la necesidad actual (P1). Las filas no forman una secuencia:
una petición autorizada con comportamiento y alcance definidos pasa a **implement** sin **specify**.

| Habilidad | Cuándo usarla |
| --- | --- |
| [status](plugins/lusona/skills/status/SKILL.md) | Quieres orientación, conocer el progreso, saber qué queda o cómo reanudar |
| [explore](plugins/lusona/skills/explore/SKILL.md) | Quieres razonar sobre una dirección, opción o futuro antes de elegir |
| [frame-product](plugins/lusona/skills/frame-product/SKILL.md) | El público, el problema, la visión, los resultados o los límites de un producto están sin definir o cambian |
| [map-capabilities](plugins/lusona/skills/map-capabilities/SKILL.md) | Hay que aclarar la cobertura de capacidades, las dependencias o el orden de entrega |
| [specify](plugins/lusona/skills/specify/SKILL.md) | Hay que definir el comportamiento previsto, el alcance o los criterios de aceptación de un cambio |
| [architect](plugins/lusona/skills/architect/SKILL.md) | Está pendiente una decisión técnica sobre límites, contratos o responsabilidades con consecuencias duraderas |
| [design](plugins/lusona/skills/design/SKILL.md) | Hay que ver una pantalla, un flujo, un estado o una relación para evaluarlos o elegir |
| [implement](plugins/lusona/skills/implement/SKILL.md) | Un cambio está autorizado para su implementación, o solo quieres un plan |
| [review](plugins/lusona/skills/review/SKILL.md) | Hay que revisar un diff frente al comportamiento previsto antes de terminar |
| [refactor](plugins/lusona/skills/refactor/SKILL.md) | El código existente tiene un problema estructural concreto y debe conservar su comportamiento |
| [investigate](plugins/lusona/skills/investigate/SKILL.md) | Hace falta evidencia sobre una causa, un comportamiento observado o la viabilidad |
| [measure](plugins/lusona/skills/measure/SKILL.md) | Una decisión requiere una línea base, un benchmark u observaciones comparables |
| [experiment](plugins/lusona/skills/experiment/SKILL.md) | Hace falta un ensayo para decidir si adoptar, rechazar o refinar un enfoque |
| [batch](plugins/lusona/skills/batch/SKILL.md) | Autorizas trabajo sin supervisión sobre elementos seleccionados de la cola, o continúas un lote registrado |

La [guía del flujo de trabajo](plugins/lusona/references/workflow-guide.md) enumera el perfil y el
resultado de cada habilidad, la tabla de selección y la terminología. Pasar de una habilidad
a otra no requiere una nueva aprobación, y no necesitas dirigir cada transición.

Invoca una habilidad en la aplicación que utilizas:

- Claude Code: `/lusona:<skill>`, por ejemplo `/lusona:status`.
- Codex: selecciona la habilidad de Lusona en la interfaz de habilidades.
- Cursor: escribe `/` en el chat de Agent y selecciona la habilidad.
- Xcode: escribe `/` en una conversación con el agente y selecciona la habilidad instalada.
- Antigravity App y CLI: `/<skill>`, por ejemplo `/status`. En el IDE independiente, consulta
  **Customizations** y nombra la habilidad de Lusona en tu petición.

[Instala Lusona](#instalación) antes de usar estas habilidades. Una petición indica la habilidad,
el resultado o el registro de entrada y el alcance autorizado. Por ejemplo:

> **status:** Evalúa este proyecto a partir de los registros disponibles y del árbol de trabajo.
> Dime qué queda pendiente y recomienda por dónde empezar.

> **explore:** Ayúdame a comparar los enlaces de invitación con las invitaciones solo por correo
> electrónico. Explica las consecuencias para nuestro equipo de soporte antes de elegir. Mantén
> esta conversación en el chat; no guardes archivos.

> **design:** Compara dos flujos de invitación usando nuestras pantallas, navegación y textos
> existentes. Muestra los pasos y el estado de invitación caducada, y explica las ventajas e
> inconvenientes de cada opción. Limita el trabajo al diseño visual; no implementes la interfaz.

> **implement:** Añade la caducidad de las invitaciones a los siete días. Conserva las invitaciones
> ya aceptadas. El trabajo estará completo cuando se rechacen las invitaciones de más de siete días,
> las invitaciones aceptadas permanezcan sin cambios y pase la batería de pruebas. Usa el nivel
> de TDD `targeted` para el límite de caducidad. Verifica en local; no despliegues.

## Autoridad y nivel de TDD

Tú mantienes la autoridad (P6). Estas reglas se aplican a todas las habilidades:

- Las especificaciones, los planes, los ADR y los estados de la cola no autorizan la implementación.
  Tampoco la autorizan una conversación ni una revisión de solo lectura.
- Seleccionar una tarea para implementarla no autoriza el resto del cambio al que pertenece.
- El agente te pregunta antes de realizar acciones destructivas y antes de cambiar los resultados
  aceptados, los contratos, el nivel de TDD o los compromisos de consecuencias importantes.
- El agente solo hace commits, push o publicaciones con tu autorización. La implementación y la
  refactorización autorizadas incluyen commits locales.
- Una petición a **implement** limitada a la planificación termina con una propuesta de enfoque
  y no autoriza la implementación.
- **batch** solo ejecuta trabajo sin supervisión sobre una selección fija de elementos de la cola
  que autorices expresamente. Usa como máximo 4 asignaciones simultáneas, o 5 si seleccionas 5,
  dentro de la capacidad de la aplicación, y un presupuesto de reparación de 2 rondas de corrección
  por elemento, salvo que concedas otro número.

La implementación requiere un nivel de TDD elegido expresamente. No hay un valor predeterminado.

| Nivel de TDD | Requisito |
| --- | --- |
| `none` | No exige escribir primero las pruebas; siguen vigentes la verificación acordada y las comprobaciones del repositorio |
| `targeted` | Escribir primero las pruebas de los comportamientos indicados |
| `strict` | Escribir primero las pruebas de cada comportamiento comprobable nuevo o modificado |

Elige el nivel en tu petición o como preferencia permanente en `docs/lusona/README.md` del
proyecto o en las instrucciones para agentes (`CLAUDE.md` o `AGENTS.md`), por ejemplo
`TDD: targeted for validation and persistence boundaries`. Hasta que elijas un nivel, el agente
solo define y planifica, y después te pregunta y recomienda un nivel. Registra el nivel y su
fuente, y te pide revisarlo cuando la secuencia elegida no sea viable.

Dentro de esa autoridad, el agente continúa sin otro comando (P7). Ejecuta la siguiente acción
acotada, realiza una medición o un experimento dentro del trabajo autorizado sin una nueva
petición y deja de preguntar cuando las respuestas no pueden cambiar la siguiente acción.
Usa la herramienta de preguntas propia de la aplicación cuando está disponible, recomienda una
respuesta y no considera el silencio ni una opción preseleccionada como consentimiento. Durante
la espera, solo se pausa el trabajo afectado y el agente indica qué permite reanudarlo.

El agente que habla contigo es el coordinador. Delega el trabajo especializado en agentes
subordinados para tareas de cualquier tamaño, e integra y verifica sus resultados. Si la
delegación está prohibida o no está disponible, trabaja por su cuenta y lo indica. Consulta
[delegación](plugins/lusona/references/delegation.md) para las asignaciones y la
[selección de modelos](plugins/lusona/references/delegation.md#model-routing).

## Decisiones y revisiones

Las decisiones aceptadas son datos de entrada para el trabajo posterior (P3). Cuando un nuevo
requisito, especificación, medición o resultado experimental contradice una decisión aceptada,
el agente:

1. Expone la decisión, su fuente, el conflicto y los supuestos afectados, tanto en la respuesta
   como en el registro correspondiente.
2. Te presenta las opciones y una respuesta recomendada.
3. Acuerda contigo uno de estos resultados: mantener, revisar en parte o sustituir la decisión.
   Reconsiderar una decisión no autoriza el cambio.
4. Registra el resultado antes de continuar el trabajo que depende de la decisión.
5. Continúa el trabajo no afectado por el conflicto, dentro de la autoridad existente.

El registro conserva el historial de cada decisión (P4). Una decisión revisada o sustituida
conserva su texto y justificación, con la fecha y la fuente de tu respuesta; una decisión
sustituida enlaza a su reemplazo. El agente actualiza los registros dependientes, las asignaciones
y los traspasos dentro de su responsabilidad de escritura, informa de las correcciones que deben
hacer otros responsables y reanuda según la revisión. Si un registro aún contiene una decisión
sustituida, se corrige o se comunica; no se sigue. Consulta las
[revisiones](plugins/lusona/references/revisions.md).

Una petición posterior cambia el alcance del objetivo actual y conserva su progreso. Solo
sustituye el objetivo cuando lo cancela o reemplaza expresamente, o pide otro incompatible.

## Evidencias y finalización

El agente solo informa del comportamiento a partir de comprobaciones observadas e indica las
comprobaciones fallidas o sin ejecutar (P5). La finalización requiere el resultado autorizado,
sus criterios, las comprobaciones obligatorias aprobadas y cualquier aceptación humana requerida.
Que las pruebas pasen no demuestra la aceptación humana.

- **Evidencias de pruebas previas al código.** Para cada comportamiento que exige pruebas primero,
  el agente observa el fallo previsto antes de cambiar el código de producción y después el
  resultado satisfactorio. Un fallo de configuración no demuestra el fallo previsto. Consulta
  [TDD](plugins/lusona/references/tdd.md).
- **Límites de corrección.** Tras 2 rondas consecutivas de corrección sin progreso sustancial,
  el agente deja de corregir ese fallo, informa de las evidencias y continúa el trabajo no afectado.
  Tras 4 rondas en total, te pregunta antes de continuar con otra. Dentro de un lote se aplica
  el presupuesto de reparación. Consulta los
  [límites de corrección](plugins/lusona/references/corrections.md).
- **Revisión independiente.** Se requiere la revisión de un agente que no haya escrito el cambio
  cuando lo exigen tus reglas o las del repositorio, o cuando el cambio afecta a límites de
  seguridad, datos persistentes o contratos compartidos, o implica modificaciones coordinadas
  de varios participantes. El trabajo por cuenta propia nunca satisface ese requisito; si la
  revisión no está disponible, el agente lo indica como incumplido.
- **Estudios.** **investigate** responde a preguntas de diagnóstico; **measure** y **experiment**
  son estudios. La incertidumbre por sí sola no inicia un estudio. Un estudio que la petición
  no exige necesita tu autorización expresa o permanente, un alcance finito y un presupuesto
  de recursos. Las evidencias en las que se basa una decisión se guardan en `docs/lusona/evidence/`
  del proyecto. Consulta las [evidencias](plugins/lusona/references/evidence.md).
- **Referencias visuales.** **explore**, **specify**, **architect** y **design** ofrecen 2-4 opciones
  visuales cuando una elección depende de la disposición, la estructura, el flujo o la apariencia.
  Los borradores de interfaz se abren en el navegador o el agente indica la ruta absoluta del
  HTML; los diagramas usan bloques Mermaid. Cuando eliges, la referencia se conserva en
  `docs/lusona/visuals/<record-id>/` con sus requisitos vinculantes. **implement** informa del estado
  de cada requisito vinculante, y **review** indica si se cumple, no se cumple o no se ha comprobado.
  Consulta los [elementos visuales](plugins/lusona/references/visuals.md).

## Registros y reanudación

El agente guarda los resultados sustantivos antes de un traspaso o de la finalización sin que se
lo pidas: decisiones, acuerdos, evidencias, conclusiones, traspasos y síntesis de conversaciones
de las que depende el trabajo posterior. Las explicaciones y los avisos de estado de los que no
depende trabajo posterior no necesitan registro. Si está prohibido guardar, el agente informa
de lo que no se ha guardado.

| Trabajo | Registro en `docs/lusona/` del proyecto |
| --- | --- |
| Un cambio que requiere especificación | `specs/<change-id>.md` y una fila en `work.md` |
| Implementación o refactorización directa sin especificación | `notes/<change-slug>.md` |
| Investigación, medición o experimento | Notas y registros en `evidence/` |
| Decisión de arquitectura con consecuencias importantes | `adr/<YYYYMMDD>-<decision-slug>.md` |
| Definición del producto y mapa de capacidades | `product.md` |
| Lote | `batches/<batch-slug>.md` |

Se requiere una especificación y su fila en la cola en cuatro casos. El tamaño no lo decide.

- La habilidad define cambios en una especificación, como hace **specify**.
- Pides una especificación o seguimiento.
- Ya existe una especificación para el cambio.
- El cambio necesita revisión independiente por lo que afecta.

Los estados de la cola son Ideas, Ready, Doing, Review y Done; ninguno autoriza la implementación.
Icebox es una sección de la cola para las filas aparcadas; una fila aparcada conserva su estado.
Consulta la [cola](plugins/lusona/references/queue.md).

Cada registro responsable mantiene un único traspaso vigente con el objetivo, las decisiones,
la autoridad, el nivel de TDD y su fuente, las evidencias, la incertidumbre, los recuentos de
correcciones, los bloqueos, las responsabilidades y la siguiente acción (P2). Cuando la aplicación
informa del uso de contexto, el agente prepara el traspaso al 40% y lo completa antes del 50%.
Al reanudar, lee los registros conservados y el árbol de trabajo, y solo te pregunta por la
autoridad o por un hecho que cambie la siguiente acción. La autorización se mantiene entre
traspasos. Si una interrupción repentina impide guardar, el agente no afirma haber creado un
punto de recuperación. Los registros de versiones anteriores del plugin siguen siendo válidos
y se actualizan en su lugar. Consulta la [conservación](plugins/lusona/references/retention.md)
y los [archivos](plugins/lusona/references/files.md).

Para reanudar, usa **status** para evaluar lo que queda o nombra el trabajo que quieres continuar:

> Continúa investigando la caducidad de las invitaciones a partir de las conclusiones guardadas.
> Comprueba la reproducción conservada con la compilación actual. No cambies el comportamiento
> en producción.

## Respuestas y siguientes acciones

Cada respuesta de trabajo termina con el mismo formato (P8); los saludos y acuses de recibo no.
El estado es **✅ Completado** (alcance solicitado cumplido), **🔄 En curso** (continúa el trabajo
autorizado), **❓ Requiere información** (falta un requisito previo) o **⏸ En pausa** (el trabajo
afectado espera un requisito indicado). El estado describe la respuesta, no el estado de la cola.
Ejemplo hipotético de respuesta; no demuestra que se haya realizado el trabajo:

> **Result:** ❓ Requiere información: Elige el nivel de TDD antes de empezar la implementación.
> La especificación y los criterios de aceptación están registrados.
>
> **Evidence:** No se han ejecutado comprobaciones; el cambio está definido, no implementado.
>
> | Next action | Owner | Needs | Authority |
> | --- | --- | --- | --- |
> | Elegir `none`, `targeted` o `strict`; se recomienda `targeted` para el cambio del parser | usuario | La especificación registrada | Nivel de TDD sin seleccionar |

- El responsable es el usuario, el coordinador o una habilidad con nombre. La columna Authority
  dice `Authorized` o indica la autoridad que falta.
- Una decisión o aprobación bloqueante aparece primero. La respuesta añade **Decisions:** cuando
  ha tomado una decisión de consecuencias importantes, y **Open issues:** cuando quedan asuntos pendientes.
- Cuando el alcance está completo y un trabajo posterior sirve al resultado acordado, la
  respuesta lo propone e indica la autoridad que falta. Cuando no queda ninguna acción, dice
  `**Next action:** None for this request` y explica el motivo en una frase.
- Una instrucción para continuar en otra sesión va en una cita debajo de la tabla.
- Tus instrucciones de formato y las restricciones de la aplicación tienen prioridad sobre el
  formato; se mantienen el resultado, las evidencias, el estado y la siguiente acción. Consulta
  los [ejemplos de finalización](plugins/lusona/references/completion.md).

## Instalación

Elige la aplicación que utilizas. Instala desde el repositorio público
[lusona/ai-skills](https://github.com/lusona/ai-skills) por HTTPS; no necesitas credenciales
de GitHub para descargarlo.

### Antigravity

Instala directamente desde GitHub:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
```

La URL instala Lusona desde el manifiesto de la raíz del repositorio. Para la App y el IDE
independiente, consulta **Customizations** tras esta instalación global con la CLI. La
[guía de instalación de Antigravity](INSTALL.md#antigravity) incluye copias locales, paquetes
portátiles, actualizaciones, eliminación y límites de verificación. Registra una comprobación
de instalación desde GitHub con Antigravity CLI 1.4.12 en Linux para Lusona 1.4.0; no se ha
probado el comportamiento interactivo en App e IDE.

### Claude Code

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

### Codex

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

### Cursor

Abre **Customize > From GitHub Repository**, introduce `https://github.com/lusona/ai-skills`
e instala **Lusona Skills** para tu proyecto o usuario. En el chat de Agent, escribe `/`
para encontrar las habilidades de Lusona. Consulta los [pasos de instalación en Cursor](INSTALL.md#cursor)
para ver los enlaces a la documentación actual de Cursor y el estado de las pruebas.

### Xcode

En Xcode 27, abre **Settings > Intelligence > Agents > Plug-ins > Add Plug-in**.
Elige **Add from URL**, introduce `https://github.com/lusona/ai-skills` y selecciona las
habilidades de Lusona que quieras instalar. Consulta los [pasos de instalación en Xcode](INSTALL.md#xcode)
para conocer la configuración, las importaciones locales y los detalles de versión.

Tras instalar, inicia una sesión nueva en tu proyecto. Para instalar desde una copia de trabajo
local, usar paquetes portátiles, actualizar o desinstalar, consulta la
[guía de instalación](INSTALL.md). Elige una sola fuente del catálogo: copia de trabajo local o GitHub.

## Referencias

- [Historial de cambios](CHANGELOG.md)
- [Instalación y desinstalación](INSTALL.md)
- [Política de privacidad](PRIVACY.md)
- [Condiciones de uso](TERMS.md)
- [Catálogo del plugin: habilidades, referencias y plantillas](plugins/lusona/README.md)
- [Principios del ciclo, habilidades, selección y terminología](plugins/lusona/references/workflow-guide.md)
- [Nivel de TDD y verificación](plugins/lusona/references/tdd.md)
- [Coordinación de lotes](plugins/lusona/skills/batch/SKILL.md)
- [Registros, conservación y traspaso](plugins/lusona/references/retention.md)
- [Cierre y reapertura](plugins/lusona/references/closeout.md)
- [Delegación](plugins/lusona/references/delegation.md)
- [Conversaciones para aclarar la intención](plugins/lusona/references/interviews.md)

## Contribuir

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para conocer el alcance de las contribuciones, las
comprobaciones locales y las pull requests. Usa los
[formularios de errores y solicitudes de funciones](https://github.com/lusona/ai-skills/issues/new/choose)
para informar de problemas o proponer mejoras. El equipo `@lusona/core` se encarga de la revisión del repositorio.

## Licencia

Las habilidades, plantillas, documentación y scripts están disponibles bajo la [licencia MIT](LICENSE).

## Desarrollo

Los archivos fuente oficiales del flujo de trabajo están en `plugins/lusona/`. Cada proyecto que
utiliza el plugin guarda sus propios datos en su `docs/lusona/`; la estructura de una cola vacía
está en `plugins/lusona/templates/work.md.template`.

Los scripts auxiliares para los registros del plugin usan Bash o PowerShell
([requisitos de ejecución](INSTALL.md#requirements)). Python 3 solo es necesario para crear
paquetes y ejecutar evaluaciones en Python, no para usar el plugin.

```bash
claude plugin validate plugins/lusona
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package.py
```

El generador de paquetes comprueba los nombres y versiones de los manifiestos nativos, los
enlaces, las rutas del catálogo y la selección de archivos. Todos los manifiestos nativos deben
usar la misma versión. Escribe en `tmp/lusona-package/` dentro del repositorio y se niega a
sobrescribir un directorio de salida existente; usa `--output tmp/<new-directory>` para otra
compilación. Ni la instalación ni la creación de paquetes inicializan los registros del proyecto.

Las reglas para todas las tareas y el formato de respuesta de cada `SKILL.md` se generan desde
el directorio `shared/` del repositorio. Edítalos allí y ejecuta
`python3 scripts/sync_shared.py --source shared
plugins/lusona`; añade `--check` para verificar sin escribir.
