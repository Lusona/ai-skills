# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona 提供 15 项技能，用于与编程智能体协作开展产品和工程工作。每项技能负责一项职责，例如定义变更规格、实现或审查变更。所有技能遵循同样的八项循环原则，在项目的 `docs/lusona/` 下保存记录，并在每次任务回复末尾说明状态、证据和下一步行动。

适用于 Claude Code、Codex、[Cursor](INSTALL.md#cursor)、[Xcode 27 编程智能体](INSTALL.md#xcode) 和 [Google Antigravity App、CLI 与 IDE](INSTALL.md#antigravity) · 当前工作副本的源码版本：**3.1.0**

> [!WARNING]
> 请勿通过 Vercel Skills（`npx skills@latest`）安装 Lusona；请使用[原生插件安装方式](#安装)。

了解我们为什么开发 Lusona Skills：[Why we built Lusona Skills](https://blog.lusona.com/blog/why-we-built-lusona-skills/)。

本 README 介绍当前工作副本中的源码。通过 GitHub 安装时使用的是已提交并推送的源码；本地修改不代表已发布版本。

![Lusona 工作循环、原则与技能分组](plugins/lusona/assets/workflow-loop.svg)

圆环展示工作如何持续推进：选择、行动、检查，再重复。根据当前需求选择技能；任意技能之后都可以使用其他任意技能。

## 目录

- [循环原则](#循环原则)
- [开始工作并选择技能](#开始工作并选择技能)
- [授权与TDD级别](#授权与tdd级别)
- [决策与修订](#决策与修订)
- [证据与完成](#证据与完成)
- [记录与恢复工作](#记录与恢复工作)
- [回复与下一步行动](#回复与下一步行动)
- [安装](#安装)
- [参考资料](#参考资料)
- [参与贡献](#参与贡献)
- [许可证](#许可证)
- [开发](#开发)

## 循环原则

所有技能都在同一循环中开展工作：选择下一项范围明确的行动，执行，检查结果，反复进行，直到达成请求的目标。循环的目的是随着理解加深，不断改进系统和设计。每项技能都应用以下八项原则，具体定义见[工作流指南](plugins/lusona/references/workflow-guide.md#loop-principles)。

| ID | 原则 | 对你的意义 |
| --- | --- | --- |
| P1 | 无固定顺序 | 智能体根据尚未解决的需求选择下一项技能。任意技能之后都可以使用其他任意技能；每项变更只使用其剩余工作需要的技能。 |
| P2 | 逐步改进 | 每轮都将结果与预期目标比较，并区分事实与假设。目标、已确认的决策、授权、TDD 级别、证据和不确定性都会传递到下一轮。 |
| P3 | 将既有决策作为输入 | 新输入与已确认的决策冲突时，智能体既不会拒绝新输入，也不会忽略原决策。它会说明冲突，并与你一起重新评估决策。 |
| P4 | 记录失效 | 被取代的决策须标明日期和来源，并保留理由。相关记录须同步修正；过时的记录不能让已被取代的选择重新生效。 |
| P5 | 以证据代替断言 | 智能体只能根据实际观察到的检查结果报告行为和完成情况。规定的检查失败或尚未执行时，不得宣称完成。 |
| P6 | 决定权属于用户 | 规格说明、计划、ADR 和队列状态均不构成实现授权。修改已确认的目标、契约、TDD 级别或影响重大的承诺，需要你作出决定。 |
| P7 | 继续范围明确的工作 | 智能体无须等待新指令，就会执行下一项已获授权的行动；当进一步询问无法改变下一步行动时停止询问，只暂停受影响的工作。 |
| P8 | 每次回复都说明下一步行动 | 每次任务回复均以下一项行动及其负责人结尾；如果没有剩余行动，则说明这一点及原因。 |

## 开始工作并选择技能

在新项目中，先运行一次 **setup**。它是可选的，没有任何技能要求先运行它。它会创建 `docs/lusona/` 和工作队列，询问长期 TDD 偏好和模型层级对应关系（均为可选），并在你确认文本后，把“Lusona skills”部分添加到 `AGENTS.md`。该部分告诉后续会话中的智能体：此项目使用 Lusona 技能，以及适用哪种 TDD 偏好。

刚接手项目、恢复工作或决定哪些事项需要处理时，从 **status** 开始。它会评估可读取的记录和证据，列出所有已知的剩余工作，并建议下一步行动。项目尚无 Lusona 记录时也可以使用。请求查看状态既不会授予，也不会撤销执行权限。

选择符合当前需求的技能（P1）。表中各行不代表执行顺序：已获授权且明确说明预期行为和范围的请求，可以直接使用 **implement**，无须先用 **specify**。

| 技能 | 使用时机 |
| --- | --- |
| [setup](plugins/lusona/skills/setup/SKILL.md) | 需要为项目配置 Lusona：创建 `docs/lusona/` 和工作队列，并在 `AGENTS.md` 中添加 Lusona 部分（可选） |
| [status](plugins/lusona/skills/status/SKILL.md) | 需要了解现状、进展、剩余工作或恢复方法 |
| [explore](plugins/lusona/skills/explore/SKILL.md) | 希望先思考方向、选项或未来，再作选择 |
| [frame-product](plugins/lusona/skills/frame-product/SKILL.md) | 产品的受众、问题、愿景、目标或边界尚未定义或正在改变 |
| [map-capabilities](plugins/lusona/skills/map-capabilities/SKILL.md) | 需要明确能力覆盖、依赖关系或交付顺序 |
| [specify](plugins/lusona/skills/specify/SKILL.md) | 需要定义变更的预期行为、范围或验收标准 |
| [architect](plugins/lusona/skills/architect/SKILL.md) | 涉及边界、契约或职责归属且具有长期影响的技术决策尚未解决 |
| [design](plugins/lusona/skills/design/SKILL.md) | 需要看到页面、流程、状态或关系，才能判断或选择 |
| [implement](plugins/lusona/skills/implement/SKILL.md) | 变更已获实现授权，或只需要计划 |
| [review](plugins/lusona/skills/review/SKILL.md) | 完成前需要对照预期行为审查差异 |
| [refactor](plugins/lusona/skills/refactor/SKILL.md) | 现有代码存在具体的结构问题，且必须保持行为不变 |
| [investigate](plugins/lusona/skills/investigate/SKILL.md) | 需要证据来回答原因、观测到的行为或可行性问题 |
| [measure](plugins/lusona/skills/measure/SKILL.md) | 决策需要基线、基准测试或可比较的观测数据 |
| [experiment](plugins/lusona/skills/experiment/SKILL.md) | 需要通过试验，决定采纳、拒绝或改进某种方法 |
| [batch](plugins/lusona/skills/batch/SKILL.md) | 授权对选定的队列项开展无人值守工作，或继续已记录的批次 |

[工作流指南](plugins/lusona/references/workflow-guide.md)列出了各技能的角色、产出、路由表和术语。技能之间的切换无须重新批准，也无须你指挥每次切换。

在所用应用中调用技能：

- Claude Code：`/lusona:<skill>`，例如 `/lusona:status`。
- Codex CLI：`$lusona:<skill>`，例如 `$lusona:status`。Codex 桌面应用：`$lusona:<skill>` 或 `/lusona:<skill>`。也可以从技能界面选择 Lusona 技能。
- Cursor：在 Agent 聊天中输入 `/` 并选择技能。
- Xcode：在智能体对话中输入 `/` 并选择已安装的技能。
- Antigravity App 和 CLI：`/<skill>`，例如 `/status`。在独立 IDE 中查看 **Customizations**，并在请求中指定 Lusona 技能名称。

使用这些技能前，请先[安装 Lusona](#安装)。技能请求应说明技能名称、目标或输入记录，以及授权范围。例如：

> **setup:** 在这个项目中设置 Lusona。写入 `AGENTS.md` 之前，先给我看要写入的文本。

> **status:** 根据现有记录和工作区评估这个项目。告诉我还剩哪些工作，并建议从哪里开始。

> **explore:** 帮我比较邀请链接与仅通过电子邮件邀请这两种方式。在做选择前，说明它们对支持团队的影响。只在对话中讨论，不要保存文件。

> **design:** 使用现有页面、导航和文案，比较两种邀请流程。展示各步骤和邀请过期状态，并说明每种方案的取舍。仅进行视觉设计，不要实现界面。

> **implement:** 将邀请的有效期设为七天。保留已接受的邀请。完成标准：拒绝超过七天的邀请，已接受的邀请保持不变，测试套件通过。针对有效期的边界条件采用 TDD 级别 `targeted`。在本地验证，不要部署。

## 授权与TDD级别

决定权属于你（P6）。以下规则适用于所有技能：

- 规格说明、计划、ADR 和队列状态均不构成实现授权。讨论和只读审查也不构成实现授权。
- 选择实现某项任务，并不代表授权实现其所属变更的其他部分。
- 智能体在执行破坏性操作前，以及修改已确认的目标、契约、TDD 级别或影响重大的承诺前，会向你询问。
- 智能体只有获得你的授权，才会提交、推送或发布。已获授权的实现和重构包括本地提交。
- 仅要求 **implement** 制定计划时，工作以提出方案结束，不构成实现授权。
- **batch** 只对你明确授权的固定一组队列项开展无人值守工作。并发分工最多为 4 项；如果你选择 5 项，则最多为 5 项，同时受应用容量限制。除非你批准其他次数，否则每项的修复预算为 2 轮纠正。

实现工作要求明确选择 TDD 级别，没有默认值。

| TDD 级别 | 要求 |
| --- | --- |
| `none` | 不要求先写测试；仍须执行约定的验证和仓库检查 |
| `targeted` | 对指定行为先写测试 |
| `strict` | 对每项新增或修改且可测试的行为先写测试 |

可在请求中选择级别，也可将其作为长期偏好写入项目的 `docs/lusona/README.md` 或智能体指令文件（`CLAUDE.md` 或 `AGENTS.md`），例如 `TDD: targeted for validation and persistence boundaries`。**setup** 可以把该偏好记录到 `AGENTS.md`。在级别选定前，智能体只定义和规划，然后向你提问并推荐级别。它会记录级别及其来源；如果选定的执行顺序不可行，会请你重新选择级别。

在上述授权范围内，智能体无须新指令就会继续工作（P7）。它会执行下一项范围明确的行动，在已获授权的工作中开展测量或实验时也无须新的请求；当答案无法改变下一步行动时，就停止询问。有应用原生提问工具时会使用该工具，并推荐答案，但不会将沉默或预选项视为同意。等待期间只暂停受影响的工作，并说明恢复条件。

与你对话的智能体是协调者。无论任务规模如何，它都会将专业工作委派给下级智能体，并集成和验证其结果，但技能指定由协调者完成的工作除外。有三个技能指定了这类工作：在 **status** 中，协调者自行完成评估；在 **explore** 中，协调者根据对话、项目记录和你指定的文件进行分析；在 **setup** 中，协调者自行完成设置。如果禁止委派或无法委派，协调者自行处理并说明情况。任务分工见[委派规则](plugins/lusona/references/delegation.md)，模型选择见[模型路由](plugins/lusona/references/delegation.md#model-routing)。

## 决策与修订

已确认的决策是后续工作的输入（P3）。当新的需求、规格说明、测量或实验结果与已确认的决策冲突时，智能体会：

1. 在回复和所属记录中说明原决策、来源、冲突以及受影响的假设。
2. 向你提供选项和建议答案。
3. 与你达成一种结果：保留、部分修订或取代原决策。重新评估决策本身不构成变更授权。
4. 在继续依赖该决策的工作前，记录结果。
5. 在现有授权范围内继续不受冲突影响的工作。

记录须保留每项决策的历史（P4）。修订或被取代的决策保留原文和理由，标明你答复的日期和来源；被取代的决策还须链接到替代决策。智能体会在自己的写入职责范围内更新依赖记录、任务分工和交接，报告其他负责人需要作出的修正，并按修订后的决定继续。仍然包含被取代决策的记录应修正或报告，不能继续遵循。详见[修订规则](plugins/lusona/references/revisions.md)。

后续请求会改变当前目标的范围，并保留已有进展。只有在明确取消或替换当前目标，或提出不兼容的目标时，才会替换当前目标。

## 证据与完成

智能体只根据实际观察到的检查结果报告行为，并列明尚未运行和失败的检查（P5）。完成需要达成已获授权的目标、满足其标准、通过规定的检查，并获得任何要求的人类验收。测试通过不代表已获人类验收。

- **先写测试的证据。** 对每项要求先写测试的行为，智能体须在修改生产代码前观察到预期失败，然后观察到通过结果。环境设置失败不能证明预期失败。详见 [TDD](plugins/lusona/references/tdd.md)。
- **纠错限制。** 连续 2 轮纠正没有实质进展时，智能体停止修正该失败，报告证据，并继续不受影响的工作。累计 4 轮后，再进行任何一轮前都须向你询问。批次内则适用修复预算。详见[纠错规则](plugins/lusona/references/corrections.md)。
- **独立审查。** 用户或仓库规则要求时，或变更影响安全边界、持久化数据、共享契约，或涉及多个参与者协同修改时，须由未编写该变更的智能体审查。自行处理始终不能满足这一要求；无法安排独立审查时，智能体会报告该要求尚未满足。
- **研究工作。** **investigate** 回答诊断问题；**measure** 和 **experiment** 开展研究工作。不确定性本身不构成启动研究的理由。请求未要求的研究需要你明确或长期授权，并须有有限的范围和资源预算。决策依据的证据保存在项目的 `docs/lusona/evidence/` 中。详见[证据规则](plugins/lusona/references/evidence.md)。
- **视觉参考。** 当选择取决于布局、结构、流程或外观时，**explore**、**specify**、**architect** 和 **design** 会提供 2-4 个视觉选项。界面草稿在浏览器中打开，或由智能体报告 HTML 的绝对路径；图示使用 Mermaid 代码块。你选定后，参考资料及其约束要求保存在 `docs/lusona/visuals/<record-id>/` 中。**implement** 报告每项约束要求的状态，**review** 逐项报告满足、未满足或未检查。详见[视觉方案与参考](plugins/lusona/references/visuals.md)。

## 记录与恢复工作

智能体会在交接或完成之前主动保存实质性产出：后续工作所依赖的决策、约定、证据、结论、交接和讨论总结。后续工作不依赖的解释和状态更新无须记录。如果禁止保存，智能体会报告哪些内容没有保存。

**setup** 会在你准备项目时创建 `docs/lusona/` 和工作队列（见[开始工作并选择技能](#开始工作并选择技能)）。不运行 setup 时，各技能会自行创建其工作所需的记录。

| 工作 | 项目 `docs/lusona/` 下的记录 |
| --- | --- |
| 需要规格说明的变更 | `specs/<change-id>.md` 和 `work.md` 中的一行 |
| 无规格说明的直接实现或重构 | `notes/<change-slug>.md` |
| 调查、测量或实验 | 笔记以及 `evidence/` 记录 |
| 影响重大的架构决策 | `adr/<YYYYMMDD>-<decision-slug>.md` |
| 产品概述和能力图谱 | `product.md` |
| 批次 | `batches/<batch-slug>.md` |

以下四种情况需要规格说明和对应的队列条目。规模不是判断依据。

- 技能通过规格说明定义变更，例如 **specify**。
- 你要求编写规格说明或跟踪工作。
- 该变更已有规格说明。
- 变更因其影响而需要独立审查。

队列状态为 Ideas、Ready、Doing、Review 和 Done；任何状态都不构成实现授权。Icebox 是队列中存放暂缓条目的区域；暂缓条目保留原有队列状态。详见[队列规则](plugins/lusona/references/queue.md)。

每份所属记录保留一份当前交接，包含目标、决策、授权、TDD 级别及其来源、证据、不确定性、纠错次数、阻碍因素、职责归属和下一步行动（P2）。应用提供上下文使用量时，智能体会在 40% 时准备交接，并在达到 50% 前完成。恢复时，它会读取保留下来的记录和工作区，只向你询问授权或会改变下一步行动的事实。授权在交接后继续有效。突然中断导致无法保存时，智能体不会声称已保存检查点。较早插件版本的记录仍然有效，并在原处更新。详见[记录保留规则](plugins/lusona/references/retention.md)和[文件规则](plugins/lusona/references/files.md)。

恢复工作时，可以用 **status** 评估剩余工作，也可以指定要继续的任务：

> 根据已保存的调查结果，继续调查邀请过期问题。用当前构建版本验证保留的复现案例。不要修改生产代码的行为。

## 回复与下一步行动

每次任务回复均以同样的格式结尾（P8），问候和确认收到消息的回复除外。状态为 **✅ 已完成**（已完成请求范围）、**🔄 进行中**（已获授权的工作继续）、**❓ 需要输入**（缺少前置条件）或 **⏸ 已暂停**（受影响的工作正在等待已说明的前置条件）。状态描述回复，而非队列状态。以下是假设的回复示例，不代表实际开展过工作：

> **Result:** ❓ 需要输入：请在开始实现前选择 TDD 级别。规格说明和验收标准已记录。
>
> **Evidence:** 尚未运行检查；变更已定义，尚未实现。
>
> | Next action | Owner | Needs | Authority |
> | --- | --- | --- | --- |
> | 选择 `none`、`targeted` 或 `strict`；解析器变更建议采用 `targeted` | 用户 | 已记录的规格说明 | 尚未选择 TDD 级别 |

- 负责人是用户、协调者或指明名称的技能。Authority 列填写 `Authorized` 或说明缺少的授权。
- 阻碍工作推进的决策或审批放在最前面。如果作出了影响重大的决定，回复添加 **Decisions:**；如果仍有未解决的问题，则添加 **Open issues:**。
- 请求范围已完成且后续工作有助于约定目标时，回复会提出该工作，并说明缺少的授权。没有剩余行动时，写明 `**Next action:** None for this request`，并用一句话说明原因。
- 给另一会话的继续工作指令，放在表格下方的引用块中。
- 除非你或应用的指示明确要求不兼容的格式，否则回复保留必需的标签和字段。要求简洁并不会去掉必需字段。调整格式时，目标、证据、状态和下一步行动仍须保留。详见[完成示例](plugins/lusona/references/completion.md)。

## 安装

选择你使用的应用。通过 HTTPS 从公开的 [lusona/ai-skills](https://github.com/lusona/ai-skills) 仓库安装；下载无须 GitHub 凭据。

### Antigravity

直接从 GitHub 安装：

```bash
agy plugin install https://github.com/lusona/ai-skills.git
```

此 URL 从仓库根目录的清单安装 Lusona。App 和独立 IDE 用户在通过 CLI 全局安装后，查看 **Customizations**。[Antigravity 安装指南](INSTALL.md#antigravity)涵盖本地工作副本、便携包、更新、移除和验证范围。其中记录了针对 Lusona 1.4.0、在 Linux 上使用 Antigravity CLI 1.4.12 完成的 GitHub 安装检查；App 和 IDE 的交互行为尚未测试。

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

打开 **Customize > From GitHub Repository**，输入 `https://github.com/lusona/ai-skills`，然后为项目或用户安装 **Lusona Skills**。在 Agent 聊天中输入 `/` 查找 Lusona 技能。[Cursor 安装步骤](INSTALL.md#cursor)提供当前 Cursor 文档的链接和测试状态。

### Xcode

在 Xcode 27 中，打开 **Settings > Intelligence > Agents > Plug-ins > Add Plug-in**。选择 **Add from URL**，输入 `https://github.com/lusona/ai-skills`，然后选择要安装的 Lusona 技能。有关设置、本地导入和版本详情，请参阅 [Xcode 安装步骤](INSTALL.md#xcode)。

安装后，在项目中开启新会话。有关从本地工作副本安装、便携安装包、更新和移除的说明，请参阅[安装指南](INSTALL.md)。插件目录请选择单一来源：本地工作副本或 GitHub。

## 参考资料

- [更新日志](CHANGELOG.md)
- [安装与移除](INSTALL.md)
- [隐私政策](PRIVACY.md)
- [使用条款](TERMS.md)
- [插件目录：技能、参考资料和模板](plugins/lusona/README.md)
- [循环原则、技能、路由和术语](plugins/lusona/references/workflow-guide.md)
- [TDD 级别与验证](plugins/lusona/references/tdd.md)
- [批次协调](plugins/lusona/skills/batch/SKILL.md)
- [记录、保留和交接](plugins/lusona/references/retention.md)
- [收尾与重新开启](plugins/lusona/references/closeout.md)
- [委派](plugins/lusona/references/delegation.md)
- [意图访谈](plugins/lusona/references/interviews.md)

## 参与贡献

有关贡献范围、本地检查和拉取请求，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。如需报告问题或提出改进建议，请使用[缺陷和功能请求表单](https://github.com/lusona/ai-skills/issues/new/choose)。`@lusona/core` 团队负责仓库审查。

## 许可证

技能、模板、文档和脚本采用 [MIT 许可证](LICENSE)。

## 开发

工作流的正式源文件位于 `plugins/lusona/`。使用该插件的项目应将自身数据放在该项目的 `docs/lusona/` 下；空队列结构见 `plugins/lusona/templates/work.md.template`。

插件的记录辅助工具使用 Bash 或 PowerShell（[运行环境要求](INSTALL.md#requirements)）。只有打包和运行 Python 评估需要 Python 3，使用插件则不需要。

```bash
claude plugin validate plugins/lusona
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package.py
```

打包工具会检查原生清单的名称与版本、链接、插件目录路径和打包文件范围。所有原生清单必须使用相同版本。输出写入仓库内的 `tmp/lusona-package/`，且拒绝覆盖已有输出目录；再次构建时请使用 `--output tmp/<new-directory>`。安装和打包都不会初始化项目记录。

各 `SKILL.md` 中的通用任务规则和回复格式由仓库的 `shared/` 目录生成。请在该目录中编辑，然后运行 `python3 scripts/sync_shared.py --source shared
plugins/lusona`；添加 `--check` 可仅验证而不写入。
