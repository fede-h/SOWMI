# Amazon — Frontier Model Safety Framework

**Versión:** v1 (sin número de versión explícito en el documento)  
**Fecha de publicación:** 9 de febrero de 2025  
**URL oficial (PDF):** https://assets.amazon.science/a7/7c/8bdade5c4eda9168f3dee6434fff/pc-amazon-frontier-model-safety-framework-2-7-final-2-9.pdf  
**Página de publicación:** https://www.amazon.science/publications/amazons-frontier-model-safety-framework  
**Extensión:** 8 páginas  

---

## Contexto

El Amazon Frontier Model Safety Framework (FMSF) fue publicado el 9 de febrero de 2025, en consonancia con el compromiso de Amazon con los Korea Frontier AI Safety Commitments. El documento describe los protocolos que Amazon seguirá para garantizar que sus modelos frontier no expongan capacidades que puedan generar riesgos severos. El marco es complementario a las prácticas más amplias de responsible AI de Amazon y se organiza en torno a tres dominios de riesgo crítico: (1) Proliferación de armas CBRN (Chemical, Biological, Radiological & Nuclear), (2) Operaciones cibernéticas ofensivas, y (3) I+D de IA automatizada. El compromiso central es: *"we will not deploy frontier AI models developed by Amazon that exceed specified risk thresholds without appropriate safeguards in place."*

Las evaluaciones aplicadas a modelos concretos (Nova 2.0 Lite, Nova Premier) combinan benchmarks automatizados, red-teaming por expertos externos, y estudios de uplift con participantes humanos.

---

## Las 5 Preguntas de Análisis

### Q1: ¿Menciona evaluación en idiomas distintos del inglés?

**Respuesta: No**

El documento del framework no contiene ninguna mención a idiomas no ingleses, evaluación multilingüe, ni cobertura lingüística de las capacidades peligrosas. Los reportes de evaluación aplicados (Nova 2.0 Lite, arXiv:2601.19134; Nova Premier, arXiv:2507.06260) tampoco contienen ninguna referencia a evaluación en idiomas distintos del inglés. La búsqueda exhaustiva de términos como "language", "multilingual", "non-English", "Spanish", "Portuguese" en el texto completo y en los documentos de aplicación no devuelve resultados relevantes.

**Cita:** No se encontró mención. El framework describe las evaluaciones sin especificar ninguna dimensión lingüística.

---

### Q2: ¿Sus benchmarks de capacidades peligrosas existen o se evalúan en español/portugués?

**Respuesta: No**

Los benchmarks utilizados en las evaluaciones del FMSF son:

- **CBRN:** WMDP, ProtocolQA, BioLP-Bench, VCT; estudios de uplift con ~800 participantes.
- **Cyber:** CyberMetric, SECURE-CWET, CTIBench, CyBench (CTF), entorno Hack The Box.
- **AI R&D:** RE-Bench (tareas de código intensivo), evaluación de agentes autónomos, revisión externa por METR.

Ninguno de estos benchmarks se menciona con variantes en español o portugués. El red-teaming externo para CBRN (conducido por Nemesys Insights) utilizó "120 uplift indicator prompts—60 in synthetic biology and 60 in microbiology/delivery systems" sin especificar idioma, pero el contexto implica inglés exclusivamente.

**Cita (sección CBRN, evaluación Nova Premier):** *"Nemesys Insights conducted evaluation using 120 uplift indicator prompts—60 in synthetic biology and 60 in microbiology/delivery systems"* — sin especificación de idioma; los tres expertos evaluadores (blind scoring, rubric 0–10) no se identifican con diversidad lingüística.

---

### Q3: ¿El red-teaming independiente/externo especifica múltiples idiomas?

**Respuesta: No**

El framework describe el red-teaming externo como un proceso en el que Amazon trabaja con "specialized vendors and in-house experts" y "specialized firms and academics" para evaluar riesgos que requieren expertise de dominio. Las evaluaciones de Nova Premier incluyen red-teaming externo por Nemesys Insights (CBRN) y equipos internos de ciberseguridad de Amazon (Cyber). Las evaluaciones de Nova 2.0 Lite incluyeron revisión externa de METR para AI R&D.

En ningún caso se especifican idiomas para el proceso de red-teaming. El análisis comparativo de METR ("Common Elements of Frontier AI Safety Policies") y la evaluación académica (arXiv:2512.01166v3) confirman que Amazon obtuvo puntajes bajos en métricas de red-teaming sistemático: "Internal open-ended red teaming (70%) – 10%" y "Third-party open-ended red teaming (30%) – 10%", indicando mínima documentación de compromisos de red-teaming sistemático.

**Cita:** No se encontró mención a idiomas en el red-teaming. El documento solo indica que se trabaja con *"specialized vendors and in-house experts to evaluate risks that require domain expertise"* — sin especificación lingüística o geográfica.

---

### Q4: ¿Menciona Global South, LATAM, o países en desarrollo?

**Respuesta: No**

El framework no contiene ninguna referencia a Global South, América Latina (LATAM), países en desarrollo, mercados emergentes, ni a consideraciones geográficas de ningún tipo. Los documentos de aplicación del framework (evaluaciones de Nova 2.0 Lite y Nova Premier) tampoco contienen estas referencias. Los análisis comparativos académicos del framework (arXiv:2512.01166v3, METR common elements) confirman la ausencia total de estas consideraciones.

El único foco geográfico implícito del framework es infraestructura cloud de AWS (sistemas EC2 Nitro, KMS, GuardDuty), lo que sitúa el marco operativamente en contextos de alta infraestructura tecnológica.

**Cita:** No se encontró mención. Los análisis independientes confirman que *"The framework focuses exclusively on technical security infrastructure, threat modeling, and English-language safety measures. There is no evidence [...] that Amazon addresses linguistic diversity or geographic considerations in frontier model risk assessment."*

---

### Q5: ¿Sus umbrales de riesgo consideran contextos de baja infraestructura?

**Respuesta: No**

Los Critical Capability Thresholds del FMSF están definidos en términos de "uplift" sobre recursos existentes: la capacidad de un modelo de proporcionar instrucciones expertas e interactivas que superen lo disponible públicamente para actores no expertos. El umbral de CBRN se define como: capacidad de proporcionar instrucción experta e interactiva que permita a un no-experto "reliably produce and deploy a CBRN weapon" con uplift material sobre herramientas existentes.

Este concepto de "uplift sobre recursos existentes" no se diferencia por región, infraestructura disponible, o contexto socioeconómico. No existe ningún umbral diferenciado para contextos donde la infraestructura de defensa, respuesta a incidentes, o instituciones regulatorias son más débiles (como en países del Sur Global).

**Cita:** No se encontró mención a diferenciación por infraestructura. El framework define el umbral como: *"AI at this level will be capable of providing expert-level, interactive instruction that provides material uplift (beyond other publicly available research or tools) that would enable a non-subject matter expert to reliably produce and deploy a CBRN weapon."* — sin distinción por contexto regional o de infraestructura.

---

## Párrafo de Diferencias y Observaciones

El Amazon FMSF es un documento técnicamente sólido en su dominio declarado: establece umbrales cuantificables para tres riesgos de alta consecuencia (CBRN, Cyber, AI R&D), integra evaluaciones externas con metodología de uplift, y vincula las evaluaciones con gobernanza corporativa de alto nivel. Sin embargo, presenta brechas sistemáticas en cinco dimensiones de equidad global:

**1. Monolingüismo total.** El framework y todas sus evaluaciones aplicadas operan exclusivamente en inglés. Ningún benchmark, ningún estudio de uplift, ningún ejercicio de red-teaming especifica cobertura en otros idiomas. Esto es especialmente relevante dado que Amazon Nova se despliega globalmente a través de AWS Bedrock.

**2. Benchmarks no transferibles.** Los benchmarks de capacidades peligrosas (WMDP, BioLP-Bench, CyBench, RE-Bench) son de origen anglosajón y no tienen versiones validadas en español, portugués, árabe, hindi, ni otras lenguas de alta densidad de usuarios de AWS.

**3. Red-teaming sin diversidad lingüística ni geográfica.** Los vendedores externos identificados (Nemesys Insights, METR) son organizaciones anglófonas de EEUU. No hay evidencia de red-teamers en contextos de LATAM, África, o Asia del Sur.

**4. Ausencia del Sur Global.** El framework no nombra ni considera a países o regiones donde las capacidades de respuesta institucional ante riesgos CBRN o cibernéticos son significativamente más débiles. Un modelo que no supera el umbral de uplift en EEUU podría representar un riesgo mayor en países con menor infraestructura de defensa.

**5. Umbrales universales sin contextualización.** Los Critical Capability Thresholds son binarios y universales: un modelo pasa o no pasa el umbral sin distinción de deployment context. Esto contrasta con enfoques que consideran el contexto de implementación (quién usa el modelo, en qué país, con qué infraestructura de mitigación disponible).

En síntesis, el FMSF de Amazon es representativo de la tendencia dominante en los frameworks frontier: sólido en técnica de mitigación para riesgos catastróficos en contextos occidentales de alta infraestructura, pero con ausencia sistemática de perspectiva global en idioma, geografía y contexto institucional.

---

## Fuentes Consultadas

- **Documento oficial:** https://assets.amazon.science/a7/7c/8bdade5c4eda9168f3dee6434fff/pc-amazon-frontier-model-safety-framework-2-7-final-2-9.pdf
- **Página Amazon Science:** https://www.amazon.science/publications/amazons-frontier-model-safety-framework
- **Evaluación Nova Premier (arXiv):** https://arxiv.org/html/2507.06260
- **Evaluación Nova 2.0 Lite (arXiv):** https://arxiv.org/html/2601.19134
- **Análisis comparativo de frameworks (arXiv):** https://arxiv.org/html/2512.01166v3
- **METR Common Elements:** https://metr.org/common-elements
- **Enkrypt AI overview:** https://www.enkryptai.com/blog/frontier-safety-frameworks-comprehensive-overview
