# Güvenlik incelemesi ve öğrenme

Türkçe · [🌐](../README.md) · [SKILL.md](../../../security-review/SKILL.md)

OWASP öğrenin, daha güvenli kod yazın ve herhangi bir projenin commitlerini inceleyin. Bu skill MCP, LLM uygulamaları, ajanlar ve skill paketlerini de kapsar.

## Kurulum

security-review klasörünü projenizin .agents/skills/ dizinine kopyalayın. Skill'i üzerinde çalışacağınız projeden çağırın.

## Örnekler

```text
$security-review Bu commit'i incele ve sonraki commitler için etkin kal.
$security-review Bu özelliği işlevsel testler ve güvenlik testleriyle geliştirmeme yardım et.
$security-review Bana MCP güvenliğini bir sınavla öğret, her seferinde bir soru sor.
```

## Davranış ve sınırlar

Skill güncel resmî kaynakları kontrol eder, bulguları ve düzeltmeleri açıklar, gerçekten çalıştırılan testleri bildirir. Geliştirme sırasında geçerli kullanımın ve yetkisiz işlemlerin test edilmesine yardımcı olur. Dersleri yanıtlarınıza göre uyarlar.

Yalnızca ajan oturumu boyunca etkindir; oturum bitince Git'i izlemeyi sürdürmez. Bu çeviri yapay zekâ tarafından oluşturulmuştur ve ana dili Türkçe olan biri tarafından incelenmemiştir.

## Kaynaklar

- [OWASP](../../../security-review/references/owasp.md)
- [MCP / LLM / AI](../../../security-review/references/ai-security.md)
- [Tests](../../../security-review/references/security-tests.md)
- [Learning](../../../security-review/references/learning.md)
- [Evaluation](../../../evals/README.md)
