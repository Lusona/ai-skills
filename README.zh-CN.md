# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona 帮助编程智能体完成产品或工程需求，并验证结果。
从现有项目中的一个小变更开始。

> [!TIP]
> 已安装？请使用[所在应用的命令](#2-获取建议)，从 `/status` 开始。

## 1. 为所在应用安装

只需执行所在应用的安装步骤。请先完成该应用的设置和身份验证。

**Claude Code** — 在终端运行：

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

**Codex** — 在终端运行：

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

**Antigravity** — 在终端运行：

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

确认 `lusona` 已启用。App 中请查看 **Customizations > Installed**；
独立 IDE 中请查看智能体侧面板的 **Customizations**。

**Cursor** — 打开 **Customize > From GitHub Repository**，输入
`https://github.com/lusona/ai-skills`，选择 **Lusona Skills**，点击 **Install**，
然后选择项目或用户范围。

**Xcode 27** — 在 **Settings > Intelligence** 中启用编程智能体。在
**Agents > Plug-ins** 中点击 **Add Plug-in > Add from URL > Continue**，输入
`https://github.com/lusona/ai-skills`，选择 Lusona 的技能并点击 **Install**。
安装到独立 CLI 不会在 Xcode 中安装此插件。

> [!WARNING]
> 请安装原生插件，不要使用 Vercel Skills（`npx skills@latest`）；单独安装的技能缺少共享资源。

## 2. 获取建议

在项目中开启新的智能体会话，然后调用 **status**：

| 应用 | 调用 status |
| --- | --- |
| Claude Code | `/lusona:status` |
| Codex CLI | `$lusona:status` |
| Codex 桌面应用 | `$lusona:status` 或 `/lusona:status`，或在技能界面选择 `status` |
| Antigravity App 和 CLI | `/status` |
| Antigravity 独立 IDE | 提出请求：`请使用 Lusona 的 status 技能。` |
| Cursor 或 Xcode | 输入 `/` 并选择 Lusona 的 `status` 技能 |

然后粘贴以下请求，将功能改为适合你项目的内容：

> 我希望团队邀请在七天后过期。请检查这个项目，推荐下一步要做的一个小变更。
> 告诉我哪些已经实现、哪些尚未实现。暂时不要修改文件。

智能体会评估当前项目，并推荐下一步行动。如果智能体需要你做决定，直接用日常语言回答。例如：

> 从发送邀请时开始计算七天。保留已接受的邀请，不要更改。

对于空项目，可以尝试：“我想开发一个团队邀请服务。请帮我选择第一个小变更。”

## 3. 开始工作

建议符合你的意图后，回复：

> 请实现这项建议。将变更限制在邀请过期功能内，并保留已接受的邀请。
> 请在本地验证。不要提交 commit，也不要部署。

在实现前，智能体可能会请你确定尚未明确的行为，或选择测试方式。
完成后，请查看报告中的变更内容、已运行的检查及其结果，以及尚存的限制或待定事项。
如果某项检查无法运行，报告应明确说明。

## 日常使用

这些分组是可选项，不是必经阶段；不确定时可从 **status** 开始。

下方的 `/name` 命令采用 Antigravity App/CLI 的简写形式。Claude Code 使用 `/lusona:<name>`，Codex CLI 使用 `$lusona:<name>`。其他应用请使用上方 status 表中的相同调用方式。

### 开始或继续

| 命令 | 用途 |
| --- | --- |
| `/status` | 评估进展、剩余工作和下一步行动。 |
| `/setup` | 按需准备项目记录和长期偏好设置。 |

### 探索与规划

| 命令 | 用途 |
| --- | --- |
| `/explore` | 选择前比较想法或方向。 |
| `/frame-product` | 定义产品的用户群、问题、愿景和边界。 |
| `/map-capabilities` | 梳理能力、依赖关系和交付顺序。 |

### 定义变更

| 命令 | 用途 |
| --- | --- |
| `/specify` | 定义一项变更的行为、范围和验收标准。 |
| `/architect` | 确定有关边界、契约或归属的长期技术决策。 |
| `/design` | 创建界面草图、流程或图表以供比较。 |

### 实现与检查

| 命令 | 用途 |
| --- | --- |
| `/implement` | 实现已获授权的有限变更，或仅请求制定计划。 |
| `/refactor` | 改善代码结构，同时保持行为不变。 |
| `/review` | 审查 diff 并报告发现的问题，不修改实现。 |
| `/batch` | 针对固定选定的队列条目，执行获得明确授权的无人值守工作。 |

### 调查与比较

| 命令 | 用途 |
| --- | --- |
| `/investigate` | 用证据确定原因、观察到的行为或可行性。 |
| `/measure` | 建立基线、基准或可比较的测量结果。 |
| `/experiment` | 在有限试验中测试干预措施或比较备选方案。 |

直接加上限制条件，例如“保持公共 API 不变”或“先不要提交”。

## 需要时查阅更多信息

- [安装详情（英文）](INSTALL.md)：更新、移除、本地软件包、要求及各应用的限制。
  Antigravity App/IDE 的安装和交互行为，以及 Cursor/Xcode 的安装和技能调用均未经过测试。
- [使用指南（英文）](docs/usage.md)：更多示例、可选的 setup 及其他技能。
- [工作流程详解（英文）](docs/workflow.md)：测试、证据和恢复工作。
- [我们为什么开发 Lusona（英文）](https://blog.lusona.com/blog/why-we-built-lusona-skills/)。

当前工作副本的源码版本：**3.1.0**。从 GitHub 安装时，使用的是已提交并推送的源码；
本地变更不代表已发布版本。请参阅[变更日志（英文）](CHANGELOG.md)。

[参与贡献（英文）](CONTRIBUTING.md) · [报告问题（英文）](https://github.com/lusona/ai-skills/issues/new/choose) · [隐私政策（英文）](PRIVACY.md) · [使用条款（英文）](TERMS.md) · [MIT 许可证（英文）](LICENSE)
