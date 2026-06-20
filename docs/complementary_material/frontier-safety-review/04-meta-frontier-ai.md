# Meta — Advanced AI Scaling Framework (Version 2)

**Titulo original:** Advanced AI Scaling Framework (Version 2)  
**Anteriormente titulado:** Frontier AI Framework (versión inicial: 3 de febrero de 2025)  
**Version actual:** v2.0 (publicada: 7 de abril de 2026)  
**URL oficial:** https://ai.meta.com/static-resource/Meta_Advanced-AI-Scaling-Framework-v2/  
**URL blog de anuncio (v1):** https://about.fb.com/news/2025/02/meta-approach-frontier-ai/

---

## Contexto del documento

El documento tiene dos versiones registradas en el Appendix II (Change log):

- **February 3, 2025 (Frontier AI Framework):** versión inicial.
- **April 7, 2026 (Advanced AI Scaling Framework v2.0):** renombrado, con thresholds revisados, adición de Loss of Control como dominio, y nuevos requisitos de transparencia.

El framework cubre riesgos catastróficos en tres dominios: Chemical & Biological, Cybersecurity, y Loss of Control.

---

## Las 5 Preguntas

### Q1: ¿Menciona evaluación en idiomas distintos del inglés?

**Respuesta: No**

El documento no contiene ninguna mención a evaluaciones en idiomas distintos del inglés. Las evaluaciones descritas (CTF challenges, BioTIER, MASK, Agent Misalignment, CyberSOCEval, AutoPatchBench, Cybench) son todas en inglés y no se especifica ninguna consideración lingüística. La sección 2.1.2 describe el proceso de evaluación como "a combination of automated and human evaluations, as well as red teaming and uplift studies" sin referencia a idiomas. La sección 4.2 detalla extensamente los benchmarks de cybersecurity y CBRN sin mencionar idiomas alternativos.

**Cita:** No se encontró mención.

---

### Q2: ¿Sus benchmarks de capacidades peligrosas (cyber, CBRN) existen o se evalúan en español/portugués?

**Respuesta: No**

Los benchmarks nombrados explícitamente en el documento son:

- **Cybersecurity:** CTF (Capture the Flag) challenges, Cybench, AutoPatchBench, CyberSOCEval, LlamaFirewall
- **CBRN:** BioTIER refusal evaluation

Ninguno de estos benchmarks es descrito con componentes en español, portugués u otro idioma que no sea inglés. La sección 4.2.1 (Cybersecurity) define los umbrales cuantitativos ("< 75% pass@10 success on all categories of simple capture the flag (CTF) challenges") sin ninguna dimensión lingüística. La sección 4.2.2 (Chemical and Biological Risks) menciona el BioTIER con criterios de rechazo ("at least 80% refusal or safe responses") igualmente sin consideración de idioma.

**Cita:** No se encontró mención.

---

### Q3: ¿El red-teaming independiente/externo especifica múltiples idiomas?

**Respuesta: No**

El documento menciona red-teaming y expertos externos en varias secciones, pero nunca especifica que deban operar en múltiples idiomas. Las referencias relevantes son:

- Sección 2.1.1: *"Host workshops with experts, including external subject matter experts where relevant, to identify new catastrophic outcomes and/or threat scenarios."*
- Sección 2.1.2: *"For both Cyber and Chemical and Biological risks, we conduct red teaming exercises once a model achieves certain levels of performance in capabilities relevant to these domains, involving external experts when appropriate."*
- Sección 3.2: *"We run threat modeling exercises both internally and with external experts with relevant domain expertise, where appropriate."*

La especificación de "domain expertise" se refiere a conocimiento técnico (biología, ciberseguridad), no a cobertura lingüística o geográfica.

**Cita:** No se encontró mención a idiomas en el red-teaming.

---

### Q4: ¿Menciona Global South, LATAM, o países en desarrollo?

**Respuesta: No**

En las 44 páginas del documento (incluyendo introducción, 5 secciones, apéndices y change log), no aparece ninguna mención a:

- Global South
- Latin America / LATAM / América Latina
- Developing countries / países en desarrollo
- Regiones geográficas específicas fuera del contexto de "geogating" como medida de mitigación (mencionado solo en el blog de anuncio de la v1, no en el documento técnico)
- Africa, Asia del Sur u otras regiones de referencia habitual en AI governance

El único término con dimensión geopolítica es la referencia a "state and non-state actors" (Sección 1.1) y "engagements with governments" (Sección 3.2), ambos sin especificación regional.

**Cita:** No se encontró mención.

---

### Q5: ¿Sus umbrales de riesgo consideran contextos de baja infraestructura?

**Respuesta: No**

Los umbrales de riesgo (Sección 3.3, Tabla 1) se definen en términos de la contribución sustancial del modelo a escenarios de amenaza catastróficos, con tres niveles: Critical, High, y Moderate or lower. Los criterios de escalación son puramente técnicos (rendimiento en benchmarks, capacidades de uplift). 

La sección 4.2 sí menciona barreras al uso indebido: *"We may take into account monetary costs as well as the ability to overcome other barriers to misuse relevant to our threat scenarios such as access to compute, restricted materials, or lab facilities."* Sin embargo, esto se plantea como variable para el atacante en escenarios de amenaza, no como un factor diferencial que ajuste umbrales según el contexto de infraestructura del país o región donde se despliega el modelo.

No hay ninguna consideración sobre cómo los mismos umbrales de riesgo podrían operar diferente en contextos con menor infraestructura de salud pública, respuesta a incidentes, o capacidad de ciberseguridad defensiva.

**Cita:** No se encontró mención.

---

## Párrafo de diferencias con una perspectiva de AI Safety global

El Advanced AI Scaling Framework de Meta (v2, abril 2026) es un documento técnicamente riguroso para su ámbito declarado: prevenir resultados catastróficos en tres dominios concretos (Cybersecurity, CBRN, Loss of Control) con thresholds operacionalizables y benchmarks cuantitativos. Sin embargo, el framework presenta una brecha sistemática respecto a una perspectiva de AI Safety verdaderamente global. Primero, la totalidad del ecosistema de evaluación —benchmarks CTF, BioTIER, MASK, CyberSOCEval— está construida en inglés, ignorando que modelos como Llama se despliegan masivamente en contextos hispanohablantes, lusófonos y de otras lenguas donde los vectores de ataque y uplift pueden diferir. Segundo, el framework no reconoce que el mismo umbral de riesgo "moderate or lower" puede implicar consecuencias radicalmente distintas en un país con sistemas de salud pública robustos versus uno con infraestructura crítica frágil: un ataque cibernético que causa "significant financial loss" a una empresa de Fortune 500 puede representar una amenaza existencial para infraestructura hospitalaria en el Sur Global. Tercero, la ausencia total de mención a LATAM, Africa, Asia del Sur, o países en desarrollo en un framework publicado por la empresa que opera WhatsApp —plataforma dominante en Brasil, México, India y Nigeria— es una omisión estructural que indica que el diseño de seguridad está centrado en proteger usuarios y sistemas del Norte Global. El framework es una contribución valiosa a la gobernanza de AI frontier, pero su aplicabilidad universal está implícitamente asumida sin evidencia de que sus mecanismos sean robustos fuera del contexto tecnológico angloparlante en el que fue diseñado.
