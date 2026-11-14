# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona hilft Programmieragenten, eine Produkt- oder Entwicklungsanfrage bis zu einem geprüften
Ergebnis umzusetzen. Beginne in einem bestehenden Projekt mit einer kleinen Änderung.

> [!TIP]
> Bereits installiert? Beginne mit `/status` und verwende den [Befehl für deine Anwendung](#2-eine-empfehlung-erhalten).

## 1. Für deine Anwendung installieren

Verwende nur die Anleitung für deine Anwendung. Schließe zuerst deren Einrichtung und Anmeldung ab.

**Claude Code** — im Terminal ausführen:

```bash
claude plugin marketplace add https://github.com/lusona/ai-skills.git
claude plugin install lusona@lusona-ai-skills --scope user
```

**Codex** — im Terminal ausführen:

```bash
codex plugin marketplace add https://github.com/lusona/ai-skills.git
codex plugin add lusona@lusona-ai-skills
```

**Antigravity** — im Terminal ausführen:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
agy plugin list --json
```

Prüfe, ob `lusona` aktiviert ist. Prüfe in der App **Customizations > Installed**;
in der eigenständigen IDE **Customizations** im Seitenbereich des Agenten.

**Cursor** — öffne **Customize > From GitHub Repository**, gib
`https://github.com/lusona/ai-skills` ein, wähle **Lusona Skills**, klicke auf **Install**
und wähle den Projekt- oder Benutzerbereich.

**Xcode 27** — aktiviere unter **Settings > Intelligence** einen Programmieragenten. Klicke unter
**Agents > Plug-ins** auf **Add Plug-in > Add from URL > Continue**, gib
`https://github.com/lusona/ai-skills` ein, wähle Lusonas Skills und klicke auf **Install**.
Eine Installation in der eigenständigen CLI installiert das Plugin nicht in Xcode.

> [!WARNING]
> Installiere das native Plugin, nicht Vercel Skills (`npx skills@latest`); einzelnen Skills fehlen die gemeinsamen Ressourcen.

## 2. Eine Empfehlung erhalten

Starte eine neue Agentensitzung in deinem Projekt und rufe **status** auf:

| Anwendung | status aufrufen |
| --- | --- |
| Claude Code | `/lusona:status` |
| Codex CLI | `$lusona:status` |
| Codex-Desktop-App | `$lusona:status` oder `/lusona:status`, oder `status` in der Skill-Oberfläche auswählen |
| Antigravity App und CLI | `/status` |
| Eigenständige Antigravity IDE | Bitte: `Verwende Lusonas status-Skill.` |
| Cursor oder Xcode | `/` eingeben und Lusonas `status`-Skill auswählen |

Füge dann diese Anfrage ein und passe die Funktion an dein Projekt an:

> Teameinladungen sollen nach sieben Tagen ablaufen. Untersuche dieses Projekt und empfehle
> eine kleine nächste Änderung. Sag mir, was bereits vorhanden ist und was fehlt. Ändere noch keine Dateien.

Du erhältst eine Einschätzung des aktuellen Projekts und eine empfohlene nächste Aktion.
Wenn der Agent eine Entscheidung braucht, antworte in einfachen Worten. Zum Beispiel:

> Zähle sieben Tage ab dem Versand der Einladung. Lass angenommene Einladungen unverändert.

Für ein leeres Projekt: „Ich möchte einen Dienst für Teameinladungen entwickeln. Hilf mir, die erste kleine Änderung auszuwählen.“

## 3. Die Arbeit starten

Wenn die Empfehlung deinem Wunsch entspricht, antworte:

> Setze diese Empfehlung um. Beschränke die Änderung auf den Ablauf von Einladungen und erhalte
> angenommene Einladungen. Prüfe das Ergebnis lokal. Erstelle keinen Commit und führe kein Deployment durch.

Der Agent kann dich vor der Umsetzung bitten, fehlendes Verhalten zu klären oder ein Testvorgehen
zu wählen. Achte am Ende darauf, was geändert wurde, welche Prüfungen mit welchen Ergebnissen
liefen und welche Einschränkungen oder Entscheidungen offen sind. Konnte eine Prüfung nicht
laufen, muss der Bericht das angeben.

## Im Alltag

Diese Gruppen sind Auswahlmöglichkeiten, keine Pflichtphasen; beginne bei Unsicherheit mit **status**.

Die Befehle `/name` unten verwenden die Kurzform von Antigravity App/CLI. Verwende in Claude Code `/lusona:<name>` und in Codex CLI `$lusona:<name>`. Nutze in anderen Anwendungen dieselbe Aufrufmethode wie in der status-Tabelle oben.

### Starten oder fortsetzen

| Befehl | Verwende ihn, um |
| --- | --- |
| `/status` | Fortschritt, verbleibende Arbeit und die nächste Aktion zu bewerten. |
| `/setup` | Optional Projektaufzeichnungen und dauerhafte Präferenzen vorzubereiten. |

### Erkunden und planen

| Befehl | Verwende ihn, um |
| --- | --- |
| `/explore` | Ideen oder Richtungen vor einer Entscheidung zu vergleichen. |
| `/frame-product` | Zielgruppe, Problem, Vision und Grenzen eines Produkts zu definieren. |
| `/map-capabilities` | Fähigkeiten, Abhängigkeiten und Lieferreihenfolge festzulegen. |

### Eine Änderung definieren

| Befehl | Verwende ihn, um |
| --- | --- |
| `/specify` | Verhalten, Umfang und Akzeptanzkriterien einer Änderung zu definieren. |
| `/architect` | Eine dauerhafte technische Entscheidung zu Grenzen, Verträgen oder Zuständigkeiten zu treffen. |
| `/design` | UI-Entwürfe, Abläufe oder Diagramme zum Vergleichen zu erstellen. |

### Umsetzen und prüfen

| Befehl | Verwende ihn, um |
| --- | --- |
| `/implement` | Eine autorisierte, begrenzte Änderung umzusetzen oder nur einen Plan anzufordern. |
| `/refactor` | Die Codestruktur unter Beibehaltung des Verhaltens zu verbessern. |
| `/review` | Einen Diff zu prüfen und Befunde ohne Änderungen an der Implementierung zu melden. |
| `/batch` | Explizit autorisierte unbeaufsichtigte Arbeit an einer festen Auswahl von Warteschlangeneinträgen auszuführen. |

### Untersuchen und vergleichen

| Befehl | Verwende ihn, um |
| --- | --- |
| `/investigate` | Ursache, beobachtetes Verhalten oder Machbarkeit durch Belege festzustellen. |
| `/measure` | Eine Ausgangsbasis, einen Benchmark oder vergleichbare Messungen zu ermitteln. |
| `/experiment` | Eine Maßnahme zu testen oder Alternativen in einem begrenzten Versuch zu vergleichen. |

Ergänze Einschränkungen in eigenen Worten, etwa „Lass die öffentliche API unverändert“ oder „Erstelle noch keinen Commit“.

## Weitere Informationen bei Bedarf

- [Installationsdetails (Englisch)](INSTALL.md): Updates, Entfernen, lokale Pakete, Voraussetzungen und Einschränkungen je Anwendung.
  Installation und interaktives Verhalten in Antigravity App/IDE sowie Installation und
  Skill-Aufrufe in Cursor/Xcode wurden nicht getestet.
- [Nutzungsanleitung (Englisch)](docs/usage.md): weitere Beispiele, optionales setup und andere Skills.
- [Workflow-Details (Englisch)](docs/workflow.md): Tests, Belege und Fortsetzen der Arbeit.
- [Warum wir Lusona entwickelt haben (Englisch)](https://blog.lusona.com/blog/why-we-built-lusona-skills/).

Version des Quellcodes in dieser Arbeitskopie: **3.1.0**. Die Installation über GitHub verwendet
committete und gepushte Quellen; lokale Änderungen begründen keine veröffentlichte Version.
Siehe das [Änderungsprotokoll (Englisch)](CHANGELOG.md).

[Mitwirken (Englisch)](CONTRIBUTING.md) · [Problem melden (Englisch)](https://github.com/lusona/ai-skills/issues/new/choose) · [Datenschutz (Englisch)](PRIVACY.md) · [Nutzungsbedingungen (Englisch)](TERMS.md) · [MIT-Lizenz (Englisch)](LICENSE)
