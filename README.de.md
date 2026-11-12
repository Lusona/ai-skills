# Lusona Skills

[English](README.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Lusona umfasst 14 Skills für Produkt- und Entwicklungsarbeit mit Programmieragenten. Jeder
Skill deckt eine Verantwortung ab, etwa eine Änderung zu spezifizieren, umzusetzen oder zu
prüfen. Alle Skills folgen denselben acht Prinzipien des Arbeitszyklus, führen Aufzeichnungen
unter `docs/lusona/` im Projekt und beenden jede Aufgabenantwort mit Status, Belegen und der
nächsten Aktion.

Für Claude Code, Codex, [Cursor](INSTALL.md#cursor), [Programmieragenten in Xcode 27](INSTALL.md#xcode) und [Google Antigravity App, CLI und IDE](INSTALL.md#antigravity) · Version des Quellcodes in dieser Arbeitskopie: **3.0.0**

> [!WARNING]
> Installiere Lusona nicht mit Vercel Skills (`npx skills@latest`); nutze die [Installation als natives Plugin](#installation).

Warum wir Lusona Skills entwickelt haben: [Why we built Lusona Skills](https://blog.lusona.com/blog/why-we-built-lusona-skills/).

Diese README beschreibt den Quellcode dieser Arbeitskopie. Die Installation über GitHub nutzt
Quellen, die per Commit erfasst und gepusht wurden; lokale Änderungen begründen keine
veröffentlichte Version.

![Lusona-Arbeitszyklus, Prinzipien und Skill-Gruppen](plugins/lusona/assets/workflow-loop.svg)

Der Kreis zeigt, wie die Arbeit weitergeht: wählen, ausführen, prüfen und wiederholen. Wähle
Skills nach dem aktuellen Bedarf; auf jeden Skill kann jeder andere folgen.

## Inhalt

- [Prinzipien des Arbeitszyklus](#prinzipien-des-arbeitszyklus)
- [Beginnen und einen Skill wählen](#beginnen-und-einen-skill-wählen)
- [Befugnisse und TDD-Stufe](#befugnisse-und-tdd-stufe)
- [Entscheidungen und Überarbeitungen](#entscheidungen-und-überarbeitungen)
- [Belege und Abschluss](#belege-und-abschluss)
- [Aufzeichnungen und Fortsetzung](#aufzeichnungen-und-fortsetzung)
- [Antworten und nächste Aktionen](#antworten-und-nächste-aktionen)
- [Installation](#installation)
- [Referenzen](#referenzen)
- [Mitwirken](#mitwirken)
- [Lizenz](#lizenz)
- [Entwicklung](#entwicklung)

## Prinzipien des Arbeitszyklus

Jeder Skill arbeitet in einem Zyklus: die nächste klar begrenzte Aktion wählen, ausführen, das
Ergebnis prüfen und dies wiederholen, bis das angeforderte Ergebnis erreicht ist. Ziel ist es,
System und Entwurf mit zunehmendem Verständnis zu verfeinern. Jeder Skill wendet diese acht
Prinzipien an. Der [Workflow-Leitfaden](plugins/lusona/references/workflow-guide.md#loop-principles)
definiert sie.

| ID | Prinzip | Was es für dich bedeutet |
| --- | --- | --- |
| P1 | Keine feste Reihenfolge | Der Agent wählt den nächsten Skill nach dem ungelösten Bedarf. Auf jeden Skill kann jeder andere folgen; eine Änderung nutzt nur die Skills, die ihre offene Arbeit benötigt. |
| P2 | Verfeinerung | Jeder Durchlauf vergleicht sein Ergebnis mit dem angestrebten Ergebnis und trennt Fakten von Annahmen. Er übernimmt Ergebnis, akzeptierte Entscheidungen, Befugnisse, TDD-Stufe, Belege und Unsicherheit in den nächsten Durchlauf. |
| P3 | Frühere Entscheidungen sind Eingaben | Widerspricht eine neue Eingabe einer akzeptierten Entscheidung, weist der Agent weder die Eingabe zurück noch ignoriert er die Entscheidung. Er benennt den Konflikt und prüft die Entscheidung gemeinsam mit dir neu. |
| P4 | Dokumentierte Ablösung | Eine abgelöste Entscheidung wird mit Datum und Quelle gekennzeichnet; ihre Begründung bleibt erhalten. Betroffene Aufzeichnungen werden abgeglichen. Eine veraltete Aufzeichnung kann eine abgelöste Wahl nicht wieder in Kraft setzen. |
| P5 | Belege statt Behauptungen | Der Agent behauptet Verhalten und Abschluss nur auf Grundlage beobachteter Prüfungen. Eine fehlgeschlagene oder nicht ausgeführte Pflichtprüfung verhindert den Abschluss. |
| P6 | Die Entscheidungsbefugnis bleibt beim Nutzer | Spezifikationen, Pläne, ADRs und Warteschlangenstatus erteilen keine Freigabe zur Implementierung. Änderungen an akzeptierten Ergebnissen, Verträgen, der TDD-Stufe oder folgenreichen Zusagen brauchen deine Entscheidung. |
| P7 | Begrenzte Arbeit fortsetzen | Der Agent führt die nächste freigegebene Aktion ohne weiteren Befehl aus, beendet Nachfragen, die die nächste Aktion nicht ändern können, und pausiert nur die betroffene Arbeit. |
| P8 | Jede Antwort nennt die nächste Aktion | Jede Aufgabenantwort endet mit einer nächsten Aktion und ihrer Zuständigkeit oder nennt den Grund, warum keine Aktion mehr bleibt. |

## Beginnen und einen Skill wählen

Beginne mit **status**, wenn du in ein Projekt einsteigst, Arbeit wieder aufnimmst oder
entscheidest, was Aufmerksamkeit braucht. Der Skill bewertet lesbare Aufzeichnungen und Belege,
nennt alle bekannten Restarbeiten und empfiehlt die nächste Aktion. Er funktioniert auch ohne
vorhandene Lusona-Aufzeichnungen. Eine Statusanfrage erteilt und entzieht keine Ausführungsbefugnis.

Wähle den Skill nach dem aktuellen Bedarf (P1). Die Zeilen bilden keine Reihenfolge: Eine
freigegebene Anfrage mit benanntem Verhalten und Umfang geht ohne **specify** zu **implement**.

| Skill | Verwenden, wenn |
| --- | --- |
| [status](plugins/lusona/skills/status/SKILL.md) | Du Orientierung, Fortschritt, Restarbeit oder Möglichkeiten zur Fortsetzung wissen möchtest |
| [explore](plugins/lusona/skills/explore/SKILL.md) | Du vor einer Wahl über eine Richtung, Option oder Zukunft nachdenken möchtest |
| [frame-product](plugins/lusona/skills/frame-product/SKILL.md) | Zielgruppe, Problem, Vision, Ergebnisse oder Grenzen eines Produkts undefiniert sind oder sich ändern |
| [map-capabilities](plugins/lusona/skills/map-capabilities/SKILL.md) | Funktionsabdeckung, Abhängigkeiten oder Lieferreihenfolge geklärt werden müssen |
| [specify](plugins/lusona/skills/specify/SKILL.md) | Angestrebtes Verhalten, Umfang oder Akzeptanzkriterien einer Änderung definiert werden müssen |
| [architect](plugins/lusona/skills/architect/SKILL.md) | Eine technische Entscheidung über Grenzen, Verträge oder Zuständigkeiten mit dauerhaften Folgen offen ist |
| [design](plugins/lusona/skills/design/SKILL.md) | Eine Ansicht, ein Ablauf, ein Zustand oder eine Beziehung sichtbar sein muss, um sie zu beurteilen oder auszuwählen |
| [implement](plugins/lusona/skills/implement/SKILL.md) | Eine Änderung zur Implementierung freigegeben ist oder du nur einen Plan möchtest |
| [review](plugins/lusona/skills/review/SKILL.md) | Ein Diff vor dem Abschluss gegen das angestrebte Verhalten geprüft werden muss |
| [refactor](plugins/lusona/skills/refactor/SKILL.md) | Bestehender Code ein konkretes Strukturproblem hat und sein Verhalten gleich bleiben muss |
| [investigate](plugins/lusona/skills/investigate/SKILL.md) | Eine Frage zu Ursache, beobachtetem Verhalten oder Machbarkeit Belege braucht |
| [measure](plugins/lusona/skills/measure/SKILL.md) | Eine Entscheidung einen Ausgangswert, Benchmark oder vergleichbare Beobachtungen braucht |
| [experiment](plugins/lusona/skills/experiment/SKILL.md) | Eine Erprobung nötig ist, um einen Ansatz anzunehmen, abzulehnen oder zu verfeinern |
| [batch](plugins/lusona/skills/batch/SKILL.md) | Du unbeaufsichtigte Arbeit an ausgewählten Warteschlangeneinträgen freigibst oder einen aufgezeichneten Batch fortsetzt |

Der [Workflow-Leitfaden](plugins/lusona/references/workflow-guide.md) nennt die Persona und das
Ergebnis jedes Skills, die Zuordnungstabelle und die Begriffe. Der Wechsel zwischen Skills
braucht keine neue Freigabe; du musst nicht jeden Übergang anweisen.

Rufe einen Skill in deiner Anwendung auf:

- Claude Code: `/lusona:<skill>`, zum Beispiel `/lusona:status`.
- Codex: Wähle den Lusona-Skill in der Skill-Oberfläche.
- Cursor: Gib `/` im Agent-Chat ein und wähle den Skill.
- Xcode: Gib `/` in einer Agentenunterhaltung ein und wähle den installierten Skill.
- Antigravity App und CLI: `/<skill>`, zum Beispiel `/status`. Prüfe in der eigenständigen IDE
  **Customizations** und nenne den Lusona-Skill in deiner Anfrage.

[Installiere Lusona](#installation), bevor du die Skills nutzt. Eine Skill-Anfrage nennt den
Skill, das Ergebnis oder die Eingabeaufzeichnung und den freigegebenen Umfang. Zum Beispiel:

> **status:** Bewerte dieses Projekt anhand der vorhandenen Aufzeichnungen und des Arbeitsbaums.
> Nenne die verbleibende Arbeit und empfiehl, wo ich anfangen sollte.

> **explore:** Hilf mir, Einladungslinks mit Einladungen ausschließlich per E-Mail zu vergleichen.
> Erkläre die Folgen für unser Supportteam, bevor wir uns entscheiden. Führe dieses Gespräch
> im Chat; speichere keine Dateien.

> **design:** Vergleiche zwei Einladungsabläufe mit unseren vorhandenen Ansichten,
> Navigationselementen und Texten. Zeige die Schritte und den Zustand einer abgelaufenen
> Einladung und erkläre die Vor- und Nachteile jeder Option. Erstelle nur den visuellen
> Entwurf; implementiere die Oberfläche nicht.

> **implement:** Lass Einladungen nach sieben Tagen ablaufen. Lass bereits angenommene
> Einladungen unverändert. Fertig bedeutet: Einladungen, die älter als sieben Tage sind,
> werden abgelehnt, angenommene Einladungen bleiben unverändert, und die Testsuite besteht.
> Nutze die TDD-Stufe `targeted` für die Ablaufgrenze. Prüfe lokal; führe kein Deployment durch.

## Befugnisse und TDD-Stufe

Du entscheidest über die Befugnisse (P6). Diese Regeln gelten für jeden Skill:

- Spezifikationen, Pläne, ADRs und Warteschlangenstatus erteilen keine Freigabe zur
  Implementierung. Gespräche und rein lesende Reviews tun dies ebenfalls nicht.
- Die Auswahl einer Aufgabe zur Implementierung gibt nicht den Rest der zugehörigen Änderung frei.
- Der Agent fragt dich vor destruktiven Aktionen sowie vor Änderungen an akzeptierten
  Ergebnissen, Verträgen, der TDD-Stufe oder folgenreichen Zusagen.
- Der Agent committet, pusht oder veröffentlicht nur mit deiner Befugnis. Freigegebene
  Implementierung und Refactoring schließen lokale Commits ein.
- Eine reine Planungsanfrage an **implement** endet mit einem vorgeschlagenen Vorgehen und
  gibt keine Implementierung frei.
- **batch** führt unbeaufsichtigte Arbeit nur an einer festen Auswahl von Warteschlangeneinträgen
  aus, die du ausdrücklich freigibst. Es nutzt höchstens 4 gleichzeitige Zuweisungen oder 5,
  wenn du 5 auswählst, begrenzt durch die Kapazität der Anwendung. Das Korrekturbudget beträgt
  2 Korrekturrunden pro Eintrag, sofern du keine andere Zahl freigibst.

Implementierung erfordert eine ausdrücklich gewählte TDD-Stufe. Es gibt keinen Standardwert.

| TDD-Stufe | Anforderung |
| --- | --- |
| `none` | Keine Pflicht, Tests zuerst zu schreiben; vereinbarte Verifikation und Repository-Prüfungen gelten weiterhin |
| `targeted` | Für benannte Verhaltensweisen zuerst Tests schreiben |
| `strict` | Für jedes neue oder geänderte testbare Verhalten zuerst Tests schreiben |

Wähle die Stufe in deiner Anfrage oder als dauerhafte Vorgabe in der `docs/lusona/README.md`
des Projekts oder den Agentenanweisungen (`CLAUDE.md` oder `AGENTS.md`), zum Beispiel
`TDD: targeted for validation and persistence boundaries`. Bis eine Stufe gewählt ist, definiert
und plant der Agent nur; dann fragt er dich mit einer Empfehlung. Er dokumentiert Stufe und
Quelle und bittet um eine geänderte Stufe, wenn die gewählte Abfolge nicht umsetzbar ist.

Innerhalb dieser Befugnisse arbeitet der Agent ohne weiteren Befehl weiter (P7). Er führt die
nächste begrenzte Aktion aus, nimmt innerhalb freigegebener Arbeit ohne neue Anfrage Messungen
oder Experimente vor und beendet Nachfragen, deren Antworten die nächste Aktion nicht ändern
können. Wenn verfügbar, nutzt er das native Fragewerkzeug der Anwendung und empfiehlt eine
Antwort. Weder Schweigen noch eine vorausgewählte Option gelten als Zustimmung. Während er
wartet, pausiert nur die betroffene Arbeit; der Agent nennt die Bedingung für ihre Fortsetzung.

Der Agent, der mit dir spricht, ist der Koordinator. Bei Aufgaben jeder Größe delegiert er
Facharbeit an untergeordnete Agenten und integriert und prüft ihre Ergebnisse. Ist Delegation
verboten oder nicht verfügbar, arbeitet er lokal und sagt dies. Siehe
[Delegation](plugins/lusona/references/delegation.md) für Zuweisungen und
[Modellzuordnung](plugins/lusona/references/delegation.md#model-routing).

## Entscheidungen und Überarbeitungen

Akzeptierte Entscheidungen sind Eingaben für spätere Arbeit (P3). Widerspricht eine neue
Anforderung, Spezifikation, Messung oder ein Experimentergebnis einer akzeptierten Entscheidung,
führt der Agent diese Schritte aus:

1. Er nennt Entscheidung, Quelle, Konflikt und betroffene Annahmen in der Antwort und in der
   zuständigen Aufzeichnung.
2. Er zeigt dir die Optionen und empfiehlt eine Antwort.
3. Er vereinbart mit dir ein Ergebnis: beibehalten, teilweise überarbeitet oder abgelöst.
   Die erneute Prüfung einer Entscheidung gibt die Änderung nicht frei.
4. Er dokumentiert das Ergebnis, bevor davon abhängige Arbeit weitergeht.
5. Er setzt nicht betroffene Arbeit innerhalb bestehender Befugnisse fort.

Die Aufzeichnung bewahrt die Geschichte jeder Entscheidung (P4). Eine überarbeitete oder
abgelöste Entscheidung behält ihren Text und ihre Begründung, mit Datum und Quelle deiner
Antwort. Eine abgelöste Entscheidung verlinkt ihren Ersatz. Der Agent aktualisiert abhängige
Aufzeichnungen, Zuweisungen und Übergaben innerhalb seiner Schreibzuständigkeit, meldet nötige
Korrekturen anderer Zuständiger und arbeitet unter der Überarbeitung weiter. Eine Aufzeichnung,
die noch eine abgelöste Entscheidung enthält, wird korrigiert oder gemeldet, nicht befolgt.
Siehe [Überarbeitungen](plugins/lusona/references/revisions.md).

Eine Folgeanfrage ändert den Umfang des aktuellen Ziels und erhält den Fortschritt. Sie ersetzt
das Ziel nur, wenn sie es ausdrücklich aufhebt oder ersetzt oder ein unvereinbares Ziel verlangt.

## Belege und Abschluss

Der Agent berichtet Verhalten nur aus beobachteten Prüfungen und nennt nicht ausgeführte und
fehlgeschlagene Prüfungen (P5). Abschluss erfordert das freigegebene Ergebnis, seine Kriterien,
bestandene Pflichtprüfungen und jede erforderliche menschliche Abnahme. Bestandene Tests
belegen keine menschliche Abnahme.

- **Belege für Tests vor dem Code.** Für jedes Verhalten mit Test-zuerst-Pflicht beobachtet der
  Agent vor der Änderung von Produktionscode den vorgesehenen Fehlschlag und danach den
  bestandenen Test. Ein Einrichtungsfehler belegt den vorgesehenen Fehlschlag nicht. Siehe
  [TDD](plugins/lusona/references/tdd.md).
- **Korrekturgrenzen.** Nach 2 aufeinanderfolgenden Korrekturrunden ohne wesentlichen Fortschritt
  beendet der Agent die Korrektur dieses Fehlers, berichtet die Belege und setzt nicht betroffene
  Arbeit fort. Nach insgesamt 4 Runden fragt er dich vor jeder weiteren Runde. In einem Batch
  gilt stattdessen das Korrekturbudget. Siehe
  [Korrekturen](plugins/lusona/references/corrections.md).
- **Unabhängiges Review.** Ein Review durch einen Agenten, der die Änderung nicht geschrieben
  hat, ist nötig, wenn deine oder die Repository-Regeln es verlangen oder die Änderung
  Sicherheitsgrenzen, persistente Daten oder gemeinsam genutzte technische Verträge betrifft
  oder mehrere Beteiligte ihre Änderungen aufeinander abstimmen. Lokale Arbeit erfüllt dies
  nie; ist das Review nicht verfügbar, meldet der Agent die Anforderung als unerfüllt.
- **Studien.** **investigate** beantwortet diagnostische Fragen; **measure** und **experiment**
  sind Studien. Unsicherheit allein startet keine Studie. Eine Studie, die die Anfrage nicht
  verlangt, braucht deine ausdrückliche oder dauerhafte Freigabe sowie einen endlichen Umfang
  und ein Ressourcenbudget. Belege, auf denen eine Entscheidung beruht, werden unter
  `docs/lusona/evidence/` im Projekt gespeichert. Siehe
  [Belege](plugins/lusona/references/evidence.md).
- **Visuelle Referenzen.** **explore**, **specify**, **architect** und **design** bieten 2-4
  visuelle Optionen, wenn eine Wahl von Anordnung, Struktur, Ablauf oder Erscheinungsbild abhängt.
  UI-Entwürfe werden im Browser geöffnet, oder der Agent nennt den absoluten HTML-Pfad;
  Diagramme stehen in Mermaid-Codeblöcken. Nach deiner Wahl wird die Referenz mit ihren
  verbindlichen Vorgaben in `docs/lusona/visuals/<record-id>/` aufbewahrt. **implement** nennt
  den Status jeder verbindlichen Vorgabe; **review** meldet jede als erfüllt, nicht erfüllt
  oder ungeprüft. Siehe [visuelle Darstellungen](plugins/lusona/references/visuals.md).

## Aufzeichnungen und Fortsetzung

Der Agent speichert wesentliche Ergebnisse vor Übergabe oder Abschluss unaufgefordert:
Entscheidungen, Vereinbarungen, Belege, Erkenntnisse, Übergaben und Gesprächssynthesen, von
denen spätere Arbeit abhängt. Erklärungen und Statusmeldungen ohne solche Abhängigkeiten
brauchen keine Aufzeichnung. Ist Speichern verboten, nennt der Agent, was nicht gespeichert wurde.

| Arbeit | Aufzeichnung unter `docs/lusona/` im Projekt |
| --- | --- |
| Änderung, die eine Spezifikation braucht | `specs/<change-id>.md` und eine Zeile in `work.md` |
| Direkte Implementierung oder Refactoring ohne Spezifikation | `notes/<change-slug>.md` |
| Untersuchung, Messung oder Experiment | Notizen und Aufzeichnungen in `evidence/` |
| Folgenreiche Architekturentscheidung | `adr/<YYYYMMDD>-<decision-slug>.md` |
| Produktbeschreibung und Funktionsübersicht | `product.md` |
| Batch | `batches/<batch-slug>.md` |

In vier Fällen sind eine Spezifikation und ihre Warteschlangenzeile erforderlich. Die Größe
entscheidet dies nicht.

- Der Skill definiert Änderungen in einer Spezifikation, wie **specify**.
- Du verlangst eine Spezifikation oder Nachverfolgung.
- Für die Änderung besteht bereits eine Spezifikation.
- Die Änderung braucht wegen ihrer Auswirkungen ein unabhängiges Review.

Die Warteschlangenstatus sind Ideas, Ready, Doing, Review und Done; keiner gibt Implementierung
frei. Icebox ist ein Abschnitt der Warteschlange für zurückgestellte Zeilen. Eine solche Zeile
behält ihren Status. Siehe [Warteschlange](plugins/lusona/references/queue.md).

Jede zuständige Aufzeichnung führt eine aktuelle Übergabe mit Ziel, Entscheidungen, Befugnissen,
TDD-Stufe und Quelle, Belegen, Unsicherheit, Korrekturzahlen, Blockaden, Zuständigkeiten und
nächster Aktion (P2). Wenn die Anwendung die Kontextnutzung meldet, bereitet der Agent bei 40%
eine Übergabe vor und schließt sie vor 50% ab. Bei Fortsetzung liest er erhaltene Aufzeichnungen
und den Arbeitsbaum und fragt dich nur nach Befugnissen oder Fakten, die die nächste Aktion
ändern. Freigaben gelten über Übergaben hinweg. Verhindert eine abrupte Unterbrechung das
Speichern, behauptet der Agent keinen gesicherten Zwischenstand. Aufzeichnungen früherer
Plugin-Versionen bleiben gültig und werden am bestehenden Ort aktualisiert. Siehe
[Aufbewahrung](plugins/lusona/references/retention.md) und [Dateien](plugins/lusona/references/files.md).

Zur Fortsetzung kannst du mit **status** die Restarbeit bewerten oder die fortzusetzende Arbeit nennen:

> Setze die Untersuchung zum Ablauf von Einladungen anhand der gespeicherten Erkenntnisse fort.
> Prüfe den festgehaltenen Reproduktionsfall mit dem aktuellen Build. Ändere das Verhalten des
> Produktionscodes nicht.

## Antworten und nächste Aktionen

Jede Aufgabenantwort endet mit derselben Form (P8); Begrüßungen und Bestätigungen nicht. Der
Status lautet **✅ Abgeschlossen** (angeforderter Umfang erfüllt), **🔄 In Arbeit** (freigegebene
Arbeit geht weiter), **❓ Eingabe nötig** (eine Voraussetzung fehlt) oder **⏸ Pausiert** (betroffene
Arbeit wartet auf eine benannte Voraussetzung). Der Status beschreibt die Antwort, nicht den
Warteschlangenstatus. Hypothetische Antwort, kein Nachweis geleisteter Arbeit:

> **Result:** ❓ Eingabe nötig: Wähle die TDD-Stufe, bevor die Implementierung beginnt.
> Spezifikation und Akzeptanzkriterien sind aufgezeichnet.
>
> **Evidence:** Keine Prüfungen ausgeführt; die Änderung ist definiert, nicht implementiert.
>
> | Next action | Owner | Needs | Authority |
> | --- | --- | --- | --- |
> | `none`, `targeted` oder `strict` wählen; `targeted` wird für die Parseränderung empfohlen | Nutzer | Die aufgezeichnete Spezifikation | TDD-Stufe nicht gewählt |

- Zuständig ist der Nutzer, der Koordinator oder ein benannter Skill. Die Spalte Authority sagt
  `Authorized` oder nennt die fehlende Befugnis.
- Eine blockierende Entscheidung oder Freigabe kommt zuerst. Die Antwort ergänzt **Decisions:**,
  wenn sie eine folgenreiche Entscheidung getroffen hat, und **Open issues:** bei offenen Problemen.
- Ist der Umfang abgeschlossen und dient eine Folgearbeit dem vereinbarten Ergebnis, schlägt
  die Antwort sie vor und nennt die fehlende Befugnis. Bleibt keine Aktion, steht dort
  `**Next action:** None for this request` mit einer Begründung in einem Satz.
- Eine Anweisung zur Fortsetzung in einer anderen Sitzung steht als Blockzitat unter der Tabelle.
- Die Antwort behält die erforderlichen Bezeichnungen und Felder, sofern weder du noch die
  Anwendung ausdrücklich ein unvereinbares Format verlangen. Der Wunsch nach Kürze entfernt sie
  nicht. In einem angepassten Format bleiben Ergebnis, Belege, Status und nächste Aktion
  erhalten. Siehe die [Abschlussbeispiele](plugins/lusona/references/completion.md).

## Installation

Wähle deine Anwendung. Installiere über HTTPS aus dem öffentlichen Repository
[lusona/ai-skills](https://github.com/lusona/ai-skills); für den Download brauchst du keine
GitHub-Zugangsdaten.

### Antigravity

Installiere direkt von GitHub:

```bash
agy plugin install https://github.com/lusona/ai-skills.git
```

Die URL installiert Lusona aus dem Manifest im Repository-Stamm. Prüfe für App und
eigenständige IDE nach dieser globalen CLI-Installation **Customizations**. Die
[Antigravity-Installationsanleitung](INSTALL.md#antigravity) beschreibt lokale Arbeitskopien,
portable Pakete, Updates, Deinstallation und Prüfgrenzen. Sie dokumentiert eine Prüfung der
GitHub-Installation mit Antigravity CLI 1.4.12 unter Linux für Lusona 1.4.0; das interaktive
Verhalten in App und IDE wurde nicht getestet.

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

Öffne **Customize > From GitHub Repository**, gib `https://github.com/lusona/ai-skills` ein
und installiere **Lusona Skills** für dein Projekt oder dein Benutzerkonto. Gib im Agent-Chat `/`
ein, um Lusonas Skills zu finden. Die [Cursor-Installationsschritte](INSTALL.md#cursor) verlinken
die aktuelle Cursor-Dokumentation und nennen den Teststatus.

### Xcode

Öffne in Xcode 27 **Settings > Intelligence > Agents > Plug-ins > Add Plug-in**.
Wähle **Add from URL**, gib `https://github.com/lusona/ai-skills` ein und wähle die Lusona-Skills,
die du installieren möchtest. Die [Installationsschritte für Xcode](INSTALL.md#xcode) beschreiben
Einrichtung, lokale Importe und Versionsdetails.

Starte nach der Installation eine neue Sitzung in deinem Projekt. Angaben zur Installation
aus einer lokalen Arbeitskopie, zu portablen Paketen, Updates und zur Deinstallation findest
du in der [Installationsanleitung](INSTALL.md). Wähle eine Katalogquelle: lokale Arbeitskopie
oder GitHub.

## Referenzen

- [Änderungsprotokoll](CHANGELOG.md)
- [Installation und Deinstallation](INSTALL.md)
- [Datenschutzerklärung](PRIVACY.md)
- [Nutzungsbedingungen](TERMS.md)
- [Plugin-Katalog: Skills, Referenzen und Vorlagen](plugins/lusona/README.md)
- [Prinzipien des Arbeitszyklus, Skills, Zuordnung und Begriffe](plugins/lusona/references/workflow-guide.md)
- [TDD-Stufe und Verifikation](plugins/lusona/references/tdd.md)
- [Batch-Koordination](plugins/lusona/skills/batch/SKILL.md)
- [Aufzeichnungen, Aufbewahrung und Übergabe](plugins/lusona/references/retention.md)
- [Abschluss und Wiederaufnahme](plugins/lusona/references/closeout.md)
- [Delegation](plugins/lusona/references/delegation.md)
- [Gespräche zur Klärung der Absicht](plugins/lusona/references/interviews.md)

## Mitwirken

[CONTRIBUTING.md](CONTRIBUTING.md) beschreibt den Umfang von Beiträgen, lokale Prüfungen und Pull
Requests. Nutze die [Formulare für Fehler und Funktionswünsche](https://github.com/lusona/ai-skills/issues/new/choose),
um Probleme zu melden oder Verbesserungen vorzuschlagen. Das Team `@lusona/core` ist für die
Reviews im Repository zuständig.

## Lizenz

Skills, Vorlagen, Dokumentation und Skripte stehen unter der [MIT-Lizenz](LICENSE).

## Entwicklung

Die maßgeblichen Workflow-Quellen liegen in `plugins/lusona/`. Daten nutzender Projekte gehören
unter `docs/lusona/` des jeweiligen Projekts; die leere Warteschlangenstruktur liegt in
`plugins/lusona/templates/work.md.template`.

Die Hilfsprogramme für Plugin-Aufzeichnungen verwenden Bash oder PowerShell
([Laufzeitanforderungen](INSTALL.md#requirements)). Python 3 wird nur für die Paketerstellung
und Python-Evaluationen benötigt, nicht für die Plugin-Nutzung.

```bash
claude plugin validate plugins/lusona
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package.py
```

Der Paketgenerator prüft Namen und Versionen nativer Manifeste, Links, Katalogpfade und die
Dateiauswahl. Alle nativen Manifeste müssen dieselbe Version verwenden. Er schreibt nach
`tmp/lusona-package/` innerhalb des Repositorys und weigert sich, ein bestehendes Ausgabeverzeichnis
zu überschreiben. Nutze `--output tmp/<new-directory>` für einen weiteren Build. Weder
Installation noch Paketerstellung initialisieren Projektaufzeichnungen.

Die Regeln für jede Aufgabe und die Antwortform in jedem `SKILL.md` werden aus dem Verzeichnis
`shared/` des Repositorys erzeugt. Bearbeite sie dort und führe
`python3 scripts/sync_shared.py --source shared
plugins/lusona` aus; ergänze `--check`, um zu prüfen, ohne Dateien zu ändern.
