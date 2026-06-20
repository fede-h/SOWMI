# 09 — Cohere: Secure AI Frontier Model Framework

**Documento oficial:** The Cohere Secure AI Frontier Model Framework
**Versión / Fecha:** Febrero 2025
**URL:** https://cohere.com/security/the-cohere-secure-ai-frontier-model-framework-february-2025.pdf
**Blog de anuncio:** https://cohere.com/blog/secure-model-framework

---

## Nota metodológica

El PDF oficial es de tipo imagen (no text-selectable), lo que impide extracción textual directa. El análisis se basa en:
1. Extractos textuales recuperados por búsqueda web indexada
2. El análisis comparativo publicado en Evaluating AI Providers' Frontier AI Safety Frameworks (arXiv 2512.01166v3)
3. El análisis de METR "Common Elements of Frontier AI Safety Policies" (marzo y diciembre 2025)
4. El blog de anuncio oficial (cohere.com/blog/secure-model-framework)

Todas las citas marcadas con [INDEXED] provienen de fragmentos indexados por motores de búsqueda o herramientas de análisis secundarias. Las marcadas con [NO ENCONTRADO] indican ausencia verificada tras búsqueda exhaustiva.

---

## Estructura del framework

El documento se organiza en cinco componentes:
1. Risk Identification
2. Risk Analysis & Evaluation
3. Risk Treatment
4. Transparency
5. Research and External Stakeholder Engagement

Principios fundacionales declarados:
- **Evidenced Risks**: "real-world risks that are known, measured, or observable"
- **Assessed in Context**: riesgo evaluado en el entorno operacional específico de Cohere y sus clientes
- **Holistically Managed**: seguridad "embedded by design into model and system development"

Estrategia central: defense-in-depth con controles en red, endpoint, identidad/acceso, datos.

---

## Las 5 preguntas

### Q1 — ¿Menciona evaluación en idiomas distintos del inglés?

**Respuesta: NO**

No se encontró ninguna mención a evaluación en idiomas distintos del inglés dentro del Secure AI Frontier Model Framework (febrero 2025).

El framework de Cohere se enfoca en riesgos para empresas y gobiernos ("real-world, practical challenges that enterprises and governments face today") sin especificar cobertura lingüística en sus evaluaciones de seguridad.

Contexto adicional relevante: Cohere Labs (la rama de investigación) ha publicado trabajos separados sobre seguridad multilingüe — en particular el paper "Towards Safe Multilingual Frontier AI" (arXiv 2409.13708, septiembre 2024) y trabajos sobre multilingual jailbreaks con los modelos Aya. Sin embargo, **este trabajo de investigación no está integrado ni citado dentro del Secure AI Frontier Model Framework**.

No se encontró mención. Ausencia confirmada por análisis secundarios (arXiv 2512.01166v3, METR 2025).

---

### Q2 — ¿Sus benchmarks de capacidades peligrosas existen o se evalúan en español/portugués?

**Respuesta: NO**

El framework no especifica benchmarks de capacidades peligrosas en ningún idioma. El análisis comparativo arXiv 2512.01166v3 asignó a Cohere 0% en "Open-ended red teaming" y 0% en "Evaluation Frequency", lo que indica que la documentación de evaluaciones de capacidades peligrosas es casi inexistente en el framework publicado.

Un red team externo (Enkrypt AI, "A Red Team Study on CBRN Capabilities in Frontier AI Models: Anthropic, OpenAI, Meta, Cohere, Mistral") evaluó a Cohere en capacidades CBRN, pero no hay evidencia de que esas pruebas se realizaran en español, portugués u otros idiomas. El reporte de Enkrypt AI no especifica diversidad lingüística en su metodología pública.

No se encontró mención de evaluaciones de capacidades peligrosas en español/portugués. Ausencia confirmada.

---

### Q3 — ¿El red-teaming independiente/externo especifica múltiples idiomas?

**Respuesta: PARCIAL** (menciona red-teaming externo, pero no idiomas)

El framework menciona red-teaming con partes externas independientes:

> "Red teaming exercises may include independent external parties, such as NIST and Humane Intelligence." [INDEXED — análisis secundario arXiv 2512.01166v3]

> "The framework laudably specifies the independence of the external testers." [INDEXED — arXiv 2512.01166v3, sección Risk Identification]

> "Cohere performs robust vulnerability management testing, including independent third-party penetration testing of model containers prior to major model releases." [INDEXED]

Sin embargo, **no se especifica** que el red-teaming se realice en múltiples idiomas. La cita del framework hace referencia a organizaciones independientes pero no a diversidad lingüística en los ejercicios. El score en red-teaming interno y externo (arXiv 2512.01166v3) fue 0% en "Open-ended red teaming", lo que sugiere que la documentación pública al respecto es mínima.

Parcial: se menciona independencia de testers externos, pero sin especificación de idiomas.

---

### Q4 — ¿Menciona Global South, LATAM, o países en desarrollo?

**Respuesta: NO**

No se encontró ninguna mención a Global South, LATAM, América Latina, países en desarrollo, o regiones geográficas específicas en el Secure AI Frontier Model Framework.

El framework está orientado a clientes empresariales y gubernamentales en general, sin diferenciación geográfica. La búsqueda exhaustiva (combinando términos "Global South", "LATAM", "Latin America", "developing", "low-resource" con el nombre del framework) no arrojó ningún resultado relevante del documento oficial.

No se encontró mención. Ausencia confirmada.

---

### Q5 — ¿Sus umbrales de riesgo consideran contextos de baja infraestructura?

**Respuesta: NO**

El framework define umbrales cualitativos de riesgo basados en niveles de seguridad escalables según "pre-mitigation scores" del modelo:

> "Any model that triggers leading indicator assessment is subject to robust baseline security protection." [INDEXED]

> "Security safeguards scaled up depending on the model's pre-mitigation scores." [INDEXED]

> "Security level 4 represents maximum safeguards with security strong enough to resist concerted attempts supported by state programs to steal model weights." [INDEXED]

Estos umbrales están orientados a la protección de pesos del modelo y acceso controlado, no a contextos de despliegue en baja infraestructura. El framework recibió 0% en umbrales cuantitativos (arXiv 2512.01166v3) y 0% en "Policy to halt development if controls insufficient". No se encontraron menciones a entornos de baja conectividad, países sin infraestructura cloud robusta, ni adaptaciones para contextos de despliegue en el Sur Global.

No se encontró mención. Ausencia confirmada.

---

## Análisis diferencial: ¿Qué hace distinto a Cohere?

### La paradoja multilingüe: liderazgo en investigación, silencio en gobernanza

Cohere es, posiblemente, la empresa de IA con el trabajo de investigación multilingüe más extenso entre las que han publicado un frontier safety framework. Sus modelos Aya (Aya 101, Aya 23, Aya Expanse) cubren hasta 101 idiomas. Su rama de investigación Cohere For AI (C4AI) ha producido:
- Trabajos sobre multilingual jailbreaks y cómo idiomas de bajos recursos son más vulnerables
- Datasets multilingües de instrucción (Aya Dataset, involucrando >3,000 investigadores en 119 países)
- Evaluaciones de seguridad multilingüe (multilingual safety context distillation, reducción de generaciones dañinas 78–89%)

**Sin embargo, nada de esto aparece en el Secure AI Frontier Model Framework.**

El framework es un documento de gobernanza y gestión de riesgos enfocado en clientes enterprise y gubernamentales. Su foco es la seguridad del modelo (model security, weight protection), no la seguridad inclusiva (inclusive safety). La brecha entre el trabajo de investigación de Cohere For AI y sus compromisos formales de gobernanza es la característica más notable de este framework.

### Debilidades estructurales documentadas

Según el análisis comparativo independiente (arXiv 2512.01166v3, score global: 8% vs. mediana de 18%):
- Score total de Cohere: **8%** (último lugar junto con Magic entre los evaluados)
- Red-teaming abierto (interno y externo): **0%**
- Frecuencia de evaluaciones documentada: **0%**
- Umbrales cuantitativos de riesgo: **0%**
- Validación de terceros de modelado de riesgos: **0%**

El framework prioriza la seguridad perimetral (network security, access controls, model weight protection) por sobre la evaluación sistemática de capacidades peligrosas — un reflejo de su orientación hacia clientes empresariales y gubernamentales con altos requisitos de seguridad operacional.

### Lo que el framework sí hace bien

- Enfoque en riesgos evidenciados ("evidenced risks") en lugar de riesgos puramente especulativos
- Priorización explícita de riesgos (risk prioritization score: 75%, el más alto entre evaluados)
- Rechazo explícito de ciertos riesgos catastróficos fuera de su ámbito (nuclear/radiológico, autonomía/auto-replicación)
- Especificación de independencia de los testers externos
- Programa de bug bounty para vulnerabilidades de IA

---

## Fuentes consultadas

- Documento oficial: https://cohere.com/security/the-cohere-secure-ai-frontier-model-framework-february-2025.pdf
- Blog de anuncio: https://cohere.com/blog/secure-model-framework
- Evaluating AI Providers' Frontier AI Safety Frameworks (arXiv 2512.01166v3): https://arxiv.org/html/2512.01166v3
- METR Common Elements of Frontier AI Safety Policies: https://metr.org/common-elements
- Towards Safe Multilingual Frontier AI (arXiv 2409.13708): https://arxiv.org/abs/2409.13708
- Enkrypt AI CBRN Red Team Study: https://www.enkryptai.com/company/resources/research-reports/red-teaming-cbrn
- AI Lab Watch commitments: https://ailabwatch.org/resources/commitments
