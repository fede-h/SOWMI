# Naver — AI Safety Framework (ASF) Beta

**Versión:** Beta (publicada noviembre–diciembre 2024)
**URL oficial (EN):** https://clova.ai/en/tech-blog/en-navers-ai-safety-framework-asf
**URL oficial (KO):** https://clova.ai/tech-blog/ko-naver-ai-safety-framework-asf
**Organización:** NAVER Corporation / NAVER Cloud (Corea del Sur)
**Evaluación independiente:** https://ratings.safer-ai.org/company/naver/ (Safer AI — Oct 2025: 0.5/5)

---

## Contexto

NAVER es el principal portal de Internet de Corea del Sur y desarrollador de HyperCLOVA X. Su ASF se enmarca explícitamente en la narrativa de "sovereign AI": la tesis de que cada nación/región debe poder desarrollar modelos que reflejen su cultura, idioma e historia, en contraposición a la concentración en modelos angloamericanos. Es uno de los doce frameworks de frontier AI safety reconocidos a nivel global (junto a Anthropic, OpenAI, Google DeepMind, Meta, etc.).

---

## 5 Preguntas de Análisis

### Q1: ¿Menciona evaluación en idiomas distintos del inglés?

**Parcial**

El framework menciona explícitamente el coreano como lengua de evaluación, y reconoce la insuficiencia de los benchmarks anglófonos. No menciona evaluación en ningún otro idioma.

> Cita (versión coreana, sección de benchmarks): *"기존의 영미권 문화를 바탕으로 만들어진 벤치마크 데이터에 한국의 특성을 반영하는 연구를 진행"*
> ("Se realizó investigación para incorporar características coreanas en benchmarks desarrollados originalmente desde marcos culturales angloamericanos.")

> Cita (versión inglesa, sección cultural): *"training and evaluating language models with local datasets within the proper cultural and societal context."*

El "local" aquí se refiere exclusivamente a Corea. No se menciona evaluación en inglés como lengua de seguridad per se, ni en ningún otro idioma.

---

### Q2: ¿Sus benchmarks de capacidades peligrosas existen o se evalúan en español/portugués? (o solo coreano/inglés)

**No**

Los únicos benchmarks de seguridad mencionados son tres datasets en coreano aplicados a HyperCLOVA X:

- **SQuARe** — benchmark coreano de seguridad general
- **KoSBi** — dataset de sesgo social en coreano para clasificadores de contenido seguro
- **KoBBQ** — benchmark coreano de sesgo (Korean Bias Benchmark for Question Answering)

> Cita (versión inglesa): *"NAVER's partnerships [...] have led to meaningful research in building local datasets specialized to Korean culture and society and creating benchmarks for evaluating Korean-centric models, including SQuARe, KoSBi, and KoBBQ datasets which are applied to our HyperCLOVA X models."*

No se menciona ningún benchmark en español, portugués, francés, árabe ni ningún otro idioma. No existe en el ASF una evaluación de capacidades peligrosas en idiomas distintos del coreano (y por extensión inglés, ya que HyperCLOVA X es bilingüe Ko/En).

---

### Q3: ¿El red-teaming independiente/externo especifica múltiples idiomas?

**No**

El framework describe un ejercicio de red-teaming realizado en abril de 2024 ("Generative AI Red Team Challenge") con agencias gubernamentales y empresas del sector, evaluando siete dominios:

> Cita (versión inglesa): *"LLMs for signs of harmful content across seven domains—human rights violation, disinformation, inconsistency, cyberattacks, bias and discrimination, illegal content, and jailbreaking."*

No se especifica en qué idioma o idiomas se realizaron las pruebas. Los participantes son coreanos (agencias gubernamentales coreanas, empresas de IA coreanas). La evaluación de Safer AI (ratings.safer-ai.org, Oct 2025) asigna **0%** en identificación de riesgos desconocidos, señalando: *"The framework doesn't mention any procedures pre-deployment to identify novel risk domains"* para red-teaming interno ni externo. No hay cláusula de diversidad lingüística en el red-teaming.

---

### Q4: ¿Menciona Global South, LATAM, o países en desarrollo?

**No**

El framework no contiene ninguna mención de Global South, América Latina, países en desarrollo, o regiones específicas fuera de Corea. El discurso de "sovereign AI" es universal en intención pero coreano en implementación concreta.

Las declaraciones de liderazgo (externas al documento ASF, pero relacionadas) apuntan a una aspiración de escala global:

> CEO Choi Soo-yeon: *"We believe we can also present a new alternative to other countries that want to grow their AI industry."*

> Fundador Lee Hae-jin: *"Naver will provide technological support to create various AI models that respect and understand the cultures and values of different regions with responsibility so that countries around the world can have an independent, sovereign AI."*

Estas son aspiraciones estratégicas, no compromisos operativos dentro del ASF. El documento en sí no menciona LATAM, Sur Global ni países en desarrollo.

---

### Q5: ¿Sus umbrales de riesgo consideran contextos de baja infraestructura?

**No**

Los umbrales operativos del ASF son:

> Cita (versión inglesa): *"Every 3 months, or when performance increases by 6x"* (evaluación de frontier AI).

> Cita sobre métricas proxy: *"the amount of computing can serve as an indicator when measuring capabilities."*

La evaluación de Safer AI señala: *"No KRIs are given for loss of control risks"* y que los umbrales están *"not expressed fully or partly quantitatively."* El marco asume implícitamente acceso a infraestructura computacional significativa como condición para medir riesgo. No hay ninguna mención de contextos de baja infraestructura, conectividad limitada, o despliegue en regiones con recursos computacionales restringidos.

---

## Diferencias Notables: El Ángulo Cultural/Lingüístico

El ASF de Naver es el único framework de frontier AI safety que parte explícitamente de una crítica al **anglocentrismo** de los benchmarks de seguridad existentes. Su contribución genuina es demostrar que los benchmarks de seguridad son culturalmente contingentes: los sesgos, definiciones de contenido dañino, y riesgos de desinformación no son universales, sino que dependen del contexto sociocultural.

Sin embargo, esta crítica se aplica **exclusivamente hacia adentro** (Corea/coreano). El framework no extrapola la misma lógica a otras culturas o idiomas no anglófonos. Hay una asimetría estructural: Naver argumenta con rigor que los modelos entrenados en cultura angloamericana son insuficientes para Corea, pero no aplica ese mismo argumento para evaluar si sus propios modelos son insuficientes para el árabe, el swahili, el español o el hindi.

El discurso de "sovereign AI" como diversidad cultural tiene potencial analítico para el AI Safety multilingual, pero en la práctica el ASF Beta es un **framework coreano-céntrico** que aún no operacionaliza la diversidad regional más allá de Corea–mundo anglófono. La puntuación de 0.5/5 de Safer AI refleja que, más allá del discurso, las estructuras de evaluación cuantitativa, red-teaming externo con diversidad lingüística, y umbrales de riesgo explícitos están ausentes o son muy débiles.

---

## Fuentes

- Documento oficial ASF (EN): https://clova.ai/en/tech-blog/en-navers-ai-safety-framework-asf
- Documento oficial ASF (KO): https://clova.ai/tech-blog/ko-naver-ai-safety-framework-asf
- Safer AI Risk Management Ratings — Naver: https://ratings.safer-ai.org/company/naver/
- Korea Times — Lee Hae-jin sobre diversidad cultural: https://www.koreatimes.co.kr/www/tech/2024/11/129_375111.html
- Prokerala — Naver unveils AI safety framework: https://www.prokerala.com/news/articles/a1540038.html
- METR — Common Elements of Frontier AI Safety Policies (Dec 2025): https://metr.org/blog/2025-12-09-common-elements-of-frontier-ai-safety-policies/
- MarkTechPost — HyperCLOVA X introduction: https://www.marktechpost.com/2024/04/06/naver-cloud-researchers-introduce-hyperclova-x-a-multilingual-language-model-tailored-to-korean-language-and-culture/
