# Notes: readme-translation-sync

Context: direct documentation change without a spec; the user asked whether the README needed
updating after the recent workflow changes, then authorized syncing the translations.

## 2026-11-04 — Translated READMEs behind the English README

### Question and scope

- Question: whether any README still describes behavior that the recent workflow commits changed.
- Scope: `README.md` and the four translations (`README.es.md`, `README.de.md`, `README.ja.md`,
  `README.zh-CN.md`) against commits 1f097da (one-row next-action table) and 5e39db8 (spec
  required for review-triggering changes).

### Evidence

- Method: compared the files each commit touched with `git show --stat`; grepped the translations
  for the table header, the `None for this request` label, and the four review-trigger
  conditions; checked the skill table against `plugins/lusona/skills/`, every relative link,
  and the stated version against `plugins/lusona/.claude-plugin/plugin.json`.
- Result: `README.md` and `plugins/lusona/README.md` already carried both changes. The four
  translations had every earlier change (design skill, Antigravity, Xcode, version 2.0.0, blog
  link) but not these two: the illustrative handoff still showed the prose next action, and the
  spec paragraph lacked the security boundary, persistent data, shared contract, and coordinated
  writers conditions. CONTRIBUTING.md requires the translations to stay in sync.
- Limitations: translations were checked by a bilingual read of the two passages, not by a
  native-speaker review.

### Conclusion and decisions

- Conclusion: the English README needed no change; the four translations needed the two passages
  updated.
- Decision: updated the Results and handoffs example and explanatory paragraph, and the spec
  and notes trigger sentence, in all four translations. The literal label
  `None for this request` stays in English because it is the exact string the plugin README
  prescribes. Command names, paths, and section anchors are unchanged.
- Checks: each replacement matched exactly once; every README now contains one table header and
  one `None for this request` label; no relative link in the translations is broken;
  `git diff --check` is clean; `python3 scripts/package.py` built the package with the five
  READMEs included and `python3 scripts/test_package.py` passed. `check_instructions.py` also
  passed but does not inspect README files.

## 2026-11-04 — Language quality review

Scope: the complete working-tree German, Spanish, Japanese, and Simplified Chinese READMEs,
including the pending synchronization changes, against `README.md`. The user requested a review
for native-speaker expectations. This review does not apply translation fixes; TDD is not applicable.

Result: all four translations are generally readable and largely faithful. Corrections are
recommended for the wording and meaning issues below before considering them fully polished.
The reviews were performed by AI language reviewers, not human native speakers.

### Findings

Locations refer to the working tree reviewed on 2026-11-04. Medium findings affect meaning or
the clarity of workflow requirements; low findings concern idiom or punctuation.

1. **Medium — Spanish assigns design acceptance to the wrong actor.**
   `README.es.md:268`: `Tras aceptar un borrador o elegir una opción, el agente conserva la referencia`
   normally makes the agent the subject of accepting or choosing. English explicitly assigns
   that decision to the user. Use `Cuando aceptas un borrador o eliges una opción, el agente
   conserva la referencia`.

2. **Medium — Chinese leaves the specification request ambiguous.**
   `README.zh-CN.md:193`: `你提出要求或要求跟踪` leaves the object of the request unstated.
   English means requesting a specification, not any request. Use
   `你要求编写规格说明或跟踪工作` to preserve that condition explicitly.

3. **Medium — German and Spanish translate coordinated writers too literally.**
   `README.de.md:311`: `koordinierte Schreiber` and `README.es.md:292`:
   `escritores coordinados` suggest authors rather than participants coordinating changes.
   Each file already explains the same condition more clearly in its independent-review paragraph.
   Suggested full clauses:
   - German: `eine Sicherheitsgrenze, persistente Daten oder einen gemeinsam genutzten
     technischen Vertrag betrifft oder mehrere Beteiligte ihre Änderungen aufeinander
     abstimmen müssen`.
   - Spanish: `cuando el cambio afecta a un límite de seguridad, a datos persistentes o a un
     contrato compartido, o implica modificaciones coordinadas de varios participantes`.

4. **Low — Japanese uses inconsistent, literal wording for the same condition.**
   `README.ja.md:263`: `共有される契約、複数の書き手の調整` reads less naturally than
   the terminology already used at lines 223–224. Reuse
   `共有インターフェースなどの契約、複数の担当者による共同編集`.
   This improves terminology and idiom; it is not an established policy error.

5. **Medium — German makes report length the criterion.**
   `README.de.md:341`: `Ausführliche Berichte` means detailed reports, while English
   `substantive reports` concerns material content regardless of length. Use
   `Berichte über wesentliche Arbeitsergebnisse nennen das Ergebnis, die Belege dafür und
   einen gegebenenfalls nötigen nächsten Schritt.` Japanese has a similar precision issue
   at `README.ja.md:286` (`詳しい報告`); suggested wording:
   `作業結果の報告には、結果、その根拠、次の作業を示します。`.

6. **Low — German and Japanese duplicate punctuation around the blog language note.**
   At `README.de.md:25`, change `...). (auf Englisch).` to `...) (auf Englisch).`.
   At `README.ja.md:21`, change `...).（英語）。` to `...)（英語）。`.

### Optional polish

- German `README.de.md:177`: `deinen Nutzer` → `dein Benutzerkonto` for user-scoped installation.
- German `README.de.md:268`: `Die Fragen richten sich nach den offenen Entscheidungen der Arbeit.`
  → `Die Fragen richten sich danach, welche Entscheidungen noch offen sind.`
- Spanish `README.es.md:228`: `te pregunta si revisarla exige más permisos`
  → `te consulta cuando revisarla exige permisos adicionales` to remove conditional ambiguity.
- Japanese `README.ja.md:256`: `根拠とする実行記録へ正確にリンクします`
  → `根拠とする具体的な実行記録へのリンクを記載します` to preserve the emphasis on
  identifying the particular runs, rather than linking accurately.
- Japanese `README.ja.md:247` and `:251`: prefer `スクリーンショットを取得` and
  `レンダリングとスクリーンショット取得のツール` to wording about photographing the UI.
- Chinese `README.zh-CN.md:193`: `多个协同写入方` could reuse the clearer
  `多个参与者协同修改` wording already present at line 173.
- The ready-to-send TDD prompts can preserve the literal `targeted` identifier for consistency.
  Translating “targeted TDD” is not itself a confirmed defect; the policy lists already retain
  the identifiers, and the English prompt also uses descriptive wording.

### Verification and limits

- Independent AI language reviewers: `/root/german_review`, `/root/spanish_review`, and
  `/root/east_asian_review`; all returned completed reviews without editing files. The coordinator
  reconciled findings against the English source and the affected passages.
- All 65 Markdown link targets in each translation resolve for local paths and fragments;
  external URLs were excluded from reachability checks.
- All fenced Bash command blocks match English exactly. Each translation retains one literal
  `None for this request` completion label. `git diff --check` passed.
- No translation corrections were applied. Packaging, installation, interactive behavior, and
  rendered layout were not retested for this review. Human native-speaker validation was not performed.

## 2026-11-04 — Applied language corrections

- Authority: the user requested, “please make those changes,” after the review.
- Applied all six finding groups and optional polish in the four translated READMEs. Preserved
  the prior synchronization edits, command blocks, link targets, and literal completion label.
  The handoff prompts now retain the `targeted` identifier in all four languages; the German
  table description specifies one data row.
- TDD: not applicable to these editorial documentation corrections. Verification used content,
  link, anchor, command-parity, whitespace, and packaging checks; no behavioral tests were added.
- Editor: `/root/translation_edits`. Independent reviewer: `/root/east_asian_review`, which
  checked the actual changes in all four translations against English and the retained findings
  and reported no actionable defects or meaning regressions. The coordinator inspected the diff.
- Checks: all 65 Markdown links in each translation were inspected; local paths and fragments
  resolve. Bash blocks match English, and each translation retains one completion label.
  `git diff --check` passed. `python3 scripts/package.py --output
  tmp/translation-language-fixes-20261105` built successfully; `python3 scripts/test_package.py`
  passed all 10 tests.
- Limits: external URL reachability, installation, interactive behavior, rendered layout, and
  human native-speaker validation were not tested. No skill definitions or manifests changed.
- Correction rounds: total 1; consecutive rounds without material progress 0. The reviewed
  findings are resolved; the earlier findings above document the pre-correction state.

## Current handoff

- Authorized translation corrections are complete and verified. The user subsequently authorized
  grouping and committing the changes; translations and this record form one local commit.
- Next action: None for this request. Pushing and publication are not authorized.
