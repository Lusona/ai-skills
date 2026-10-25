# Lusona AI Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

> [!WARNING]
> No instales Lusona con Vercel Skills (`npx skills@latest`); usa la [instalación como plugin nativo](#installation).

Lusona ayuda a un agente de IA a completar lo que le pides: comprender la solicitud, actuar y
verificar el resultado. Tú defines el resultado, las restricciones y los permisos. El agente
elige la siguiente acción útil según las pruebas disponibles, continúa el trabajo autorizado y
pregunta cuando necesita información o permiso de tu parte.

Para Claude Code, Codex y los [agentes de programación de Xcode 27](plugins/lusona/INSTALL.md#xcode) · Versión del código fuente de esta copia de trabajo: **1.0.0**

Este README describe el código fuente de esta copia de trabajo. La instalación desde GitHub
utiliza el código confirmado mediante commit y enviado al repositorio remoto; los cambios locales
no constituyen una versión publicada.

<a id="index"></a>
## Índice

- [Elegir un comando](#choose-a-command)
- [Empezar por un resultado](#start-with-an-outcome)
- [Instalación](#installation)
- [Cómo continúa el trabajo](#how-the-work-continues)
- [Preguntas y pruebas](#questions-and-evidence)
- [Recuperación y reanudación](#recovery-and-resumption)
- [Resultados y traspasos](#results-and-handoffs)
- [Referencias](#reference)
- [Contribuir](#contributing)
- [Licencia](#license)
- [Desarrollo](#development)

<a id="choose-a-command"></a>
## Elegir un comando

Elige la responsabilidad que necesitas. Puedes empezar con cualquier comando cuyo alcance
se ajuste a tu solicitud; el agente conserva las decisiones aceptadas y recurre a otras
responsabilidades según haga falta, dentro de los permisos que le has dado. No hay una secuencia obligatoria.

En Claude Code, invoca `/lusona:<command>`. En Codex, selecciona la habilidad de Lusona en la
interfaz de habilidades. En Xcode, escribe `/` en una conversación con el agente y selecciona
la habilidad instalada. [Instala Lusona](#installation) antes de usar estos comandos.

| Comando | Para qué sirve |
| --- | --- |
| [explore](plugins/lusona/skills/explore/SKILL.md) | Comprender el tema, explorar posibilidades y definir preferencias mediante el diálogo |
| [status](plugins/lusona/skills/status/SKILL.md) | Evaluar el progreso, todo el trabajo pendiente conocido y la siguiente acción |
| [frame-product](plugins/lusona/skills/frame-product/SKILL.md) | Definir usuarios, problema, resultados deseados y límites del producto |
| [map-capabilities](plugins/lusona/skills/map-capabilities/SKILL.md) | Trazar las capacidades, sus dependencias y el orden de entrega |
| [specify](plugins/lusona/skills/specify/SKILL.md) | Acordar el comportamiento, las restricciones, los criterios de aceptación y la política de TDD de un cambio |
| [architect](plugins/lusona/skills/architect/SKILL.md) | Resolver decisiones de diseño, contratos y asignación de responsabilidades con consecuencias importantes |
| [investigate](plugins/lusona/skills/investigate/SKILL.md) | Determinar causas, hechos o viabilidad mediante pruebas y experimentos |
| [implement](plugins/lusona/skills/implement/SKILL.md) | Planificar y entregar un cambio de comportamiento o una corrección de errores autorizados |
| [review](plugins/lusona/skills/review/SKILL.md) | Examinar un diff concreto para detectar defectos y carencias de verificación |
| [refactor](plugins/lusona/skills/refactor/SKILL.md) | Mejorar la estructura del código existente sin alterar su comportamiento ni su compatibilidad |
| [batch](plugins/lusona/skills/batch/SKILL.md) | Coordinar varios resultados seleccionados con autorización expresa para trabajar sin supervisión |

Usa **investigate** para determinar qué ocurre y por qué; usa **architect** para decidir límites
técnicos y resolver equilibrios entre alternativas con consecuencias importantes. Usa **refactor** para un problema
estructural concreto cuando el comportamiento deba mantenerse, e **implement** para cambiar
comportamientos o corregir defectos. Las decisiones de diseño habituales se resuelven dentro
de la implementación o la refactorización. Completar una investigación o una decisión de
diseño no autoriza un cambio en el código de producción.

<a id="start-with-an-outcome"></a>
## Empezar por un resultado

Para un cambio definido, usa `/lusona:implement` en Claude Code o selecciona `implement` en Codex:

> Añade la caducidad de las invitaciones a los siete días. Conserva las invitaciones ya aceptadas.
> El trabajo estará terminado cuando se rechacen las invitaciones de más de siete días,
> las invitaciones aceptadas permanezcan intactas y pase la batería de pruebas. Usa TDD
> dirigido (`targeted`) para el límite de caducidad. Verifica en local; no despliegues.
> Pregunta si una decisión con consecuencias importantes bloquea el cambio.

Indica el resultado, qué significa terminar y los límites de los permisos del agente. El agente
se encarga de la planificación necesaria y continúa con los incrementos que cumplan los
requisitos sin que tengas que dar otro comando. Recibes el resultado, las pruebas de verificación
y las decisiones o limitaciones pendientes.

Elige TDD de forma expresa en la solicitud o mediante una preferencia permanente:

- `none`: la verificación sigue siendo obligatoria, sin exigir que las pruebas se escriban primero.
- `targeted`: escribe primero las pruebas de los comportamientos indicados.
- `strict`: escribe primero las pruebas de cada comportamiento verificable que cambie.

Guarda una preferencia permanente en `docs/lusona/README.md` del proyecto o en las instrucciones
del agente (`CLAUDE.md` o `AGENTS.md`), por ejemplo, `TDD: targeted for changed behavior`.
Sin una selección expresa, el agente puede inspeccionar y planificar, pero pregunta antes de implementar.

Otros puntos de partida:

> **explore:** Ayúdame a comparar los enlaces de invitación y las invitaciones solo por correo.
> Explica las consecuencias para nuestro equipo de soporte antes de que elijamos. Mantén esta
> conversación en el chat; no guardes archivos.

> **investigate:** Averigua por qué las invitaciones caducadas siguen funcionando en esta
> reproducción del problema. Ejecuta experimentos útiles para distinguir las posibles causas
> e informa de las pruebas obtenidas. No cambies el comportamiento del código de producción.

> **implement, solo planificación:** Propón un enfoque para la caducidad de las invitaciones
> y su verificación. No edites la implementación ni las dependencias.

> **status:** Evalúa el trabajo sobre invitaciones a partir de los registros actuales y el
> árbol de trabajo. Dime qué queda pendiente y cuál es la siguiente acción de alcance acotado.

Las conversaciones, especificaciones, planes, decisiones de arquitectura y revisiones no
conceden permiso para implementar. Una solicitud clara de implementación o refactorización
puede avanzar sin un comando `specify` aparte cuando su alcance, política de TDD y requisitos
previos estén resueltos.

<a id="installation"></a>
## Instalación

Elige tu aplicación. Instala desde el repositorio público
[lusona/ai-skills](https://github.com/lusona/ai-skills) por HTTPS; no necesitas credenciales
de GitHub para descargarlo.

<a id="claude-code"></a>
### Claude Code

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

<a id="codex"></a>
### Codex

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

<a id="xcode"></a>
### Xcode

En Xcode 27, abre **Settings > Intelligence > Agents > Plug-ins > Add Plug-in**.
Elige **Add from URL**, introduce `https://github.com/lusona/ai-skills` y selecciona las
habilidades de Lusona que quieras instalar. Consulta los [pasos de instalación en Xcode](plugins/lusona/INSTALL.md#xcode)
para conocer la configuración, las importaciones locales y los detalles de versión.

Tras instalar, inicia una sesión nueva en tu proyecto. Para instalar desde una copia de trabajo
local, usar paquetes portátiles, actualizar o desinstalar, consulta la
[guía de instalación](plugins/lusona/INSTALL.md). Elige una sola fuente del catálogo: copia de
trabajo local o GitHub.

<a id="how-the-work-continues"></a>
## Cómo continúa el trabajo

El agente lee el resultado solicitado, las decisiones aceptadas, las pruebas actuales y los
criterios pendientes; elige una acción de alcance acotado, actúa dentro de sus permisos y
comprueba el resultado. Repite este ciclo mientras quede trabajo útil autorizado. Las
habilidades aportan responsabilidades y conocimientos especializados durante todo el ciclo.

```mermaid
flowchart TD
    Understand[Comprender el resultado y las pruebas] --> Assess{¿Siguiente acción?}
    Assess -->|Queda trabajo autorizado| Act[Ejecutar una acción de alcance acotado]
    Act --> Check[Verificar el resultado]
    Check --> Assess
    Assess -->|Hace falta información o permiso| Ask[Hacer la pregunta]
    Ask -->|Hay trabajo independiente autorizado| Act
    Ask -->|No hay trabajo disponible| Wait[Esperar respuesta; el objetivo sigue activo]
    Wait -->|Se recibe la respuesta o el permiso necesario| Understand
    Assess -->|Pausa solicitada o falta un requisito previo| Pause[Pausar el trabajo afectado]
    Pause -->|Se cumplen las condiciones de reanudación| Understand
    Assess -->|Se cumplen los requisitos de finalización| Done[Completar el resultado solicitado]

    classDef work fill:#dbeafe,stroke:#2563eb,color:#172554
    classDef input fill:#fef3c7,stroke:#b45309,color:#451a03
    classDef complete fill:#dcfce7,stroke:#15803d,color:#14532d
    class Understand,Assess,Act,Check work
    class Ask,Wait,Pause input
    class Done complete
```

El gráfico resume el [ciclo de trabajo compartido](plugins/lusona/README.md#work-loop).
Sus límites se aplican al trabajo afectado; el trabajo independiente autorizado puede
continuar mientras otra parte espera.

- **Continuar:** Ejecutar la siguiente acción útil autorizada. Una recomendación o una
  indicación para continuar no sustituye el trabajo que el agente actual puede realizar.
- **Preguntar y esperar:** Pedir la decisión o el permiso que falta mediante una herramienta
  nativa de preguntas permitida o un texto breve. Continuar el trabajo independiente; ceder
  el turno cuando no quede ninguno. Mientras espera una respuesta, el objetivo sigue activo.
  El silencio no aporta una decisión ni un permiso.
- **Pausar:** Detener el trabajo afectado cuando solicitas una pausa, falta información o una
  capacidad necesaria, faltan permisos o se alcanza un límite de correcciones. Indicar las
  condiciones exactas para reanudarlo. Si tú solicitas la pausa, tú debes pedir la reanudación;
  las demás pausas requieren el requisito previo, las pruebas o los permisos que especifique
  el límite aplicable. Un punto de control por sí solo no aporta ninguno de ellos.
- **Completar:** Terminar todo el alcance autorizado, cumplir los criterios de aceptación y
  realizar las comprobaciones obligatorias, la revisión independiente requerida y cualquier
  aceptación humana o entrega exigida. Que pasen las pruebas no basta para dar el trabajo por
  terminado. Una comprobación obligatoria fallida o sin ejecutar impide afirmar que ha terminado.

Tú controlas el alcance y las decisiones con consecuencias importantes. El agente resuelve
los detalles habituales dentro de tus restricciones y pregunta antes de cambiar resultados
aceptados o tomar medidas destructivas fuera de sus permisos. Las reglas del usuario o del
repositorio pueden exigir revisión independiente; también es obligatoria para límites de
seguridad, datos persistentes, contratos compartidos o varios participantes que escriban de
forma coordinada.

Por ejemplo, un investigador ejecuta otro experimento si permite distinguir entre las causas
pendientes. Si necesita tu compilación para reproducir el problema, te la pide y continúa
cualquier inspección independiente. Cuando ya no queda trabajo independiente útil, espera esa
compilación. Confirmar una causa puede completar el diagnóstico, mientras que corregir el
código de producción sigue requiriendo permiso de implementación y una política de TDD.

El agente revisa los enfoques habituales a partir de las pruebas y conserva el alcance y los
criterios aceptados. Fuera de un lote, tras dos rondas de corrección consecutivas sin avances
sustanciales, deja de repetir las correcciones afectadas e informa de las pruebas. Antes de
alcanzar cuatro rondas en total, puede seguir un enfoque sustancialmente distinto dentro de sus
permisos si hay nuevas pruebas o cambia un requisito previo que lo justifique. Tras cuatro
rondas en total, necesita tu decisión para continuar las correcciones. Los lotes usan el
presupuesto de reparación registrado. Consulta las [reglas de corrección](plugins/lusona/README.md#work-loop)
para conocer el cómputo y las condiciones de reanudación.

El agente principal coordina las preguntas, asignaciones, integración y verificación. Delega
el trabajo sustancial de producto e ingeniería en especialistas con perfiles y modelos
adecuados; puede encargarse del diálogo de exploración y estado. Si la delegación está
prohibida o no está disponible, puede continuar el trabajo autorizado por su cuenta. La
revisión independiente obligatoria sigue necesitando otro revisor. Consulta
[delegación](plugins/lusona/references/delegation.md) para conocer las responsabilidades y los traspasos.

<a id="questions-and-evidence"></a>
## Preguntas y pruebas

El agente adapta las preguntas, explicaciones, ejemplos y experimentos a la comprensión que
has demostrado. Responde primero a las preguntas directas, reutiliza las respuestas ya
acordadas y pregunta sobre incertidumbres con consecuencias importantes. Tu experiencia
modifica la profundidad de las explicaciones; los requisitos de pruebas y decisiones siguen vigentes.

Durante la exploración, puedes comprender mejor el tema o definir preferencias sin elegir una
dirección. El agente usa escenarios concretos y compara ventajas e inconvenientes mientras otro
intercambio pueda cambiar la comprensión que buscas o la siguiente acción. Durante la
investigación, contrasta hipótesis mientras otro experimento pueda distinguir causas. Termina
la indagación cuando más intercambios o experimentos no cambiarían el resultado solicitado ni
la siguiente acción justificada; si faltan pruebas que bloquean el avance, las identifica en
lugar de afirmar que tiene certeza.

Por ejemplo, un mantenedor con experiencia que ya ha indicado las restricciones de
compatibilidad no necesita repetirlas. Si desconoces una opción de migración, el agente te
explica sus consecuencias antes de pedirte una preferencia. Consulta las
[entrevistas de intención](plugins/lusona/references/interviews.md).

<a id="recovery-and-resumption"></a>
## Recuperación y reanudación

El trabajo autorizado incluye registros locales mínimos de recuperación cuando hagan falta
para reanudar con seguridad o coordinar responsabilidades, dentro de las escrituras permitidas
y tus restricciones. Una conversación que no necesites conservar no requiere archivo. El
agente reutiliza el registro del responsable existente o las notas o el registro de cambio
más pequeños que sirvan, y guarda los hechos que han cambiado en puntos significativos y
antes de un traspaso intencionado.

Un registro de recuperación conserva el resultado solicitado, la fuente de los permisos y de
la política de TDD, las decisiones aceptadas, las pruebas útiles, las preguntas pendientes
importantes, las responsabilidades, el recuento de correcciones cuando corresponda y la
siguiente acción. La exploración puede conservar decisiones y preguntas sin especificación ni
cola de trabajo. `implement` y `refactor` pueden crear un registro de cambio cuando haga falta;
ninguno exige pasar antes por `specify`. Registrar contexto no selecciona TDD, no autoriza la
implementación, no incorpora trabajo a una cola ni completa el resultado solicitado.

Las restricciones de solo lectura, de no guardar y de destino tienen prioridad. Si no puede
guardar o está prohibido, el agente ofrece un traspaso en la conversación e indica la
limitación para recuperar el contexto. Una interrupción abrupta puede impedir crear un punto
de control. Al reanudar, el agente comprueba los registros que se conserven y las pruebas del
árbol de trabajo; después pregunta solo por los hechos importantes o los permisos que no
pueda recuperar. Consulta [registros y conservación](plugins/lusona/references/retention.md).

Para otra sesión, una instrucción de continuación útil podría ser:

> Continúa investigando la caducidad de las invitaciones desde el registro responsable del
> trabajo. Reproduce el caso conservado en la compilación proporcionada antes de proponer una
> corrección. Mantén el alcance de diagnóstico registrado; los cambios en el código de
> producción siguen sin autorización.

Esta instrucción permite un traspaso real. El agente actual continúa el trabajo que puede
realizar dentro de sus permisos.

<a id="results-and-handoffs"></a>
## Resultados y traspasos

Lusona está probando un formato compartido para evaluaciones sustanciales y traspasos:
**Resultado**, **Pruebas** y **Siguiente acción**. Acompaña el resultado con **✅ Completado**,
**🔄 En curso**, **❓ Necesita información** o **⏸ En pausa**, y conserva el significado mediante
palabras. Si hace falta una respuesta o aprobación que bloquea el avance, empieza por ella.
El diálogo habitual, las preguntas y las actualizaciones breves mantienen un tono natural.

Ejemplo ilustrativo de traspaso; no demuestra que se haya realizado el trabajo:

> **✅ Completado · Resultado:** Diagnóstico completo; la reproducción confirma que la
> comprobación de caducidad usa una marca de tiempo incorrecta. La corrección en el código de
> producción sigue sin autorización.
>
> **Pruebas:** El caso conservado y la comprobación específica coinciden. Falta probar el
> comportamiento en las distintas plataformas.
>
> **Siguiente acción:** Puedes autorizar la corrección de la marca de tiempo y seleccionar su
> política de TDD; entonces el agente podrá implementar y verificar esa corrección de alcance acotado.

El estado describe la respuesta o el resultado autorizado: completar un diagnóstico no
completa la corrección propuesta. En un traspaso, la siguiente acción identifica a su
responsable, los datos necesarios y los permisos pendientes. Al finalizar, puede ser
**Ninguna para esta solicitud**.

Las tablas de estado usan **Resultado | Estado | Trabajo pendiente** y conservan bloqueos y
dependencias. Las tablas comparativas usan columnas útiles, como **Opción | Ventaja | Contrapartida**.
Las tablas especializadas y los esquemas de registros guardados conservan su finalidad. El
formato que solicites y las restricciones de la aplicación tienen prioridad; el texto y el
formato compatibles conservan el mismo significado cuando los símbolos o las tablas no
resulten adecuados. Esta convención de presentación es una prueba provisional; aún no se ha
comprobado su comportamiento en las distintas aplicaciones. Consulta
[revisión y comunicación](plugins/lusona/README.md#review-and-communication).

<a id="reference"></a>
## Referencias

- [Instalación y desinstalación](plugins/lusona/INSTALL.md)
- [Contrato del flujo de trabajo y ciclo de trabajo](plugins/lusona/README.md#work-loop)
- [Selección de habilidades y terminología](plugins/lusona/references/workflow-guide.md)
- [Política de TDD y secuencia de trabajo](plugins/lusona/references/tdd.md)
- [Ejecución de lotes y recuperación](plugins/lusona/references/batch-execution.md)
- [Registros y conservación](plugins/lusona/references/retention.md)
- [Cierre y reapertura](plugins/lusona/references/closeout.md)
- [Delegación y asignación de modelos](plugins/lusona/references/delegation.md)

<a id="contributing"></a>
## Contribuir

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para conocer el alcance de las contribuciones, las
comprobaciones locales y las pull requests. Usa los
[formularios de errores y solicitudes de funciones](https://github.com/lusona/ai-skills/issues/new/choose)
para informar de problemas o proponer mejoras. El equipo `@lusona/core` se encarga de la revisión
del repositorio.

<a id="license"></a>
## Licencia

Las habilidades, plantillas, documentación y scripts están disponibles bajo la [licencia MIT](LICENSE).

<a id="development"></a>
## Desarrollo

Las fuentes canónicas del flujo de trabajo están en `plugins/lusona/`. Los datos de cada
proyecto consumidor pertenecen a su propio `docs/lusona/`; la estructura de cola vacía está en
`templates/work.md`.

```bash
claude plugin validate plugins/lusona
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package.py
```

El generador de paquetes comprueba la identidad y versión de los manifiestos nativos, los
enlaces, las rutas del catálogo y la selección de archivos. Escribe en `tmp/lusona-package/`
dentro del repositorio; usa `--output tmp/<new-directory>` para generar otro paquete. Ambos
manifiestos deben usar la misma versión. La instalación desde GitHub utiliza el código
confirmado mediante commit y enviado al repositorio remoto; puedes usar una copia de trabajo
local antes de publicar. Ni la instalación ni la creación de paquetes inicializan los
registros del proyecto.

Reducir el tamaño del código fuente no demuestra un ahorro de tokens o latencia; para ello
hacen falta mediciones que incluyan al coordinador y a todos los agentes de trabajo.
