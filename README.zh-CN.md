<a id="lusona-ai-skills"></a>
# Lusona AI Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

> [!WARNING]
> 请勿通过 Vercel Skills（`npx skills@latest`）安装 Lusona；请使用[原生插件安装方式](#installation)。

Lusona 帮助 AI 智能体从理解需求、执行工作到验证结果，完成你提出的目标。你确定目标、约束和授权范围。智能体根据证据选择下一项有用的行动，继续已获授权的工作，并在需要你的意见或许可时提问。

适用于 Claude Code、Codex 和 [Xcode 27 编码智能体](plugins/lusona/INSTALL.md#xcode) · 当前检出源码版本：**1.0.0**

本 README 描述当前检出目录中的源码。通过 GitHub 安装时使用的是已提交并推送的源码；本地修改不代表已发布版本。

<a id="index"></a>
## 目录

- [选择命令](#choose-a-command)
- [从目标开始](#start-with-an-outcome)
- [安装](#installation)
- [工作如何继续](#how-the-work-continues)
- [提问与证据](#questions-and-evidence)
- [恢复与续接](#recovery-and-resumption)
- [结果与交接](#results-and-handoffs)
- [参考资料](#reference)
- [参与贡献](#contributing)
- [许可证](#license)
- [开发](#development)

<a id="choose-a-command"></a>
## 选择命令

根据所需职责选择命令。只要命令的范围符合你的请求，就可以从它开始，无须遵循固定顺序。智能体会沿用已接受的决定，并在授权范围内按需运用其他职责。

在 Claude Code 中，输入 `/lusona:<command>`。在 Codex 中，从技能界面选择 Lusona 技能。在 Xcode 中，在智能体对话里输入 `/`，然后选择已安装的技能。使用这些命令前，请先[安装 Lusona](#installation)。

| 命令 | 用途 |
| --- | --- |
| [explore](plugins/lusona/skills/explore/SKILL.md) | 通过讨论增进理解，探索可能性与偏好 |
| [status](plugins/lusona/skills/status/SKILL.md) | 评估当前进展、所有已知的剩余工作及下一步行动 |
| [frame-product](plugins/lusona/skills/frame-product/SKILL.md) | 明确用户、问题、预期结果和产品边界 |
| [map-capabilities](plugins/lusona/skills/map-capabilities/SKILL.md) | 梳理能力、依赖关系和交付顺序 |
| [specify](plugins/lusona/skills/specify/SKILL.md) | 就一项变更的行为、约束、验收标准和 TDD 策略达成一致 |
| [architect](plugins/lusona/skills/architect/SKILL.md) | 确定影响重大的设计、契约和责任归属 |
| [investigate](plugins/lusona/skills/investigate/SKILL.md) | 通过证据和实验查明原因、事实或可行性 |
| [implement](plugins/lusona/skills/implement/SKILL.md) | 规划并交付已获授权的行为变更或缺陷修复 |
| [review](plugins/lusona/skills/review/SKILL.md) | 检查实际 diff 中的缺陷和验证缺口 |
| [refactor](plugins/lusona/skills/refactor/SKILL.md) | 在保持行为和兼容性的前提下改善现有代码结构 |
| [batch](plugins/lusona/skills/batch/SKILL.md) | 在明确的无人值守工作授权下，协调多个选定目标 |

用 **investigate** 查明发生了什么以及原因；用 **architect** 决定影响重大的技术边界与取舍。行为保持不变、需要解决具体结构问题时，用 **refactor**；需要改变行为或修复缺陷时，用 **implement**。常规设计选择由实现或重构过程处理。完成调查或设计决策，并不意味着已获准修改生产代码。

<a id="start-with-an-outcome"></a>
## 从目标开始

对于已明确的变更，在 Claude Code 中使用 `/lusona:implement`，或在 Codex 中选择 `implement`：

> 为邀请添加七天有效期。保留已接受的邀请。
> 完成标准：拒绝超过七天的邀请，已接受的邀请不受影响，测试套件通过。
> 对有效期边界使用 targeted TDD。
> 在本地验证，不要部署。如有影响重大的决定阻碍变更，请提问。

说明目标、完成标准和智能体的授权范围。智能体负责必要的规划，并逐步推进符合条件的工作，无须你再输入命令。你会收到结果、验证证据，以及尚未解决的决定或限制。

请在请求中或长期偏好设置中明确选择 TDD 策略：

- `none`：仍须验证，但不要求先写测试。
- `targeted`：对指定行为先写测试，再实现。
- `strict`：对每项发生变更且可测试的行为，先写测试，再实现。

可将长期偏好写入项目的 `docs/lusona/README.md` 或智能体指令文件（`CLAUDE.md` 或 `AGENTS.md`），例如 `TDD: targeted for changed behavior`。如果没有明确选择，智能体可以检查和规划，但会在实现前询问。

其他起点：

> **explore：** 帮我比较邀请链接与仅通过电子邮件邀请这两种方式。在做选择前，说明它们对支持团队的影响。只在对话中讨论，不要保存文件。

> **investigate：** 查明这个复现案例中已过期的邀请为何仍然有效。运行有助于区分原因的实验，并报告证据。不要改变生产行为。

> **implement，仅规划：** 为邀请过期功能及其验证提出方案。不要修改实现或依赖。

> **status：** 根据现有记录和工作区评估邀请相关工作的进展。告诉我还剩哪些工作，以及下一项范围明确的行动。

讨论、规格说明、计划、架构决策和审查都不授予实现权限。只要范围、TDD 策略和前置条件已经明确，清晰的实现或重构请求便可直接推进，无须单独执行 `specify` 命令。

<a id="installation"></a>
## 安装

选择你使用的宿主。通过 HTTPS 从公开的 [lusona/ai-skills](https://github.com/lusona/ai-skills) 仓库安装；下载无须 GitHub 凭据。

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

在 Xcode 27 中，打开 **Settings > Intelligence > Agents > Plug-ins > Add Plug-in**。
选择 **Add from URL**，输入 `https://github.com/lusona/ai-skills`，然后选择要安装的 Lusona 技能。有关设置、本地导入和版本详情，请参阅 [Xcode 安装步骤](plugins/lusona/INSTALL.md#xcode)。

安装后，在项目中开启新会话。有关从本地检出目录安装、便携安装包、更新和移除的说明，请参阅[安装指南](plugins/lusona/INSTALL.md)。插件目录来源只选一个：本地检出目录或 GitHub。

<a id="how-the-work-continues"></a>
## 工作如何继续

智能体阅读目标、已接受的决定、当前证据和剩余标准，选择一项范围明确的行动，在授权范围内执行，再检查结果。只要仍有有用且已获授权的工作，智能体就会重复这个循环。技能在整个循环中提供职责指引和领域知识。

```mermaid
flowchart TD
    Understand[理解目标和证据] --> Assess{下一步行动？}
    Assess -->|仍有已获授权的工作| Act[执行范围明确的行动]
    Act --> Check[验证结果]
    Check --> Assess
    Assess -->|需要意见或授权| Ask[提出问题]
    Ask -->|有可独立推进的已授权工作| Act
    Ask -->|没有此类工作| Wait[等待答复；目标仍在进行]
    Wait -->|收到所需答复或授权| Understand
    Assess -->|用户要求暂停或缺少前置条件| Pause[暂停受影响的工作]
    Pause -->|满足恢复条件| Understand
    Assess -->|已满足完成要求| Done[完成请求的目标]

    classDef work fill:#dbeafe,stroke:#2563eb,color:#172554
    classDef input fill:#fef3c7,stroke:#b45309,color:#451a03
    classDef complete fill:#dcfce7,stroke:#15803d,color:#14532d
    class Understand,Assess,Act,Check work
    class Ask,Wait,Pause input
    class Done complete
```

该图概括了[共用工作循环](plugins/lusona/README.md#work-loop)。其中的边界适用于受影响的工作；一部分工作等待时，其他已获授权且不依赖它的工作仍可继续。

- **继续：** 执行下一项有用且已获授权的行动。当前智能体能完成的工作，不能用建议或让用户另行续接的提示来代替。
- **提问并等待：** 使用获准的原生提问工具或简短文字，请求缺失的决定或授权。继续不受影响的独立工作；没有此类工作时，交还控制权并等待答复。等待期间，目标仍在进行。沉默不代表决定或许可。
- **暂停：** 当你要求暂停、缺少必要输入或能力、缺少授权，或达到纠错限制时，停止受影响的工作，并说明恢复所需的具体条件。由你要求的暂停，须由你指示恢复；其他暂停须补齐适用边界所要求的前置条件、证据或授权。单纯保存检查点不能满足这些条件。
- **完成：** 完成全部已授权范围、验收标准、必需检查、必需的独立审查，以及任何必需的人工验收或交付。仅测试通过不足以认定完成。必需检查失败或尚未运行时，不得宣称完成。

你掌握范围和重大决定。智能体在约束内处理常规细节；在改变已接受的目标，或执行超出授权范围的破坏性操作前，智能体会询问。用户或仓库规则要求时，以及工作涉及安全边界、持久化数据、共享契约或多名协同修改者时，须进行独立审查。

例如，负责调查的智能体会在下一次实验有助于区分剩余原因时继续实验。如果它需要你提供用于复现的构建版本，就会提出请求，并继续不依赖该构建的检查。没有其他有用的独立工作后，它会等待该构建。确认原因可以完成诊断，但生产代码修复仍须获得实现授权，并明确 TDD 策略。

智能体会根据证据调整常规方案，同时保持已接受的范围和标准。非批处理任务中，连续两轮纠错未取得实质进展后，智能体会停止重复相关纠错，并报告证据。累计不足四轮时，如果新证据或前置条件变化提供了依据，智能体可以在授权范围内尝试有实质区别的方案。累计达到四轮后，进一步纠错须由你决定。批处理任务使用其记录的修复预算。计数与恢复规则见[纠错规则](plugins/lusona/README.md#work-loop)。

主智能体协调提问、分工、集成和验证，并将实质性的产品与工程工作委派给具备合适角色和模型的专门智能体；探索和状态对话可由主智能体处理。如果禁止委派或无法委派，智能体可以在本地继续已获授权的工作。必需的独立审查仍须由另一位审查者完成。责任归属和交接规则见[委派](plugins/lusona/references/delegation.md)。

<a id="questions-and-evidence"></a>
## 提问与证据

智能体会根据你在交流中表现出的理解程度，调整问题、解释、示例和实验。它会先回答直接问题，沿用已经确定的答案，并对影响重大的不确定事项提问。你的专业经验决定解释的深度，但证据和决策要求仍然适用。

探索时，你可以增进理解或形成偏好，而不必选定方向。只要进一步交流可能改变你所要求的理解或下一步行动，智能体就会借助具体情景和取舍继续讨论。调查时，只要另一次实验还可能区分原因，智能体就会继续检验假设。如果进一步交流或实验既不会改变请求的目标，也不会改变有依据的下一步行动，智能体会结束探究；如果缺少证据阻碍进展，它会指出缺少什么，而不声称已有定论。

例如，有经验的维护者已经提供兼容性约束，就无须重复回答。对于不熟悉某项迁移选择的读者，智能体会先解释后果，再询问偏好。详见[意图访谈](plugins/lusona/references/interviews.md)。

<a id="recovery-and-resumption"></a>
## 恢复与续接

为了安全续接工作或协调责任归属而需要记录时，已授权工作包括在获准写入的范围和你的限制内，保存最少量的本地恢复记录。无须留存的对话不用写文件。智能体会沿用现有的记录归属，或选择足够用的最小笔记或变更记录，在有意义的任务节点及主动交接前保存事实变化。

恢复记录保留目标、授权和 TDD 策略的来源、已接受的决定、有用证据、重要的待决问题、责任归属、适用时的纠错轮数，以及下一步行动。探索阶段可以只保留决定和问题，无须规格说明或队列。implement 和 refactor 可以按需创建变更记录，两者都不要求先经过 Specify。记录上下文本身不会选定 TDD 策略、授予实现权限、将工作加入队列，也不代表目标完成。

只读、禁止保存和保存位置限制具有优先权。如果禁止保存或无法保存，智能体会在对话中提供交接内容，并说明恢复方面的限制。突然中断可能导致来不及保存检查点。续接时，智能体会检查保留下来的记录和工作区证据，只询问无法恢复的重要事实或授权。详见[记录与保留](plugins/lusona/references/retention.md)。

在另一个会话中，可以这样指示续接：

> 从负责记录此任务的文档继续调查邀请过期问题。在提出修正方案前，先用已提供的构建版本复现保留的案例。保持记录中的诊断范围；生产变更仍未获授权。

此类指令用于真正的任务交接。当前智能体仍会继续完成授权范围内自己能够执行的工作。

<a id="results-and-handoffs"></a>
## 结果与交接

Lusona 正在试用一种共用格式，用于实质性评估和交接：**结果**、**证据**和**下一步行动**。结果须配上 **✅ 已完成**、**🔄 进行中**、**❓ 需要输入**或 **⏸ 已暂停**，并保留表达含义的文字。如有阻碍进展的问题或审批请求，先提出它。日常对话、提问和简短更新保持自然表达。

以下是交接示例，不代表已经执行了这些工作：

> **✅ 已完成 · 结果：** 诊断完成；复现确认过期检查使用了错误的时间戳。生产修复仍未获授权。
>
> **证据：** 保留的案例和针对性检查结果一致。尚未测试跨平台行为。
>
> **下一步行动：** 你可以授权修正时间戳，并选择 TDD 策略；随后智能体即可实现并验证这项范围明确的修复。

状态描述的是本次答复或已授权目标：诊断完成不等于拟议修复完成。交接时，下一步行动须明确负责人、所需输入和仍需获得的授权。完成时，可以写为**本次请求无后续行动**。

状态表使用**目标 | 状态 | 剩余工作**，保留阻碍和依赖关系。比较表可使用**选项 | 好处 | 取舍**等有用列。专用表格和已保存记录的结构保留各自用途。你的格式要求和宿主限制具有优先权；符号或表格不适用时，使用宿主支持的文字和格式表达相同含义。这种呈现约定仍在试用，尚未确认各宿主中的实际表现。详见[审查与沟通](plugins/lusona/README.md#review-and-communication)。

<a id="reference"></a>
## 参考资料

- [安装与移除](plugins/lusona/INSTALL.md)
- [工作流契约与工作循环](plugins/lusona/README.md#work-loop)
- [技能选择与术语](plugins/lusona/references/workflow-guide.md)
- [TDD 策略与执行顺序](plugins/lusona/references/tdd.md)
- [批处理执行与恢复](plugins/lusona/references/batch-execution.md)
- [记录与保留](plugins/lusona/references/retention.md)
- [收尾与重新开启](plugins/lusona/references/closeout.md)
- [委派与模型路由](plugins/lusona/references/delegation.md)

<a id="contributing"></a>
## 参与贡献

有关贡献范围、本地检查和拉取请求，请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。如需报告问题或提出改进建议，请使用[缺陷和功能请求表单](https://github.com/lusona/ai-skills/issues/new/choose)。`@lusona/core` 团队负责仓库审查。

<a id="license"></a>
## 许可证

技能、模板、文档和脚本采用 [MIT 许可证](LICENSE)。

<a id="development"></a>
## 开发

工作流的权威源码位于 `plugins/lusona/`。使用该插件的项目应将自身数据放在该项目的 `docs/lusona/` 下；空队列结构见 `templates/work.md`。

```bash
claude plugin validate plugins/lusona
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package.py
```

打包工具会检查原生清单的标识与版本、链接、插件目录路径和文件选择，并将输出写入仓库内的 `tmp/lusona-package/`。如需输出到其他位置，使用 `--output tmp/<new-directory>`。两个清单必须使用相同版本。通过 GitHub 安装时使用已提交并推送的源码；发布前可使用本地检出目录。安装和打包都不会初始化项目记录。

源码体积缩小不代表 token 用量或延迟下降；这些收益需要对协调者和所有工作智能体进行测量。
