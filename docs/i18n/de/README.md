# Sicherheitsprüfung und Lernen

Deutsch · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

Lerne OWASP, schreibe sichereren Code und prüfe Commits in beliebigen Projekten. Der Skill behandelt auch MCP, LLM-Anwendungen, Agenten und Skill-Pakete.

## Installation

Kopiere den Ordner security-review in das Verzeichnis .agents/skills/ deines Projekts. Rufe den Skill im gewünschten Projekt auf.

## Beispiele

```text
$security-review Prüfe diesen Commit und bleibe für die nächsten aktiv.
$security-review Hilf mir, diese Funktion mit Funktions- und Sicherheitstests zu implementieren.
$security-review Bringe mir MCP-Sicherheit mit einem Quiz bei, jeweils eine Frage.
```

## Verhalten und Grenzen

Der Skill prüft aktuelle offizielle Quellen, erklärt Befunde und Korrekturen und nennt die tatsächlich ausgeführten Tests. Während der Entwicklung hilft er, erlaubte Nutzung und unzulässige Aktionen zu testen. Die Übungen passen sich deinen Antworten an.

Er bleibt innerhalb der Agentensitzung aktiv und überwacht Git nach deren Ende nicht weiter. Diese Übersetzung wurde mit KI erstellt und nicht von einem Muttersprachler geprüft.

## Quellen

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
