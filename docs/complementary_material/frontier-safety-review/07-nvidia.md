# NVIDIA — Frontier AI Risk Assessment

**Título oficial:** FRONTIER AI RISK ASSESSMENT  
**Versión / fecha:** "Applicable from August 2025" (sin número de versión explícito)  
**Autores:** Barnaby Simkin, Nikki Pope, Leon Derczynski, Christopher Parisien  
**URL:** https://images.nvidia.com/content/pdf/NVIDIA-Frontier-AI-Risk-Assessment.pdf  
**Extensión:** 15 páginas (PDF)  
**Naturaleza del documento:** White paper técnico-formal, no un marco regulatorio externo. Describe el sistema interno de evaluación de riesgos de NVIDIA para modelos de IA de frontera.

---

## Análisis: 5 Preguntas

---

### Q1. ¿Menciona evaluación en idiomas distintos del inglés?

**Respuesta: No**

El documento no menciona en ningún momento la evaluación de modelos en idiomas distintos del inglés. La única referencia a "language" en el contexto relevante es descriptiva del tipo de producto:

> "AI model files which are designed to have specific capabilities, such as image classification, **language translation**, or anomaly detection." (sección: Detailed Risk Assessment — Use case specification)

El término "language translation" aparece únicamente como ejemplo de tipo de capacidad de modelo (MR1 en la tabla de riesgo), no como criterio de evaluación de seguridad. No hay mención de evaluaciones multilingües, de cobertura lingüística en benchmarks, ni de diversidad de idiomas en ninguna parte del framework.

---

### Q2. ¿Sus benchmarks de capacidades peligrosas existen o se evalúan en español/portugués?

**Respuesta: No**

El documento lista los siguientes benchmarks de capacidades peligrosas y riesgo frontera:

> "TruthfulQA, FEVER, and GLUE test a model's tendency to generate false or misleading content. BBQ and BOLD test open-ended generation for biased language. WMDP benchmark serves as both a proxy evaluation for hazardous knowledge in large language models (LLMs) and a benchmark for unlearning methods to remove such knowledge." (sección: Risk evaluation)

Y menciona adicionalmente: MBPP, MoleculeNet, ARC, AILuminate v1.0 (MLCommons).

Ninguno de estos benchmarks es descrito con cobertura en español o portugués. No se hace ninguna mención a variantes multilingües, ni se señala la ausencia de cobertura en esos idiomas como una limitación conocida.

---

### Q3. ¿El red-teaming independiente/externo especifica múltiples idiomas?

**Respuesta: No**

El documento describe el red-teaming de la siguiente manera:

> "In adversarial red teaming, expert human operators deliberately probe a frontier AI model's vulnerability and attempt to induce it to produce harmful, biased, or disallowed outputs. The red team also probes each guardrail component independently with targeted examples to identify weaknesses and improve performance in edge cases." (sección: Risk evaluation)

> "These human adversaries are able to leverage domain knowledge, creativity, and context-awareness to simulate realistic attack strategies." (ibid.)

No se especifica que el red-teaming deba realizarse en múltiples idiomas. No hay mención de equipos multilingües, de pruebas en idiomas distintos al inglés, ni de consideraciones sobre jailbreaks o ataques adversariales en otras lenguas. El red-teaming descrito es esencialmente monolingüe por omisión.

Adicionalmente, NVIDIA menciona Garak (su escáner de vulnerabilidades LLM de código abierto) como herramienta de red-teaming automatizado:

> "NVIDIA runs and supports the Garak LLM vulnerability scanner. This constantly updated public project collects techniques for exploiting LLM and multi-modal model vulnerabilities." (ibid.)

Garak tiene alguna capacidad multilingüe como proyecto, pero el documento no la menciona ni la requiere.

---

### Q4. ¿Menciona Global South, LATAM, o países en desarrollo?

**Respuesta: No**

No se encontró ninguna mención de "Global South", "Latin America", "LATAM", "developing countries", "emerging economies", "países en desarrollo" ni ningún término equivalente en todo el documento. La geografía está completamente ausente del framework. Los riesgos se tratan como universales y sin diferenciación regional.

---

### Q5. ¿Sus umbrales de riesgo consideran contextos de baja infraestructura?

**Respuesta: No**

Los umbrales de riesgo del framework (MR1–MR5) se basan en tres criterios: caso de uso previsto, capacidades del modelo, y nivel de autonomía:

> "Risk categories are allocated by looking at what the model is designed to do (its capabilities), where it will be deployed (its use case), and how autonomously it operates (level of autonomy)." (sección: Preliminary Risk Assessment)

El término "infrastructure" aparece una sola vez en el documento, en referencia técnica a la arquitectura de despliegue del modelo:

> "...with no user interface, deployment infrastructure, or additional logic." (sección: Detailed Risk Assessment)

No hay ninguna consideración de infraestructura de conectividad, capacidad institucional local, recursos computacionales limitados del usuario final, ni diferencias de contexto socioeconómico que afecten los umbrales de riesgo. El framework presupone implícitamente entornos de despliegue con alta capacidad tecnológica.

---

## Diferencias respecto a otros frameworks analizados

El framework de NVIDIA presenta varias diferencias estructurales importantes en relación con los de otros actores del ecosistema frontier (Anthropic, Google DeepMind, OpenAI, UK AISI):

1. **Foco en proveedor de infraestructura, no de modelos frontier propios.** El documento reconoce explícitamente que "frontier AI models are not currently under development at NVIDIA", lo que hace que el framework sea parcialmente hipotético. Esto lo distingue de frameworks de laboratorios que evalúan modelos que ya despliegan.

2. **Ausencia total de dimensiones geográficas, culturales o lingüísticas.** A diferencia de frameworks que al menos mencionan diversidad lingüística o biases culturales, el documento de NVIDIA es completamente silencioso al respecto.

3. **Enfoque de ingeniería de sistemas.** El framework adopta metodología de safety engineering clásica (v-model, risk = likelihood × severity × observability), lo que es más maduro en términos de proceso técnico pero más estrecho en alcance societal.

4. **Red-teaming interno sin mandato externo.** No hay mención de evaluaciones por terceros independientes ni organismos externos, a diferencia de frameworks que exigen auditorías externas para MR5.

5. **Benchmarks estándar sin adaptación regional.** Los benchmarks listados (TruthfulQA, WMDP, BBQ, BOLD, etc.) son todos datasets en inglés. No hay mención de planes de expansión multilingüe ni reconocimiento de esta brecha.

6. **Brevedad relativa.** Con 15 páginas, el documento es considerablemente más corto que los frameworks de Anthropic o Google DeepMind (que típicamente superan las 40-60 páginas), lo que refleja un alcance más acotado.
