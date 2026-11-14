# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona ayuda a los agentes de programación a llevar una petición de producto o ingeniería
hasta un resultado comprobado. Empieza en un proyecto existente con un cambio pequeño.

> [!TIP]
> ¿Ya lo instalaste? Empieza con `/status` usando el [comando para tu aplicación](#2-obtén-una-recomendación).

## 1. Instala para tu aplicación

Sigue solo las instrucciones de tu aplicación. Completa primero su configuración y autenticación.

**Claude Code** — ejecuta en una terminal:

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

**Codex** — ejecuta en una terminal:

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

**Antigravity** — ejecuta en una terminal:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

Comprueba que `lusona` esté habilitado. En la App, consulta **Customizations > Installed**;
en el IDE independiente, consulta **Customizations** en el panel lateral del agente.

**Cursor** — abre **Customize > From GitHub Repository**, introduce
`https://github.com/lusona/ai-skills`, selecciona **Lusona Skills**, pulsa **Install**
y elige el ámbito de proyecto o usuario.

**Xcode 27** — habilita un agente de programación en **Settings > Intelligence**. En
**Agents > Plug-ins**, pulsa **Add Plug-in > Add from URL > Continue**, introduce
`https://github.com/lusona/ai-skills`, selecciona las habilidades de Lusona y pulsa **Install**.
Una instalación de la CLI independiente no instala el plugin en Xcode.

> [!WARNING]
> Instala el plugin nativo, no Vercel Skills (`npx skills@latest`); las habilidades individuales carecen de los recursos compartidos.

## 2. Obtén una recomendación

Inicia una nueva sesión del agente en tu proyecto e invoca **status**:

| Aplicación | Cómo invocar status |
| --- | --- |
| Claude Code | `/lusona:status` |
| Codex CLI | `$lusona:status` |
| Aplicación de escritorio de Codex | `$lusona:status` o `/lusona:status`, o selecciona `status` en la interfaz de habilidades |
| Antigravity App y CLI | `/status` |
| IDE independiente de Antigravity | Pide: `Usa la habilidad status de Lusona.` |
| Cursor o Xcode | Escribe `/` y selecciona la habilidad `status` de Lusona |

Después pega esta petición, adaptando la función a tu proyecto:

> Quiero que las invitaciones al equipo caduquen después de siete días. Inspecciona este proyecto
> y recomienda un siguiente cambio pequeño. Dime qué existe y qué falta. No cambies archivos todavía.

Recibirás una evaluación del proyecto actual y una siguiente acción recomendada. Si el agente
necesita una decisión, responde con palabras sencillas. Por ejemplo:

> Cuenta siete días desde el envío de la invitación. Mantén sin cambios las invitaciones aceptadas.

Para un proyecto vacío, prueba: «Quiero crear un servicio de invitaciones a equipos. Ayúdame a elegir el primer cambio pequeño».

## 3. Empieza el trabajo

Cuando la recomendación coincida con lo que quieres, responde:

> Implementa esa recomendación. Limita el cambio a la caducidad de las invitaciones y conserva
> las invitaciones aceptadas. Verifícalo localmente. No hagas commits ni despliegues.

El agente puede pedirte que aclares el comportamiento o elijas cómo probarlo antes de implementar.
Al terminar, comprueba qué cambió, qué verificaciones se ejecutaron y sus resultados, y qué límites
o decisiones quedan. Si alguna verificación no pudo ejecutarse, el informe debe indicarlo.

## Uso cotidiano

Estos grupos son opciones, no etapas obligatorias; empieza con **status** si tienes dudas.

Los comandos `/name` de abajo usan la forma abreviada de Antigravity App/CLI. En Claude Code usa `/lusona:<name>`; en Codex CLI, `$lusona:<name>`. En otras aplicaciones, usa el mismo método de invocación que en la tabla de status anterior.

### Empezar o retomar

| Comando | Úsalo para |
| --- | --- |
| `/status` | Evaluar el progreso, el trabajo pendiente y la siguiente acción. |
| `/setup` | Preparar, de forma opcional, los registros del proyecto y las preferencias permanentes. |

### Explorar y planificar

| Comando | Úsalo para |
| --- | --- |
| `/explore` | Comparar ideas o direcciones antes de elegir. |
| `/frame-product` | Definir el público, el problema, la visión y los límites de un producto. |
| `/map-capabilities` | Organizar capacidades, dependencias y orden de entrega. |

### Definir un cambio

| Comando | Úsalo para |
| --- | --- |
| `/specify` | Definir el comportamiento, el alcance y los criterios de aceptación de un cambio. |
| `/architect` | Resolver una decisión técnica duradera sobre límites, contratos o responsabilidades. |
| `/design` | Crear bocetos de interfaz, flujos o diagramas para compararlos. |

### Implementar y verificar

| Comando | Úsalo para |
| --- | --- |
| `/implement` | Implementar un cambio acotado y autorizado, o solicitar solo un plan. |
| `/refactor` | Mejorar la estructura del código conservando su comportamiento. |
| `/review` | Revisar un diff e informar de los hallazgos sin editar la implementación. |
| `/batch` | Ejecutar trabajo desatendido con autorización explícita sobre una selección fija de elementos de la cola. |

### Investigar y comparar

| Comando | Úsalo para |
| --- | --- |
| `/investigate` | Establecer con evidencias la causa, el comportamiento observado o la viabilidad. |
| `/measure` | Establecer una referencia, un benchmark o mediciones comparables. |
| `/experiment` | Probar una intervención o comparar alternativas en un ensayo acotado. |

Añade restricciones de forma natural, como «mantén la API pública sin cambios» o «no hagas ningún commit todavía».

## Más información cuando la necesites

- [Detalles de instalación (en inglés)](INSTALL.md): actualizaciones, eliminación, paquetes locales, requisitos y limitaciones por aplicación.
  No se han probado la instalación ni el comportamiento interactivo de Antigravity App/IDE,
  ni la instalación e invocación en Cursor/Xcode.
- [Guía de uso (en inglés)](docs/usage.md): más ejemplos, setup opcional y otras habilidades.
- [Detalles del flujo de trabajo (en inglés)](docs/workflow.md): pruebas, evidencias y reanudación del trabajo.
- [Por qué creamos Lusona (en inglés)](https://blog.lusona.com/blog/why-we-built-lusona-skills/).

Versión del código fuente de esta copia de trabajo: **3.1.0**. La instalación desde GitHub usa
el código incluido en commits y enviado al repositorio remoto; los cambios locales no constituyen
una versión publicada. Consulta el [historial de cambios (en inglés)](CHANGELOG.md).

[Contribuir (en inglés)](CONTRIBUTING.md) · [Informar de un problema (en inglés)](https://github.com/lusona/ai-skills/issues/new/choose) · [Privacidad (en inglés)](PRIVACY.md) · [Condiciones de uso (en inglés)](TERMS.md) · [Licencia MIT (en inglés)](LICENSE)
