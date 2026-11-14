# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona は、コーディングエージェントがプロダクトや開発の依頼を受け、結果を確認するまでの作業を支援します。
既存のプロジェクトで、小さな変更から始めてください。

> [!TIP]
> インストール済みなら、[使用するアプリのコマンド](#2-推奨を受け取る)で `/status` から始めてください。

## 1. 使用するアプリにインストールする

使用するアプリの手順だけを実行してください。先にアプリの設定と認証を済ませます。

**Claude Code** — ターミナルで実行：

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

**Codex** — ターミナルで実行：

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

**Antigravity** — ターミナルで実行：

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

`lusona` が有効になっていることを確認します。App では **Customizations > Installed**、
スタンドアロン IDE ではエージェントのサイドパネルの **Customizations** を確認してください。

**Cursor** — **Customize > From GitHub Repository** を開き、
`https://github.com/lusona/ai-skills` を入力します。**Lusona Skills** を選び、**Install** をクリックし、
プロジェクトまたはユーザーの範囲を選びます。

**Xcode 27** — **Settings > Intelligence** でコーディングエージェントを有効にします。
**Agents > Plug-ins** で **Add Plug-in > Add from URL > Continue** をクリックし、
`https://github.com/lusona/ai-skills` を入力します。Lusona のスキルを選び、**Install** をクリックします。
スタンドアロン CLI へのインストールでは、Xcode にプラグインはインストールされません。

> [!WARNING]
> Vercel Skills（`npx skills@latest`）ではなく、ネイティブプラグインをインストールしてください。個別のスキルには共有リソースが含まれません。

## 2. 推奨を受け取る

プロジェクトで新しいエージェントセッションを開始し、**status** を呼び出します：

| アプリ | status の呼び出し方 |
| --- | --- |
| Claude Code | `/lusona:status` |
| Codex CLI | `$lusona:status` |
| Codex デスクトップアプリ | `$lusona:status` または `/lusona:status`、またはスキル選択画面で `status` を選ぶ |
| Antigravity App と CLI | `/status` |
| Antigravity スタンドアロン IDE | `Lusona の status スキルを使ってください。`と依頼する |
| Cursor または Xcode | `/` を入力し、Lusona の `status` スキルを選ぶ |

次の依頼を貼り付け、機能の内容を自分のプロジェクトに合わせて変えます：

> チームへの招待を7日後に期限切れにしたいです。このプロジェクトを調べ、次に行う小さな変更を1つ提案してください。
> すでに実装されていることと、不足していることを教えてください。まだファイルは変更しないでください。

現在のプロジェクトの評価と、次に行う作業の推奨が返されます。エージェントから判断を求められたら、
普段の言葉で答えてください。例：

> 招待を送信した時点から7日間としてください。承諾済みの招待は変更しないでください。

空のプロジェクトなら：「チームへの招待サービスを作りたいです。最初の小さな変更を選ぶのを手伝ってください。」

## 3. 作業を始める

推奨が希望に合っていれば、次のように返信します：

> その提案を実装してください。変更は招待の期限切れに限定し、承諾済みの招待は維持してください。
> ローカルで検証してください。コミットやデプロイはしないでください。

実装前に、未定の動作やテスト方法についてエージェントから質問される場合があります。
最後に、変更内容、実行したチェックとその結果、残る制約や判断事項を確認してください。
実行できなかったチェックがあれば、報告にその旨が記載されるはずです。

## 日常の使い方

これらのグループは選択肢であり、必須の段階ではありません。迷ったら **status** から始めてください。

以下の `/name` コマンドは Antigravity App/CLI の短縮形式です。Claude Code では `/lusona:<name>`、Codex CLI では `$lusona:<name>` を使います。他のアプリでは、上の status 表と同じ呼び出し方法を使ってください。

### 開始・再開する

| コマンド | 用途 |
| --- | --- |
| `/status` | 進捗、残りの作業、次のアクションを確認する。 |
| `/setup` | 必要に応じてプロジェクトの記録と継続的な設定を準備する。 |

### 検討・計画する

| コマンド | 用途 |
| --- | --- |
| `/explore` | 選択する前にアイデアや方向性を比較する。 |
| `/frame-product` | 製品の対象ユーザー、問題、ビジョン、境界を定義する。 |
| `/map-capabilities` | 機能、依存関係、提供順序を整理する。 |

### 変更を定義する

| コマンド | 用途 |
| --- | --- |
| `/specify` | 1つの変更の動作、範囲、受け入れ基準を定義する。 |
| `/architect` | 境界、契約、所有責任に関する長期的な技術判断を行う。 |
| `/design` | 比較用の UI モックアップ、フロー、図を作成する。 |

### 実装・確認する

| コマンド | 用途 |
| --- | --- |
| `/implement` | 許可された範囲の変更を実装する、または計画だけを依頼する。 |
| `/refactor` | 動作を維持しながらコード構造を改善する。 |
| `/review` | 差分をレビューし、実装を編集せずに指摘事項を報告する。 |
| `/batch` | 固定された選択済みのキュー項目について、明示的に許可された無人作業を実行する。 |

### 調査・比較する

| コマンド | 用途 |
| --- | --- |
| `/investigate` | 根拠に基づいて原因、観測された動作、実現可能性を明らかにする。 |
| `/measure` | ベースライン、ベンチマーク、比較可能な測定値を確立する。 |
| `/experiment` | 範囲を限定した試行で介入を検証し、または代替案を比較する。 |

「公開 API は変更しないでください」「まだコミットしないでください」など、制約も普段の言葉で添えてください。

## 必要に応じて読む

- [インストールの詳細（英語）](INSTALL.md)：更新、削除、ローカルパッケージ、要件、アプリごとの制約。
  Antigravity App/IDE のインストールと対話動作、Cursor/Xcode のインストールとスキル呼び出しは未検証です。
- [使い方ガイド（英語）](docs/usage.md)：他の例、任意の setup、その他のスキル。
- [ワークフローの詳細（英語）](docs/workflow.md)：テスト、根拠、作業の再開。
- [Lusona を開発した理由（英語）](https://blog.lusona.com/blog/why-we-built-lusona-skills/)。

この作業コピーのソースバージョン：**3.1.0**。GitHub からのインストールでは、コミットしてプッシュしたソースを
使用します。ローカルの変更は、公開済みのリリースを意味しません。[変更履歴（英語）](CHANGELOG.md)を参照してください。

[貢献（英語）](CONTRIBUTING.md) · [問題の報告（英語）](https://github.com/lusona/ai-skills/issues/new/choose) · [プライバシー（英語）](PRIVACY.md) · [利用規約（英語）](TERMS.md) · [MIT ライセンス（英語）](LICENSE)
