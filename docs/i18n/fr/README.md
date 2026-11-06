# Revue de sécurité et apprentissage

Français · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

Étudiez OWASP, écrivez du code plus sûr et examinez les commits de tout projet. Cette compétence couvre aussi MCP, les applications LLM, les agents et les paquets de compétences.

## Installation

Copiez le dossier security-review dans le répertoire .agents/skills/ de votre projet. Invoquez la compétence depuis le projet concerné.

## Exemples

```text
$security-review Examine ce commit et reste active pour les suivants.
$security-review Aide-moi à développer cette fonctionnalité avec des tests fonctionnels et de sécurité.
$security-review Enseigne-moi la sécurité MCP avec un questionnaire, une question à la fois.
```

## Fonctionnement et limites

La compétence consulte les sources officielles actuelles, explique les constats et les corrections et précise les tests réellement exécutés. Elle aide à tester les usages légitimes et les actions non autorisées, et adapte les leçons à vos réponses.

Elle reste active pendant la session de l’agent ; elle ne surveille pas Git après sa fermeture. Cette traduction a été générée par IA et n’a pas été révisée par une personne de langue maternelle française.

## Références

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
