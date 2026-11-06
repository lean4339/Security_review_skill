# Priksa keamanan lan sinau

Basa Jawa · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

Sinaua OWASP, tulisen kode sing luwih aman, lan priksa commit ing proyek apa wae. Skill iki uga nyakup MCP, aplikasi LLM, agen, lan paket skill.

## Instalasi

Salinen folder security-review menyang direktori .agents/skills/ ing proyekmu. Undangen skill saka proyek sing arep digarap.

## Tuladha

```text
$security-review Priksa commit iki lan tetep aktif kanggo commit sabanjure.
$security-review Tulung aku nggawe fitur iki nganggo tes fungsi lan tes keamanan.
$security-review Wulangana aku keamanan MCP nganggo kuis, takon siji-siji.
```

## Cara kerja lan watesan

Skill mriksa sumber resmi paling anyar, nerangake masalah lan carane ndandani, sarta nglaporake tes sing tenan ditindakake. Nalika nulis kode, skill mbantu nguji panggunaan sing sah lan tumindak tanpa idin. Piwulang dicocogake karo wangsulanmu.

Skill mung aktif sajrone sesi agen; ora ngawasi Git sawise sesi rampung. Terjemahan iki digawe AI lan durung dipriksa dening panutur asli.

## Rujukan

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
