# Microsoft — Frontier Governance Framework

**Versión:** Version 1 (February 2025)  
**Fecha de publicación:** 8 February 2025  
**URL oficial:** https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Microsoft-Frontier-Governance-Framework.pdf  
**Páginas:** 14 (incluyendo apéndices)

---

## Análisis de 5 preguntas clave

---

### Q1. ¿Menciona evaluación en idiomas distintos del inglés?

**Respuesta: No**

El documento no contiene ninguna mención a idiomas distintos del inglés en el contexto de evaluaciones. Los benchmarks de capacidades generales listados en la Sección 3 son:

- General reasoning
- Scientific and mathematical reasoning
- Long-context reasoning
- Spatial understanding and awareness
- Autonomy, planning, and tool use
- Advanced software engineering

La única referencia vagamente relevante a diversidad lingüística/cultural aparece en la Sección 1, al mencionar riesgos que son "culturally contextual" y gobernados por el programa más amplio — pero sin especificar idiomas ni evaluación multilingüe:

> "more culturally contextual risks that are heavily shaped by use case and deployment environments, as well as laws and norms that vary across regions." (Section 1, §3)

Esta mención delega la diversidad cultural al programa de gobernanza más amplio (Responsible AI Program), sin que el FGF mismo la operacionalice. **No se encontró mención explícita a evaluación multilingüe.**

---

### Q2. ¿Sus benchmarks de capacidades peligrosas existen o se evalúan en español/portugués?

**Respuesta: No**

El framework describe dos niveles de evaluación:

1. **Leading indicator assessment** (Sección 3): usa "state-of-the-art benchmarks" para capacidades generales. No se nombra ningún benchmark específico, y no hay mención a versiones en español, portugués ni otros idiomas.

2. **Deeper capability assessment** (Sección 3): incluye "adversarial testing and systematic measurement using state-of-the-art methods" para CBRN, ciber-operaciones y autonomía avanzada. No se especifica que estos tests operen en múltiples idiomas.

La única especificación sobre qué criterios deben cumplir los benchmarks es una nota al pie:

> "For a benchmark to be included in our suite of leading indicator assessments it must: 1) have low saturation (i.e., the best performing models typically score lower than 70%); 2) measure an advanced capability, for example, mathematical reasoning, rather than an application-oriented capability like financial market prediction; and 3) have a sufficient number of prompts to account for non-determinism in model output." (Section 3, footnote 1)

Ninguno de estos criterios incluye diversidad lingüística. **No se encontró mención a evaluación en español ni portugués.**

---

### Q3. ¿El red-teaming independiente/externo especifica múltiples idiomas?

**Respuesta: No**

El framework menciona actores externos en dos contextos:

**Capability evaluation** (Sección 3):
> "As appropriate, evaluations involve qualified and expert external actors that meet relevant security standards, including those with domain-specific expertise." (Section 3, Deeper capability assessment)

**Advanced security red teaming** (Sección 4):
> "Advanced security red teaming, using third parties where appropriate, to reasonably simulate relevant threat actors seeking to steal the model weights so that security safeguards are robust." (Section 4, Security measures)

En ambos casos, la especialización mencionada es de **dominio técnico** (seguridad, CBRN, cyber) o de **amenazas de seguridad**, no de diversidad lingüística o geográfica. **No se encontró ninguna mención a red-teaming multilingüe o en idiomas específicos distintos del inglés.**

---

### Q4. ¿Menciona Global South, LATAM, o países en desarrollo?

**Respuesta: No**

El documento no contiene ninguna mención a "Global South", "Latin America", "LATAM", "developing countries", "emerging economies" ni términos equivalentes. La única referencia a diversidad geográfica es genérica y aparece en el contexto de variación legal y normativa:

> "laws and norms that vary across jurisdictions" (Section 2, Integrated governance)

> "laws and norms that vary across regions" (Section 1, §3)

Estas menciones reconocen que las normas varían por región, pero lo hacen en el contexto de delegar esa complejidad al programa de gobernanza más amplio (Responsible AI Program), no en el marco del FGF mismo. **No se encontró mención a Global South, LATAM ni países en desarrollo.**

---

### Q5. ¿Sus umbrales de riesgo consideran contextos de baja infraestructura?

**Respuesta: No**

El Apéndice I define umbrales de capacidad (capability thresholds) para tres categorías: CBRN, ciber-operaciones, y autonomía avanzada. Los umbrales están definidos en función del nivel de pericia del actor amenazante (e.g., "PhD level education", "low-skilled actor", "STEM education") y del tipo de daño técnico posible.

Por ejemplo, en CBRN:
> "Critical: The model provides a meaningful uplift to an expert's ability to develop a highly dangerous novel threat or significantly lowers the barriers to a low-skilled actor developing and delivering a known CBRN threat." (Appendix I, CBRN)

Los factores contextuales externos al modelo se mencionan brevemente en la Sección 3:
> "This holistic risk assessment also considers the marginal capability uplift a model may provide over and above currently available tools and information, including currently available open-weights models." (Section 3, Deeper capability assessment — Holistic risk assessment)

Y en la Sección 6:
> "more holistic risk assessment techniques that appropriately factor in considerations outside of model capabilities, such as system-level mitigations, as well as societal and institutional factors external to the AI system that can impact whether and how a hazard materializes and the scale of its impact." (Section 6)

Esta última mención reconoce que factores institucionales y societales importan, pero los identifica como trabajo futuro y no los operacionaliza en los umbrales actuales. No hay ninguna referencia a infraestructura tecnológica local, conectividad, capacidad institucional de respuesta, ni variación de riesgo según contexto de desarrollo. **No se encontró mención a contextos de baja infraestructura.**

---

## Párrafo de diferencias y brechas

El Microsoft Frontier Governance Framework (v1, febrero 2025) es un documento técnicamente riguroso en su dominio de aplicación: riesgos de seguridad nacional y seguridad pública a escala derivados de capacidades avanzadas de modelos de IA (CBRN, ciber-operaciones, autonomía avanzada). Sin embargo, presenta brechas sistemáticas en cuanto a representación geográfica y lingüística.

El framework no menciona en ningún punto evaluaciones en idiomas distintos del inglés, no especifica criterios de diversidad lingüística para los benchmarks ni para el red-teaming externo, y no hace referencia alguna al Global South, América Latina o países en desarrollo. Los umbrales de riesgo del Apéndice I están construidos sobre variables técnicas universalizadas (nivel educativo del atacante, tipo de arma) sin calibrar para contextos de menor infraestructura institucional o tecnológica.

Esta omisión es significativa: un modelo que "lowers the barriers to a low-skilled actor" en un país con altas capacidades de respuesta de emergencias puede tener un perfil de riesgo muy diferente al mismo modelo en un país con baja capacidad institucional. La Sección 6 reconoce vagamente que "societal and institutional factors external to the AI system can impact whether and how a hazard materializes", pero los identifica como trabajo futuro sin incluirlos en los umbrales operacionales actuales. En contraste con el alcance geográfico explícito de algunos frameworks de otras organizaciones, el FGF de Microsoft opera con una noción implícita de riesgo homogéneo a nivel global, sin diferenciar por región, idioma ni contexto de desarrollo.

---

*Análisis realizado el 2026-06-19. Documento fuente: Version 1, 8 February 2025.*
