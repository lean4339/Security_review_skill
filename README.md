# Security Review · OWASP

🌐 **32 languages** · [SKILL.md](security-review/SKILL.md) · [Tests & evaluation](evals/README.md) · [Language selection](docs/i18n/README.md)

[English](#lang-en) | [普通话 / 简体中文](#lang-cmn) | [हिन्दी](#lang-hi) | [Español](#lang-es) | [العربية الفصحى](#lang-ar) | [Français](#lang-fr) | [বাংলা](#lang-bn) | [Português](#lang-pt) | [Bahasa Indonesia](#lang-id) | [اردو](#lang-ur) | [Русский](#lang-ru) | [Deutsch](#lang-de) | [日本語](#lang-ja) | [Naijá / Nigerian Pidgin](#lang-pcm) | [العربية المصرية](#lang-arz) | [मराठी](#lang-mr) | [Tiếng Việt](#lang-vi) | [తెలుగు](#lang-te) | [Kiswahili](#lang-sw) | [Hausa](#lang-ha) | [Türkçe](#lang-tr) | [پنجابی (شاہ مکھی)](#lang-pnb) | [Tagalog](#lang-tl) | [தமிழ்](#lang-ta) | [粵語 / 繁體中文](#lang-yue) | [吴语（上海话）](#lang-wuu) | [فارسی ایران](#lang-fa) | [한국어](#lang-ko) | [አማርኛ](#lang-am) | [ไทย](#lang-th) | [Basa Jawa](#lang-jv) | [Italiano](#lang-it)

---

<a id="lang-en"></a>

## English — Security review and learning

Study OWASP, build safer code, and review commits in any project. This skill also covers MCP, LLM applications, agents, and skills.

### Installation

Copy the security-review folder into your project's .agents/skills/ directory. Invoke it from the project you want to work on.

### Examples

```text
$security-review Review this commit and stay active for the next ones.
$security-review Help me implement this feature with functional and security tests.
$security-review Teach me MCP security with a quiz, one question at a time.
```

### Behavior and limits

The skill checks current official sources, explains findings and fixes, and reports which tests actually ran. During development it helps write tests for valid use and unauthorized actions. It adapts lessons to your answers.

It stays active within the agent session; it does not monitor Git after the session ends. This translation is AI-generated and has not been reviewed by a native speaker.

### References

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-cmn"></a>

## 普通话 / 简体中文 — 安全审查与学习

学习 OWASP，编写更安全的代码，并审查任何项目的提交。本技能也涵盖 MCP、大语言模型应用、智能体和技能包。

### 安装

将 security-review 文件夹复制到项目的 .agents/skills/ 目录。在需要处理的项目中调用。

### 示例

```text
$security-review 审查这次提交，并继续审查本会话中的后续提交。
$security-review 帮助我实现这个功能，并编写功能测试和安全测试。
$security-review 用测验教我 MCP 安全，每次只问一个问题。
```

### 行为与限制

技能会查询最新官方资料，解释发现的问题和修复方法，并说明实际执行了哪些测试。开发时，它会帮助验证正常操作和未经授权的操作，并根据你的回答调整教学。

技能仅在智能体会话中保持启用，会话结束后不会持续监控 Git。本译文由人工智能生成，尚未经母语使用者审校。

### 参考资料

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-hi"></a>

## हिन्दी — सुरक्षा समीक्षा और अध्ययन

OWASP सीखें, सुरक्षित कोड लिखें और किसी भी परियोजना के कमिट की समीक्षा करें। यह स्किल MCP, LLM अनुप्रयोगों, एजेंटों और स्किल पैकेजों को भी शामिल करती है।

### स्थापना

security-review फ़ोल्डर को अपनी परियोजना की .agents/skills/ डायरेक्टरी में कॉपी करें। जिस परियोजना पर काम करना है, वहीं से इसे चलाएँ।

### उदाहरण

```text
$security-review इस कमिट की समीक्षा करो और अगले कमिट के लिए सक्रिय रहो।
$security-review इस सुविधा को कार्यात्मक और सुरक्षा परीक्षणों के साथ बनाने में मदद करो।
$security-review मुझे MCP सुरक्षा पर प्रश्नोत्तरी दो; एक बार में एक प्रश्न पूछो।
```

### व्यवहार और सीमाएँ

स्किल नवीनतम आधिकारिक स्रोत देखती है, समस्याएँ और सुधार समझाती है तथा वास्तव में चलाए गए परीक्षण बताती है। विकास के दौरान यह वैध उपयोग और अनधिकृत कार्रवाइयों के परीक्षण लिखने में मदद करती है। शिक्षण आपके उत्तरों के अनुसार बदलता है।

यह केवल एजेंट सत्र के भीतर सक्रिय रहती है; सत्र समाप्त होने के बाद Git की निगरानी नहीं करती। यह अनुवाद AI ने बनाया है और किसी मातृभाषी ने इसकी समीक्षा नहीं की है।

### संदर्भ

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-es"></a>

## Español — Revisión de seguridad y aprendizaje

Estudiá OWASP, escribí código más seguro y revisá commits de cualquier proyecto. La skill también cubre MCP, aplicaciones LLM, agentes y paquetes de skills.

### Instalación

Copiá la carpeta security-review al directorio .agents/skills/ de tu proyecto. Invocala desde el proyecto sobre el que querés trabajar.

### Ejemplos

```text
$security-review Revisá este commit y quedá activa para los siguientes.
$security-review Ayudame a implementar esta funcionalidad con tests funcionales y de seguridad.
$security-review Enseñame seguridad MCP con un cuestionario, una pregunta por vez.
```

### Comportamiento y límites

La skill consulta fuentes oficiales vigentes, explica hallazgos y correcciones e indica qué tests ejecutó realmente. Durante el desarrollo ayuda a probar el uso legítimo y las acciones no autorizadas. Adapta las lecciones a tus respuestas.

Queda activa dentro de la sesión del agente; no monitorea Git después de cerrarla. Este texto fue generado por IA y no tiene revisión lingüística independiente.

### Referencias

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-ar"></a>

## العربية الفصحى — مراجعة الأمان والتعلّم

تعلّم OWASP، واكتب شيفرة أكثر أمانًا، وراجع التعديلات المثبّتة في أي مشروع. تشمل المهارة أيضًا MCP وتطبيقات النماذج اللغوية الكبيرة والوكلاء وحزم المهارات.

### التثبيت

انسخ مجلد security-review إلى دليل .agents/skills/ في مشروعك. استدعِ المهارة من المشروع الذي تريد العمل عليه.

### أمثلة

```text
$security-review راجع هذا التعديل المثبّت وابقَ نشطًا لمراجعة التعديلات التالية.
$security-review ساعدني في تنفيذ هذه الميزة مع اختبارات وظيفية واختبارات أمان.
$security-review علّمني أمان MCP باختبار قصير، سؤال واحد في كل مرة.
```

### السلوك والحدود

تراجع المهارة المصادر الرسمية الحالية، وتشرح النتائج والإصلاحات، وتبيّن الاختبارات التي نُفّذت بالفعل. أثناء التطوير تساعد في اختبار الاستخدام المسموح والإجراءات غير المصرّح بها، وتكيّف الدروس حسب إجاباتك.

تبقى نشطة داخل جلسة الوكيل فقط، ولا تراقب Git بعد انتهائها. هذه الترجمة مولّدة بالذكاء الاصطناعي ولم يراجعها متحدث أصلي.

### المراجع

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-fr"></a>

## Français — Revue de sécurité et apprentissage

Étudiez OWASP, écrivez du code plus sûr et examinez les commits de tout projet. Cette compétence couvre aussi MCP, les applications LLM, les agents et les paquets de compétences.

### Installation

Copiez le dossier security-review dans le répertoire .agents/skills/ de votre projet. Invoquez la compétence depuis le projet concerné.

### Exemples

```text
$security-review Examine ce commit et reste active pour les suivants.
$security-review Aide-moi à développer cette fonctionnalité avec des tests fonctionnels et de sécurité.
$security-review Enseigne-moi la sécurité MCP avec un questionnaire, une question à la fois.
```

### Fonctionnement et limites

La compétence consulte les sources officielles actuelles, explique les constats et les corrections et précise les tests réellement exécutés. Elle aide à tester les usages légitimes et les actions non autorisées, et adapte les leçons à vos réponses.

Elle reste active pendant la session de l’agent ; elle ne surveille pas Git après sa fermeture. Cette traduction a été générée par IA et n’a pas été révisée par une personne de langue maternelle française.

### Références

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-bn"></a>

## বাংলা — নিরাপত্তা পর্যালোচনা ও শেখা

OWASP শিখুন, আরও নিরাপদ কোড লিখুন এবং যেকোনো প্রকল্পের কমিট পর্যালোচনা করুন। এই স্কিল MCP, LLM অ্যাপ্লিকেশন, এজেন্ট ও স্কিল প্যাকেজও কভার করে।

### ইনস্টলেশন

আপনার প্রকল্পের .agents/skills/ ডিরেক্টরিতে security-review ফোল্ডারটি কপি করুন। যে প্রকল্পে কাজ করবেন, সেখান থেকে স্কিলটি চালু করুন।

### উদাহরণ

```text
$security-review এই কমিট পর্যালোচনা করো এবং পরের কমিটগুলোর জন্য সক্রিয় থাকো।
$security-review কার্যকরী ও নিরাপত্তা পরীক্ষা সহ এই ফিচারটি তৈরি করতে সাহায্য করো।
$security-review একবারে একটি প্রশ্ন করে কুইজের মাধ্যমে আমাকে MCP নিরাপত্তা শেখাও।
```

### আচরণ ও সীমা

স্কিলটি বর্তমান আনুষ্ঠানিক উৎস দেখে, সমস্যা ও সংশোধন ব্যাখ্যা করে এবং কোন পরীক্ষাগুলো সত্যিই চালানো হয়েছে তা জানায়। এটি বৈধ ব্যবহার ও অননুমোদিত কাজের পরীক্ষা লিখতে সাহায্য করে এবং আপনার উত্তর অনুযায়ী পাঠ বদলায়।

এটি শুধু এজেন্ট সেশনের মধ্যে সক্রিয় থাকে; সেশন শেষ হলে Git পর্যবেক্ষণ করে না। এই অনুবাদ AI দিয়ে তৈরি এবং কোনো মাতৃভাষীর পর্যালোচনা হয়নি।

### তথ্যসূত্র

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-pt"></a>

## Português — Revisão de segurança e aprendizado

Estude OWASP, escreva código mais seguro e revise commits de qualquer projeto. A skill também abrange MCP, aplicações LLM, agentes e pacotes de skills.

### Instalação

Copie a pasta security-review para o diretório .agents/skills/ do projeto. Invoque a skill a partir do projeto em que deseja trabalhar.

### Exemplos

```text
$security-review Revise este commit e continue ativa para os próximos.
$security-review Ajude-me a implementar esta funcionalidade com testes funcionais e de segurança.
$security-review Ensine-me segurança MCP com um questionário, uma pergunta por vez.
```

### Comportamento e limites

A skill consulta fontes oficiais atuais, explica os problemas e as correções e informa quais testes realmente executou. Durante o desenvolvimento, ajuda a testar usos legítimos e ações não autorizadas. Adapta as aulas às suas respostas.

Ela permanece ativa durante a sessão do agente; não monitora o Git depois que a sessão termina. Esta tradução foi gerada por IA e não foi revisada por um falante nativo.

### Referências

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-id"></a>

## Bahasa Indonesia — Tinjauan keamanan dan pembelajaran

Pelajari OWASP, tulis kode yang lebih aman, dan tinjau commit di proyek mana pun. Skill ini juga mencakup MCP, aplikasi LLM, agen, dan paket skill.

### Instalasi

Salin folder security-review ke direktori .agents/skills/ proyek Anda. Panggil skill dari proyek yang ingin dikerjakan.

### Contoh

```text
$security-review Tinjau commit ini dan tetap aktif untuk commit berikutnya.
$security-review Bantu saya membuat fitur ini dengan pengujian fungsional dan keamanan.
$security-review Ajari saya keamanan MCP melalui kuis, satu pertanyaan setiap kali.
```

### Perilaku dan batasan

Skill memeriksa sumber resmi terkini, menjelaskan temuan dan perbaikan, serta menyebutkan pengujian yang benar-benar dijalankan. Saat pengembangan, skill membantu menguji penggunaan yang sah dan tindakan tanpa izin. Materi disesuaikan dengan jawaban Anda.

Skill tetap aktif selama sesi agen; tidak memantau Git setelah sesi berakhir. Terjemahan ini dibuat oleh AI dan belum ditinjau penutur asli.

### Referensi

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-ur"></a>

## اردو — سیکیورٹی جائزہ اور تعلیم

OWASP سیکھیں، زیادہ محفوظ کوڈ لکھیں اور کسی بھی منصوبے کے کمٹس کا جائزہ لیں۔ یہ اسکل MCP، LLM ایپلی کیشنز، ایجنٹس اور اسکل پیکیجز کو بھی شامل کرتی ہے۔

### تنصیب

security-review فولڈر کو اپنے منصوبے کی .agents/skills/ ڈائریکٹری میں کاپی کریں۔ اسے اسی منصوبے سے چلائیں جس پر کام کرنا چاہتے ہیں۔

### مثالیں

```text
$security-review اس کمٹ کا جائزہ لو اور اگلے کمٹس کے لیے فعال رہو۔
$security-review فنکشنل اور سیکیورٹی ٹیسٹس کے ساتھ یہ فیچر بنانے میں میری مدد کرو۔
$security-review مجھے MCP سیکیورٹی پر کوئز دو، ایک وقت میں ایک سوال پوچھو۔
```

### رویّہ اور حدود

اسکل موجودہ سرکاری ذرائع دیکھتی ہے، مسائل اور اصلاحات سمجھاتی ہے اور بتاتی ہے کہ کون سے ٹیسٹ واقعی چلائے گئے۔ ترقی کے دوران یہ جائز استعمال اور غیر مجاز کارروائیوں کے ٹیسٹس لکھنے میں مدد کرتی ہے۔ اسباق آپ کے جوابات کے مطابق بدلتے ہیں۔

یہ صرف ایجنٹ کے سیشن کے اندر فعال رہتی ہے؛ سیشن ختم ہونے کے بعد Git کی نگرانی نہیں کرتی۔ یہ ترجمہ AI نے تیار کیا ہے اور کسی مقامی زبان بولنے والے نے اس کا جائزہ نہیں لیا۔

### حوالہ جات

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-ru"></a>

## Русский — Проверка безопасности и обучение

Изучайте OWASP, пишите более безопасный код и проверяйте коммиты любого проекта. Навык также охватывает MCP, приложения с LLM, агентов и пакеты навыков.

### Установка

Скопируйте папку security-review в каталог .agents/skills/ вашего проекта. Вызывайте навык из проекта, над которым хотите работать.

### Примеры

```text
$security-review Проверь этот коммит и оставайся активным для следующих.
$security-review Помоги реализовать эту функцию с функциональными тестами и тестами безопасности.
$security-review Обучи меня безопасности MCP с помощью викторины, задавая по одному вопросу.
```

### Поведение и ограничения

Навык проверяет актуальные официальные источники, объясняет проблемы и исправления и сообщает, какие тесты действительно выполнены. При разработке помогает проверить разрешённое использование и недопустимые действия. Обучение адаптируется к вашим ответам.

Навык активен в рамках сеанса агента и не следит за Git после его завершения. Перевод создан ИИ и не проверен носителем языка.

### Источники

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-de"></a>

## Deutsch — Sicherheitsprüfung und Lernen

Lerne OWASP, schreibe sichereren Code und prüfe Commits in beliebigen Projekten. Der Skill behandelt auch MCP, LLM-Anwendungen, Agenten und Skill-Pakete.

### Installation

Kopiere den Ordner security-review in das Verzeichnis .agents/skills/ deines Projekts. Rufe den Skill im gewünschten Projekt auf.

### Beispiele

```text
$security-review Prüfe diesen Commit und bleibe für die nächsten aktiv.
$security-review Hilf mir, diese Funktion mit Funktions- und Sicherheitstests zu implementieren.
$security-review Bringe mir MCP-Sicherheit mit einem Quiz bei, jeweils eine Frage.
```

### Verhalten und Grenzen

Der Skill prüft aktuelle offizielle Quellen, erklärt Befunde und Korrekturen und nennt die tatsächlich ausgeführten Tests. Während der Entwicklung hilft er, erlaubte Nutzung und unzulässige Aktionen zu testen. Die Übungen passen sich deinen Antworten an.

Er bleibt innerhalb der Agentensitzung aktiv und überwacht Git nach deren Ende nicht weiter. Diese Übersetzung wurde mit KI erstellt und nicht von einem Muttersprachler geprüft.

### Quellen

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-ja"></a>

## 日本語 — セキュリティレビューと学習

OWASPを学び、より安全なコードを書き、任意のプロジェクトのコミットをレビューできます。このスキルはMCP、LLMアプリ、エージェント、スキルパッケージも対象にします。

### インストール

security-reviewフォルダーをプロジェクトの.agents/skills/ディレクトリーにコピーしてください。作業対象のプロジェクトから呼び出します。

### 使用例

```text
$security-review このコミットをレビューし、以降のコミットも継続して確認してください。
$security-review この機能の実装と、機能テストおよびセキュリティテストの作成を手伝ってください。
$security-review MCPのセキュリティをクイズで教えてください。一度に一問ずつ出してください。
```

### 動作と制限

最新の公式資料を確認し、問題と修正方法を説明し、実際に実行したテストを報告します。開発中は正当な操作と権限のない操作のテストを支援し、回答に応じて学習内容を調整します。

スキルが有効なのはエージェントのセッション内です。終了後にGitを監視することはありません。この翻訳はAI生成で、母語話者による校閲は受けていません。

### 参考資料

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-pcm"></a>

## Naijá / Nigerian Pidgin — Security review and learning

Learn OWASP, write code wey safe pass, and review commits for any project. This skill also cover MCP, LLM apps, agents and skill packages.

### How to install

Copy security-review folder put inside your project .agents/skills/ directory. Call the skill from the project wey you wan work on.

### Examples

```text
$security-review Review this commit and stay active for the next ones.
$security-review Help me build this feature with functional tests and security tests.
$security-review Teach me MCP security with quiz; ask one question at a time.
```

### How e work and limits

The skill go check current official sources, explain problems and fixes, and tell you which tests e really run. As you dey code, e go help test correct use and actions wey no get permission. E go adjust lessons based on your answers.

E dey active only inside the agent session; e no dey watch Git after the session end. Na AI make this translation; native speaker never review am.

### Sources

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-arz"></a>

## العربية المصرية — مراجعة الأمان والتعلّم

اتعلّم OWASP، واكتب كود أكثر أمان، وراجع الكوميتات في أي مشروع. الـskill دي كمان بتغطي MCP وتطبيقات LLM والـagents وحزم الـskills.

### التثبيت

انسخ فولدر security-review جوّه .agents/skills/ في مشروعك. شغّل الـskill من المشروع اللي عايز تشتغل عليه.

### أمثلة

```text
$security-review راجع الكوميت ده وخليك شغّال للكوميتات اللي بعده.
$security-review ساعدني أنفّذ الميزة دي مع اختبارات تشغيل واختبارات أمان.
$security-review علّمني أمان MCP بكويز، سؤال واحد كل مرة.
```

### طريقة الشغل والحدود

الـskill بتراجع المصادر الرسمية الحالية، وبتشرح المشاكل وإصلاحها، وبتقول إيه الاختبارات اللي اتشغّلت فعلًا. وقت كتابة الكود بتساعد تختبر الاستخدام المسموح والتصرفات اللي من غير صلاحية، وبتغيّر الشرح حسب إجاباتك.

بتفضل شغّالة جوّه جلسة الـagent بس؛ مش بتراقب Git بعد ما الجلسة تخلص. الترجمة دي معمولة بالذكاء الاصطناعي ولسه ما راجعهاش متحدث أصلي.

### المراجع

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-mr"></a>

## मराठी — सुरक्षा परीक्षण आणि शिक्षण

OWASP शिका, अधिक सुरक्षित कोड लिहा आणि कोणत्याही प्रकल्पातील कमिट तपासा. ही स्किल MCP, LLM ॲप्लिकेशन्स, एजंट आणि स्किल पॅकेजेससाठीही वापरता येते.

### स्थापना

security-review फोल्डर तुमच्या प्रकल्पातील .agents/skills/ डिरेक्टरीमध्ये कॉपी करा. ज्या प्रकल्पावर काम करायचे आहे, तिथून स्किल वापरा.

### उदाहरणे

```text
$security-review हा कमिट तपास आणि पुढील कमिटसाठी सक्रिय राहा.
$security-review कार्यात्मक आणि सुरक्षा चाचण्यांसह हे वैशिष्ट्य तयार करण्यास मदत कर.
$security-review मला प्रश्नमंजुषेतून MCP सुरक्षा शिकव; एका वेळी एक प्रश्न विचार.
```

### कार्यपद्धती आणि मर्यादा

स्किल सध्याचे अधिकृत स्रोत तपासते, समस्या आणि सुधारणा समजावते व प्रत्यक्ष चालवलेल्या चाचण्या सांगते. विकासादरम्यान वैध वापर आणि अनधिकृत कृतींच्या चाचण्या लिहिण्यास मदत करते. शिकवणी तुमच्या उत्तरांनुसार बदलते.

ती फक्त एजंट सत्रात सक्रिय राहते; सत्र संपल्यानंतर Git वर लक्ष ठेवत नाही. हे भाषांतर AI ने तयार केले असून मातृभाषिकाने तपासलेले नाही.

### संदर्भ

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-vi"></a>

## Tiếng Việt — Rà soát bảo mật và học tập

Học OWASP, viết mã an toàn hơn và rà soát commit của bất kỳ dự án nào. Skill này cũng bao gồm MCP, ứng dụng LLM, tác tử AI và gói skill.

### Cài đặt

Sao chép thư mục security-review vào .agents/skills/ của dự án. Gọi skill từ dự án bạn muốn làm việc.

### Ví dụ

```text
$security-review Rà soát commit này và tiếp tục hoạt động cho các commit tiếp theo.
$security-review Giúp tôi triển khai tính năng này cùng kiểm thử chức năng và bảo mật.
$security-review Dạy tôi bảo mật MCP bằng bài trắc nghiệm, mỗi lần một câu hỏi.
```

### Hoạt động và giới hạn

Skill kiểm tra nguồn chính thức hiện hành, giải thích phát hiện và cách sửa, đồng thời báo rõ những kiểm thử đã thực sự chạy. Trong quá trình lập trình, skill giúp kiểm tra việc sử dụng hợp lệ và hành động trái phép. Bài học được điều chỉnh theo câu trả lời.

Skill chỉ hoạt động trong phiên của tác tử; không theo dõi Git sau khi phiên kết thúc. Bản dịch này do AI tạo và chưa được người bản ngữ rà soát.

### Tài liệu tham khảo

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-te"></a>

## తెలుగు — భద్రతా సమీక్ష మరియు అభ్యాసం

OWASP నేర్చుకోండి, మరింత సురక్షితమైన కోడ్ రాయండి, ఏ ప్రాజెక్టులోనైనా కమిట్‌లను సమీక్షించండి. ఈ స్కిల్ MCP, LLM అప్లికేషన్‌లు, ఏజెంట్లు మరియు స్కిల్ ప్యాకేజీలను కూడా కవర్ చేస్తుంది.

### ఇన్‌స్టాలేషన్

security-review ఫోల్డర్‌ను మీ ప్రాజెక్టులోని .agents/skills/ డైరెక్టరీకి కాపీ చేయండి. మీరు పని చేయాలనుకునే ప్రాజెక్టు నుంచే స్కిల్‌ను పిలవండి.

### ఉదాహరణలు

```text
$security-review ఈ కమిట్‌ను సమీక్షించి, తరువాతి కమిట్‌ల కోసం సక్రియంగా ఉండు.
$security-review కార్యాచరణ మరియు భద్రతా పరీక్షలతో ఈ ఫీచర్‌ను రూపొందించడంలో సహాయపడు.
$security-review ఒక్కోసారి ఒక్క ప్రశ్న అడుగుతూ క్విజ్ ద్వారా MCP భద్రత నేర్పు.
```

### ప్రవర్తన మరియు పరిమితులు

స్కిల్ తాజా అధికారిక వనరులను పరిశీలించి, సమస్యలు మరియు పరిష్కారాలను వివరిస్తుంది. నిజంగా అమలు చేసిన పరీక్షలను తెలియజేస్తుంది. సరైన వినియోగం, అనుమతి లేని చర్యల కోసం పరీక్షలు రాయడంలో సహాయపడి, మీ సమాధానాల ప్రకారం పాఠాలను మార్చుతుంది.

ఇది ఏజెంట్ సెషన్‌లో మాత్రమే సక్రియంగా ఉంటుంది; సెషన్ ముగిసిన తరువాత Git‌ను పర్యవేక్షించదు. ఈ అనువాదం AI ద్వారా తయారైంది; మాతృభాష మాట్లాడే వ్యక్తి సమీక్షించలేదు.

### వనరులు

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-sw"></a>

## Kiswahili — Ukaguzi wa usalama na kujifunza

Jifunze OWASP, andika msimbo salama zaidi na kagua commit za mradi wowote. Skill hii pia inahusu MCP, programu za LLM, mawakala na vifurushi vya skill.

### Usakinishaji

Nakili folda ya security-review kwenye saraka ya .agents/skills/ ya mradi wako. Iite kutoka kwenye mradi unaotaka kufanyia kazi.

### Mifano

```text
$security-review Kagua commit hii na uendelee kuwa hai kwa commit zinazofuata.
$security-review Nisaidie kutekeleza kipengele hiki pamoja na majaribio ya utendaji na usalama.
$security-review Nifundishe usalama wa MCP kwa maswali, swali moja kwa wakati.
```

### Tabia na mipaka

Skill hukagua vyanzo rasmi vya sasa, hueleza matatizo na marekebisho, na hutaja majaribio yaliyotekelezwa kweli. Wakati wa kuandika msimbo husaidia kupima matumizi halali na vitendo visivyoidhinishwa. Mafunzo hubadilishwa kulingana na majibu yako.

Hubaki hai ndani ya kipindi cha wakala pekee; haifuatilii Git baada ya kipindi kuisha. Tafsiri hii imetengenezwa kwa AI na haijakaguliwa na mzungumzaji wa lugha ya kwanza.

### Marejeo

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-ha"></a>

## Hausa — Binciken tsaro da koyo

Koyi OWASP, rubuta lambar kwamfuta mafi aminci, kuma duba commit na kowane aiki. Wannan skill ya kuma shafi MCP, manhajojin LLM, wakilan AI da kunshin skill.

### Shigarwa

Kwafi babban fayil security-review zuwa kundin .agents/skills/ na aikinka. Kira skill daga aikin da kake son yi.

### Misalai

```text
$security-review Duba wannan commit kuma ka ci gaba da kasancewa a shirye don na gaba.
$security-review Taimaka mini gina wannan fasali tare da gwajin aiki da gwajin tsaro.
$security-review Koya mini tsaron MCP ta tambayoyi, tambaya ɗaya a lokaci guda.
```

### Yadda yake aiki da iyakoki

Skill yana bincika sabbin majiyoyin hukuma, yana bayyana matsaloli da gyare-gyare, kuma yana faɗin gwaje-gwajen da aka gudanar da gaske. Yana taimaka wa gwajin amfani na halal da ayyukan da ba a ba da izini ba. Darussa suna dacewa da amsoshinka.

Yana aiki ne kawai a cikin zaman wakilin AI; ba ya sa ido kan Git bayan zaman ya ƙare. AI ne ya samar da fassarar nan, kuma mai harshen asali bai duba ta ba.

### Majiyoyi

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-tr"></a>

## Türkçe — Güvenlik incelemesi ve öğrenme

OWASP öğrenin, daha güvenli kod yazın ve herhangi bir projenin commitlerini inceleyin. Bu skill MCP, LLM uygulamaları, ajanlar ve skill paketlerini de kapsar.

### Kurulum

security-review klasörünü projenizin .agents/skills/ dizinine kopyalayın. Skill'i üzerinde çalışacağınız projeden çağırın.

### Örnekler

```text
$security-review Bu commit'i incele ve sonraki commitler için etkin kal.
$security-review Bu özelliği işlevsel testler ve güvenlik testleriyle geliştirmeme yardım et.
$security-review Bana MCP güvenliğini bir sınavla öğret, her seferinde bir soru sor.
```

### Davranış ve sınırlar

Skill güncel resmî kaynakları kontrol eder, bulguları ve düzeltmeleri açıklar, gerçekten çalıştırılan testleri bildirir. Geliştirme sırasında geçerli kullanımın ve yetkisiz işlemlerin test edilmesine yardımcı olur. Dersleri yanıtlarınıza göre uyarlar.

Yalnızca ajan oturumu boyunca etkindir; oturum bitince Git'i izlemeyi sürdürmez. Bu çeviri yapay zekâ tarafından oluşturulmuştur ve ana dili Türkçe olan biri tarafından incelenmemiştir.

### Kaynaklar

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-pnb"></a>

## پنجابی (شاہ مکھی) — سکیورٹی دی جانچ تے سکھلائی

OWASP سکھو، ہور محفوظ کوڈ لکھو تے کسے وی پروجیکٹ دے کمٹ چیک کرو۔ ایہہ سکل MCP، LLM ایپاں، ایجنٹاں تے سکل پیکیجاں نوں وی کور کردی اے۔

### انسٹالیشن

security-review فولڈر اپنے پروجیکٹ دی .agents/skills/ ڈائریکٹری وچ کاپی کرو۔ جیہڑے پروجیکٹ اُتے کم کرنا اے، اوتھوں سکل چلاؤ۔

### مثالاں

```text
$security-review ایس کمٹ دی جانچ کرو تے اگلے کمٹاں لئی فعال رہو۔
$security-review فنکشنل تے سکیورٹی ٹیسٹاں نال ایہہ فیچر بناؤن وچ میری مدد کرو۔
$security-review مینوں MCP سکیورٹی کوئز نال سکھاؤ، اک ویلے اک سوال پچھو۔
```

### کم کرن دا طریقہ تے حدّاں

سکل موجودہ سرکاری ماخذ ویکھدی اے، مسئلے تے اوہناں دے حل سمجھاؤندی اے، تے دَسدی اے کہ کیہڑے ٹیسٹ واقعی چلے نیں۔ کوڈ لکھن ویلے جائز استعمال تے بغیر اجازت کمّاں دے ٹیسٹ بناؤن وچ مدد کردی اے۔ سبق تہاڈے جواباں مطابق بدلدا اے۔

ایہہ صرف ایجنٹ دے سیشن وچ فعال رہندی اے؛ سیشن مکن پچھوں Git دی نگرانی نہیں کردی۔ ایہہ ترجمہ AI نے بنایا اے تے ماں بولی بولن والے نے ایہدی جانچ نہیں کیتی۔

### حوالے

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-tl"></a>

## Tagalog — Pagsusuri ng seguridad at pag-aaral

Pag-aralan ang OWASP, sumulat ng mas ligtas na code, at suriin ang mga commit ng anumang proyekto. Saklaw din ng skill ang MCP, mga LLM application, agent, at skill package.

### Pag-install

Kopyahin ang folder na security-review sa .agents/skills/ ng iyong proyekto. Tawagin ang skill mula sa proyektong gagawin mo.

### Mga halimbawa

```text
$security-review Suriin ang commit na ito at manatiling aktibo para sa mga susunod.
$security-review Tulungan akong gawin ang feature na ito kasama ang functional at security tests.
$security-review Turuan mo ako ng MCP security gamit ang pagsusulit, isang tanong bawat pagkakataon.
```

### Pagkilos at mga limitasyon

Sinusuri ng skill ang kasalukuyang opisyal na sanggunian, ipinapaliwanag ang mga problema at pag-aayos, at sinasabi kung aling tests ang talagang pinatakbo. Tumutulong itong subukan ang wastong paggamit at mga hindi awtorisadong aksiyon. Inaangkop nito ang aralin sa iyong mga sagot.

Aktibo lamang ito sa loob ng session ng agent; hindi nito binabantayan ang Git pagkatapos nito. Ginawa ng AI ang saling ito at hindi pa nasuri ng katutubong tagapagsalita.

### Mga sanggunian

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-ta"></a>

## தமிழ் — பாதுகாப்பு ஆய்வும் கற்றலும்

OWASP கற்றுக்கொள்ளுங்கள், மேலும் பாதுகாப்பான நிரலை எழுதுங்கள், எந்தத் திட்டத்தின் கமிட்களையும் ஆய்வு செய்யுங்கள். இந்த ஸ்கில் MCP, LLM செயலிகள், முகவர்கள் மற்றும் ஸ்கில் தொகுப்புகளையும் உள்ளடக்குகிறது.

### நிறுவல்

security-review கோப்புறையை உங்கள் திட்டத்தின் .agents/skills/ அடைவில் நகலெடுக்கவும். வேலை செய்ய வேண்டிய திட்டத்திலிருந்து ஸ்கில்லை அழைக்கவும்.

### எடுத்துக்காட்டுகள்

```text
$security-review இந்த கமிட்டை ஆய்வு செய்து அடுத்த கமிட்களுக்கும் செயல்பாட்டில் இரு.
$security-review செயல்பாட்டு மற்றும் பாதுகாப்புச் சோதனைகளுடன் இந்த அம்சத்தை உருவாக்க உதவு.
$security-review ஒவ்வொரு முறையும் ஒரு கேள்வி கேட்டு வினாடி வினா மூலம் MCP பாதுகாப்பைக் கற்பி.
```

### செயல்பாடும் வரம்புகளும்

ஸ்கில் தற்போதைய அதிகாரப்பூர்வ ஆதாரங்களைப் பார்த்து, சிக்கல்களையும் திருத்தங்களையும் விளக்குகிறது. உண்மையில் இயக்கப்பட்ட சோதனைகளைத் தெரிவிக்கிறது. அனுமதிக்கப்பட்ட பயன்பாட்டையும் அனுமதியற்ற செயல்களையும் சோதிக்க உதவுகிறது. உங்கள் பதில்களுக்கு ஏற்ப பாடங்களை மாற்றுகிறது.

இது முகவரின் அமர்வுக்குள் மட்டுமே செயல்படும்; அமர்வு முடிந்தபின் Git-ஐக் கண்காணிக்காது. இந்த மொழிபெயர்ப்பு AI மூலம் உருவாக்கப்பட்டது; தாய்மொழி பேசுபவரால் சரிபார்க்கப்படவில்லை.

### ஆதாரங்கள்

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-yue"></a>

## 粵語 / 繁體中文 — 安全審查同學習

學習 OWASP、寫更安全嘅程式碼，同埋審查任何專案嘅 commit。呢個 skill 亦涵蓋 MCP、LLM 應用、AI 代理同 skill 套件。

### 安裝

將 security-review 資料夾複製去專案嘅 .agents/skills/ 目錄。喺你想處理嘅專案入面呼叫佢。

### 例子

```text
$security-review 幫我審查呢個 commit，之後嘅 commit 都繼續跟進。
$security-review 幫我實作呢個功能，連同功能測試同安全測試一齊做。
$security-review 用問答教我 MCP 安全，每次只問一條問題。
```

### 運作同限制

Skill 會查閱最新官方資料，解釋發現嘅問題同修正方法，並講清楚實際跑過邊啲測試。寫程式嗰陣會協助測試正常使用同未獲授權嘅操作，亦會按你嘅答案調整教學。

佢只會喺代理工作階段入面保持啟用；階段結束後唔會繼續監察 Git。呢份翻譯由 AI 產生，未經母語使用者校對。

### 參考資料

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-wuu"></a>

## 吴语（上海话） — 安全检查搭学习

学 OWASP，写更加安全个代码，检查各个项目个 commit。搿个 skill 也包括 MCP、LLM 应用、AI 代理搭 skill 包。

### 安装

拿 security-review 文件夹复制到项目个 .agents/skills/ 目录里向。勒侬要做事体个项目里向调用伊。

### 例子

```text
$security-review 检查搿个 commit，后头个 commit 也继续检查。
$security-review 帮我实现搿个功能，功能测试搭安全测试一道做。
$security-review 用问答教我 MCP 安全，一趟问一个问题。
```

### 用法搭限制

搿个 skill 会查看现在个官方资料，讲清爽问题搭修正办法，也会讲明实际上跑过啥个测试。写代码个辰光，伊会帮侬测试正常使用搭无授权个操作，照侬个回答调整学习内容。

伊只勒代理会话里向有效；会话结束以后勿会继续监看 Git。搿份翻译是 AI 做个，还呒没母语使用者校对。

### 参考资料

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-fa"></a>

## فارسی ایران — بازبینی امنیت و یادگیری

OWASP را یاد بگیرید، کد امن‌تری بنویسید و کامیت‌های هر پروژه‌ای را بازبینی کنید. این مهارت MCP، برنامه‌های LLM، عامل‌ها و بسته‌های مهارت را نیز پوشش می‌دهد.

### نصب

پوشهٔ security-review را در مسیر .agents/skills/ پروژهٔ خود کپی کنید. مهارت را از پروژه‌ای فراخوانی کنید که می‌خواهید روی آن کار کنید.

### مثال‌ها

```text
$security-review این کامیت را بازبینی کن و برای کامیت‌های بعدی فعال بمان.
$security-review کمکم کن این قابلیت را همراه با آزمون‌های عملکردی و امنیتی پیاده‌سازی کنم.
$security-review امنیت MCP را با آزمون به من یاد بده؛ هر بار فقط یک سؤال بپرس.
```

### رفتار و محدودیت‌ها

مهارت منابع رسمی روز را بررسی می‌کند، مشکلات و اصلاحات را توضیح می‌دهد و آزمون‌هایی را که واقعاً اجرا شده‌اند گزارش می‌کند. هنگام توسعه به آزمودن استفادهٔ مجاز و اقدامات غیرمجاز کمک می‌کند و درس‌ها را با پاسخ‌های شما تطبیق می‌دهد.

فقط در نشست عامل فعال می‌ماند؛ پس از پایان نشست Git را پایش نمی‌کند. این ترجمه با هوش مصنوعی تولید شده و گویشور بومی آن را بازبینی نکرده است.

### منابع

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-ko"></a>

## 한국어 — 보안 검토와 학습

OWASP를 배우고 더 안전한 코드를 작성하며 모든 프로젝트의 커밋을 검토하세요. 이 스킬은 MCP, LLM 애플리케이션, 에이전트와 스킬 패키지도 다룹니다.

### 설치

security-review 폴더를 프로젝트의 .agents/skills/ 디렉터리에 복사하세요. 작업할 프로젝트에서 스킬을 호출하세요.

### 예시

```text
$security-review 이 커밋을 검토하고 다음 커밋에도 계속 활성 상태를 유지해 줘.
$security-review 기능 테스트와 보안 테스트를 포함해 이 기능을 구현하도록 도와줘.
$security-review 퀴즈로 MCP 보안을 가르쳐 줘. 한 번에 한 문제씩 질문해 줘.
```

### 동작과 한계

스킬은 최신 공식 자료를 확인하고 발견한 문제와 수정 방법을 설명하며 실제로 실행한 테스트를 보고합니다. 개발 중에는 정상 사용과 권한 없는 동작을 테스트하도록 돕고, 답변에 맞춰 학습 내용을 조정합니다.

에이전트 세션 안에서만 활성 상태를 유지하며 세션 종료 후 Git을 감시하지 않습니다. 이 번역은 AI가 생성했으며 원어민의 검토를 받지 않았습니다.

### 참고 자료

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-am"></a>

## አማርኛ — የደህንነት ግምገማ እና ትምህርት

OWASP ይማሩ፣ የበለጠ ደህንነት ያለው ኮድ ይጻፉ፣ የማንኛውንም ፕሮጀክት commit ይገምግሙ። ይህ skill MCP፣ LLM መተግበሪያዎችን፣ ወኪሎችን እና skill ጥቅሎችንም ይሸፍናል።

### መጫን

የsecurity-review አቃፊን ወደ ፕሮጀክትዎ .agents/skills/ ማውጫ ይቅዱ። ሊሠሩበት ከሚፈልጉት ፕሮጀክት ውስጥ skillን ይጥሩ።

### ምሳሌዎች

```text
$security-review ይህን commit ገምግም እና ለሚቀጥሉትም ንቁ ሁን።
$security-review ይህን ባህሪ ከተግባራዊ እና ከደህንነት ፈተናዎች ጋር እንድገነባ እርዳኝ።
$security-review በአንድ ጊዜ አንድ ጥያቄ እየጠየቅህ የMCP ደህንነትን አስተምረኝ።
```

### አሠራር እና ገደቦች

Skillው ወቅታዊ ኦፊሴላዊ ምንጮችን ይመለከታል፣ ችግሮችንና መፍትሔዎችን ያብራራል፣ በእርግጥ የተካሄዱ ፈተናዎችንም ይገልጻል። ሕጋዊ አጠቃቀምን እና ያልተፈቀዱ ድርጊቶችን ለመፈተን ይረዳል። ትምህርቱን ከመልሶችዎ ጋር ያስማማል።

በወኪሉ ክፍለ ጊዜ ውስጥ ብቻ ንቁ ይሆናል፤ ክፍለ ጊዜው ካለቀ በኋላ Gitን አይከታተልም። ይህ ትርጉም በAI የተዘጋጀ ሲሆን በአፍ መፍቻ ተናጋሪ አልተገመገመም።

### ምንጮች

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-th"></a>

## ไทย — การตรวจสอบความปลอดภัยและการเรียนรู้

เรียนรู้ OWASP เขียนโค้ดให้ปลอดภัยขึ้น และตรวจสอบ commit ของโครงการใดก็ได้ สกิลนี้ครอบคลุม MCP แอปพลิเคชัน LLM เอเจนต์ และแพ็กเกจสกิลด้วย

### การติดตั้ง

คัดลอกโฟลเดอร์ security-review ไปไว้ในไดเรกทอรี .agents/skills/ ของโครงการ แล้วเรียกใช้สกิลจากโครงการที่ต้องการทำงาน

### ตัวอย่าง

```text
$security-review ตรวจสอบ commit นี้และคงสถานะทำงานไว้สำหรับ commit ถัดไป
$security-review ช่วยพัฒนาฟีเจอร์นี้พร้อมการทดสอบการทำงานและความปลอดภัย
$security-review สอนความปลอดภัย MCP ด้วยแบบทดสอบ โดยถามทีละข้อ
```

### การทำงานและข้อจำกัด

สกิลตรวจสอบแหล่งข้อมูลทางการล่าสุด อธิบายปัญหาและวิธีแก้ไข และรายงานว่ารันการทดสอบใดจริง ระหว่างพัฒนาจะช่วยทดสอบทั้งการใช้งานที่ถูกต้องและการกระทำที่ไม่ได้รับอนุญาต พร้อมปรับบทเรียนตามคำตอบ

สกิลทำงานอยู่ภายในเซสชันของเอเจนต์เท่านั้น และไม่เฝ้าดู Git หลังเซสชันจบ คำแปลนี้สร้างโดย AI และยังไม่ได้รับการตรวจทานจากเจ้าของภาษา

### แหล่งอ้างอิง

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-jv"></a>

## Basa Jawa — Priksa keamanan lan sinau

Sinaua OWASP, tulisen kode sing luwih aman, lan priksa commit ing proyek apa wae. Skill iki uga nyakup MCP, aplikasi LLM, agen, lan paket skill.

### Instalasi

Salinen folder security-review menyang direktori .agents/skills/ ing proyekmu. Undangen skill saka proyek sing arep digarap.

### Tuladha

```text
$security-review Priksa commit iki lan tetep aktif kanggo commit sabanjure.
$security-review Tulung aku nggawe fitur iki nganggo tes fungsi lan tes keamanan.
$security-review Wulangana aku keamanan MCP nganggo kuis, takon siji-siji.
```

### Cara kerja lan watesan

Skill mriksa sumber resmi paling anyar, nerangake masalah lan carane ndandani, sarta nglaporake tes sing tenan ditindakake. Nalika nulis kode, skill mbantu nguji panggunaan sing sah lan tumindak tanpa idin. Piwulang dicocogake karo wangsulanmu.

Skill mung aktif sajrone sesi agen; ora ngawasi Git sawise sesi rampung. Terjemahan iki digawe AI lan durung dipriksa dening panutur asli.

### Rujukan

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)

---

<a id="lang-it"></a>

## Italiano — Revisione della sicurezza e apprendimento

Studia OWASP, scrivi codice più sicuro e controlla i commit di qualsiasi progetto. La skill copre anche MCP, applicazioni LLM, agenti e pacchetti di skill.

### Installazione

Copia la cartella security-review nella directory .agents/skills/ del progetto. Invoca la skill dal progetto su cui vuoi lavorare.

### Esempi

```text
$security-review Controlla questo commit e rimani attiva per i successivi.
$security-review Aiutami a implementare questa funzionalità con test funzionali e di sicurezza.
$security-review Insegnami la sicurezza MCP con un quiz, una domanda alla volta.
```

### Comportamento e limiti

La skill consulta fonti ufficiali aggiornate, spiega problemi e correzioni e indica quali test ha davvero eseguito. Durante lo sviluppo aiuta a verificare gli usi legittimi e le azioni non autorizzate. Adatta le lezioni alle tue risposte.

Rimane attiva nella sessione dell’agente; non monitora Git dopo la sua conclusione. Questa traduzione è stata generata dall’IA e non è stata revisionata da una persona madrelingua.

### Riferimenti

- [OWASP](security-review/references/owasp.md)
- [MCP / LLM / AI](security-review/references/ai-security.md)
- [Tests](security-review/references/security-tests.md)
- [Learning](security-review/references/learning.md)
- [Evaluation](evals/README.md)
