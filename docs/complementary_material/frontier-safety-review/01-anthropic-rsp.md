# Revisión: Anthropic — Responsible Scaling Policy (RSP)

## Identificación del documento

- **Título exacto:** Anthropic's Responsible Scaling Policy (Version 3.3)
- **Versión:** 3.3
- **Fecha de vigencia:** May 26, 2026
- **URL oficial (versión PDF):** https://cdn.sanity.io/files/4zrzovbb/website/c11e84981d0a7281a1b229f3fa6af0da66eaf43f.pdf
- **Página de índice de versiones:** https://www.anthropic.com/responsible-scaling-policy
- **Documento analizado:** RSP v3.3 (versión más reciente pública al 19 de junio de 2026), con referencias cruzadas a v2.1 (March 31, 2025) y v3.0 (February 24, 2026) para mayor cobertura.

---

## Las 5 preguntas de research

### Q1: ¿Menciona evaluación en idiomas distintos del inglés?

**Respuesta: No**

El texto completo del RSP v3.3 (1.310 líneas extraídas via pdftotext) no contiene ninguna mención a "language", "multilingual", "English", "Spanish", "Portuguese", ni ningún idioma específico. La búsqueda fue exhaustiva en v3.3, v3.0 y v2.1: resultado cero en los tres documentos.

La única referencia relevante encontrada en el ecosistema Anthropic —pero **fuera** del RSP— es la iniciativa de third-party evaluations (blog post separado, no parte del RSP):

> "Capability benchmarks often aren't available across most of the world's languages. We'd like to support capability evaluations that support multiple languages."

Esta declaración aparece en https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations, no en el RSP. El RSP en sí es completamente silencioso sobre idiomas.

**Conclusión para el paper:** Ausencia total de mención a idiomas en el documento normativo central. La preocupación por la cobertura multilingüe existe en documentos auxiliares, pero no se traduce en compromisos o requisitos dentro del marco de escalonamiento responsable.

---

### Q2: ¿Sus benchmarks de capacidades peligrosas (CBRN, cyber, autonomía) existen o se evalúan en español/portugués?

**Respuesta: No**

El RSP v2.1 (que contiene la definición técnica más detallada de los umbrales CBRN) define los evaluados de la siguiente manera:

> "CBRN-3: The ability to significantly assist individuals or groups with basic STEM backgrounds in obtaining, producing, or deploying CBRN weapons. We assess this by comparing what potential attackers could achieve with full model access versus 2023-level online resources, assuming they have funding and up to one year of time to invest, but no initial specialized expertise."
> — RSP v2.1, Appendix C: Detailed Capability Thresholds

> "CBRN-4: The ability to substantially uplift CBRN development capabilities of moderately resourced state programs (with relevant expert teams), such as by novel weapons design, substantially accelerating existing processes, or dramatic reduction in technical barriers. We currently define this as uplifting a team of people with skills equivalent to entry-level PhD biologists to be able to approximate the capabilities of a world-class, state-backed bioweapons team."
> — RSP v2.1, Appendix C

El RSP v3.3 ajusta el umbral de CBRN no-novedoso:

> "Non-novel chemical/biological weapons production. AI systems with the ability to significantly help individuals or groups with basic technical backgrounds (e.g., undergraduate STEM degrees) create/obtain and deploy chemical and/or biological weapons with serious potential for catastrophic damages."
> — RSP v3.3, Section 1 (Capability or usage threshold table)

Ninguno de estos umbrales especifica el idioma en que deben conducirse las evaluaciones. El RSP v3.3 también adopta una postura deliberadamente flexible sobre metodología:

> "For now, our evaluations will focus specifically on AI R&D, as this domain likely plays to AI systems' current strengths and is more tractable to assess than capabilities in other domains."
> — RSP v3.3, Section 1

**Conclusión para el paper:** Los benchmarks de CBRN, cyber y autonomía son definidos en términos abstractos de capacidad técnica y umbrales de "uplift", sin especificar idioma. Las evaluaciones de uplift biológico se condujeron en inglés (evidenciado por los system cards: "human uplift studies with biodefense experts"), pero el RSP no lo estipula ni lo requiere explícitamente.

---

### Q3: ¿El red-teaming independiente/externo especifica que debe hacerse en múltiples idiomas?

**Respuesta: No**

El RSP v2.1 especifica red-teaming de la siguiente forma:

> "Red-teaming: Conduct red-teaming that demonstrates that threat actors with realistic access levels and resources are highly unlikely to be able to consistently elicit information from any generally accessible systems that greatly increases their ability to cause catastrophic harm relative to other available tools."
> — RSP v2.1, Section 4.1 (ASL-3 Deployment Standard), item 3

> "periodic, broadly scoped, and independent testing with expert red-teamers who are industry-renowned and have been recognized in competitive challenges."
> — RSP v2.1, Section 4.2 (ASL-3 Security Standard), item 3 (Audits)

El RSP v3.3 menciona red-teaming en tres contextos:

> "red-teaming, bug bounties, and threat intelligence for continually assessing the threat of jailbreaks"
> — RSP v3.3, Section 1 (Mitigations—our plan as a company)

> "adversarial red-teaming to test our auditing methods"
> — RSP v3.3, Section 2 (Frontier Safety Roadmap)

> "Develop our internal red-teaming of our deployment safeguards to the point where our internal red-teaming performs better at finding potential jailbreaks than the collective abilities of the participants in our established bug bounty programs."
> — RSP v3.3, Section 2 (Frontier Safety Roadmap)

Ninguna de estas menciones hace referencia a requisitos de idioma, cobertura lingüística, ni diversidad geográfica de los red-teamers.

**Conclusión para el paper:** El red-teaming externo es un componente explícito del RSP, pero los criterios de selección de evaluadores se refieren exclusivamente a expertise técnica ("industry-renowned", "knowledgeable about potential ways such evaluations might be misleading") y ausencia de conflictos de interés. No se incluye la diversidad lingüística o geográfica como criterio ni como recomendación.

---

### Q4: ¿Menciona Global South, LATAM, o países en desarrollo en algún contexto?

**Respuesta: No**

Búsqueda exhaustiva en los tres documentos (v3.3, v3.0, v2.1) con términos: "global south", "latin america", "latam", "developing countr", "low-income", "emerging market", "africa", "asia", "india", "brazil", "mexico". Resultado: cero coincidencias en los tres documentos.

Las únicas referencias geográficas en el RSP son:

1. Regulación nacional y armonización entre países (en abstracto):
   > "To the extent this takes the form of national regulation, different countries should attempt to harmonize their governance, including standards of evidence, to avoid a race to the bottom."
   > — RSP v3.3, Section 1

2. Referencia al "global balance of power" como contexto de amenaza (no como beneficiario):
   > "AI systems that can fully automate, or otherwise dramatically accelerate, the work of large, top-tier teams of human researchers in domains where fast progress could cause threats to international security and/or rapid disruptions to the global balance of power."
   > — RSP v3.3, Section 1 (Automated R&D threshold)

**Conclusión para el paper:** La ausencia es total y consistente entre versiones. El RSP opera con una lógica de "frontier AI developers" que implícitamente corresponde a actores con recursos de alto nivel (top-tier research teams, state-sponsored programs), sin considerar la perspectiva de regiones periféricas como objetos de riesgo ni como agentes de gobernanza.

---

### Q5: ¿Sus umbrales de riesgo consideran contextos de baja infraestructura (sin GPU, sin equipo de seguridad local)?

**Respuesta: No**

El RSP no menciona "GPU", "compute capacity" en el sentido de restricción de acceso, ni "local safety teams" ni "low-infrastructure" en ninguna versión analizada.

La definición de "moderately resourced" en el contexto de CBRN-3 es la más cercana a una consideración de recursos, pero opera en dirección contraria: define el umbral de amenaza (qué puede hacer un actor con recursos moderados), no el contexto de despliegue:

> "We assess this by comparing what potential attackers could achieve with full model access versus 2023-level online resources, assuming they have funding and up to one year of time to invest, but no initial specialized expertise."
> — RSP v2.1, Appendix C

La única referencia a "compute" en v3.3 aparece en el contexto de métricas de evaluación de capacidad de entrenamiento:

> "We adjusted the comprehensive assessment cadence to 4x Effective Compute or..."
> — RSP v3.3, Changelog (RSP v2.0 changes)

**Conclusión para el paper:** Los umbrales de riesgo asumen implícitamente un contexto de infraestructura mínimamente suficiente (acceso a modelos, equipos de investigación, recursos computacionales). No se contempla cómo los riesgos se distribuyen o amplifican en contextos donde la infraestructura de seguridad es escasa: ausencia de equipos locales de respuesta a incidentes, limitaciones de conectividad para monitoreo, o barreras para implementar las mitigaciones de deployment recomendadas.

---

## Nota de diferencias y aspectos propios de este framework

El RSP de Anthropic es el framework más maduro y estructurado del ecosistema (v3.3 es ya la octava iteración desde 2023), y presenta características distintivas relevantes para una agenda de AI Safety con perspectiva de equidad global:

**1. Explícita separación entre compromisos unilaterales y recomendaciones para la industria.** El RSP v3.0 introdujo esta distinción: Anthropic ya no se compromete a implementar mitigaciones independientemente de lo que hagan los competidores cuando eso podría resultar en una pérdida de cuota de mercado para el actor más responsable. Esta lógica de "collective action problem" es sofisticada pero implícitamente asume que los actores relevantes son los frontier AI developers del Norte Global.

**2. El sistema de ASL (AI Safety Levels) como estructura de umbrales progresivos** es exportable por diseño ("our approach to risk should be exportable" — RSP v2.1, Introduction), pero la exportabilidad se entiende como adopción del mismo framework por otros developers, no como adaptación a contextos con capacidades asimétricas.

**3. Risk Reports con revisión externa** son una innovación del RSP v3.0. Los criterios para seleccionar reviewers externos (sección 3.6.1) exigen expertise en evaluaciones de capacidades peligrosas, reputación de independencia, y ausencia de conflictos de interés financiero con Anthropic. No se menciona diversidad geográfica, cultural, o lingüística como criterio.

**4. El modelo de amenaza dominante** es bipolar: actores individuales con background STEM básico (CBRN-3) y programas estatales bien recursos (CBRN-4). No hay consideración de cómo los mismos modelos pueden ser instrumentalizados en contextos de conflicto de baja intensidad, represión estatal en economías emergentes, o desinformación en idiomas distintos del inglés.

**5. Ausencia de perspectiva de beneficiario.** El RSP define con detalle a quiénes proteger *de* (threat actors), pero no especifica a quiénes proteger *para*. El único indicio es la frase del objetivo final: "make sure that the benefits of our models exceed their costs" — pero sin desagregar quién recibe los beneficios y quién asume los costos.

---

## Fuentes consultadas

- RSP v3.3 (PDF): https://cdn.sanity.io/files/4zrzovbb/website/c11e84981d0a7281a1b229f3fa6af0da66eaf43f.pdf
- RSP v3.0 (PDF): https://www-cdn.anthropic.com/e670587677525f28df69b59e5fb4c22cc5461a17.pdf
- RSP v2.1 (PDF): https://www-cdn.anthropic.com/17310f6d70ae5627f55313ed067afc1a762a4068.pdf
- Versiones y actualizaciones: https://www.anthropic.com/responsible-scaling-policy
- Iniciativa de evaluaciones de terceros: https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations
- Transparency Hub / Model Report: https://www.anthropic.com/transparency/model-report
