# OpenAI — Preparedness Framework v2

**Versión:** Version 2  
**Fecha de última actualización:** 15 de abril de 2025  
**URL oficial:** https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf  
**Página de anuncio:** https://openai.com/index/updating-our-preparedness-framework/  
**Extensión:** 22 páginas  

---

## Las 5 Preguntas de Análisis

### Q1: ¿Menciona evaluación en idiomas distintos del inglés?

**Respuesta: No**

El documento no contiene ninguna mención a idiomas no ingleses, evaluación multilingüe, ni cobertura lingüística de las capacidades peligrosas. La búsqueda exhaustiva de términos como "language", "multilingual", "non-English", "Spanish", "Portuguese" en el texto completo del PDF devuelve cero resultados relevantes.

**Cita:** No se encontró mención. El documento describe evaluaciones de capacidades sin especificar ninguna dimensión lingüística.

---

### Q2: ¿Sus benchmarks de capacidades peligrosas (CBRN, cyber, autonomía) existen o se evalúan en español/portugués?

**Respuesta: No**

Los benchmarks descritos para las tres Tracked Categories (Biological and Chemical, Cybersecurity, AI Self-Improvement) no especifican idiomas de evaluación. La única descripción concreta de un benchmark de bio indica:

> "Our evaluations test acquiring critical and sensitive information across the five stages of the biological threat creation process: Ideation, Acquisition, Magnification, Formulation, and Release." (Sección 3.1, recuadro ilustrativo)

No se menciona el español, portugués, ni ningún otro idioma no inglés para ninguno de los benchmarks. El marco asume implícitamente una operación en inglés sin explicitarlo.

---

### Q3: ¿El red-teaming independiente/externo especifica que debe hacerse en múltiples idiomas?

**Respuesta: No**

El documento menciona red-teaming externo e independiente en varias secciones, pero en ningún momento especifica requisitos lingüísticos. Las referencias relevantes son:

> "These may include a wide range of evidence gathering activities, such as human expert red-teaming, expert consultations, resource-intensive third party evaluations (e.g., bio wet lab studies, assessments by independent third party evaluators), and any other activity requested by SAG." (Sección 3.1)

> "Third-party stress testing of safeguards: If we deem that a deployment warrants third party stress testing of safeguards and if high quality third-party testing is available, we will work with third parties to evaluate safeguards." (Sección 5.2)

> "Automated and expert redteaming (identifying success per resources)" (Apéndice C.1, tabla de salvaguardas)

Ninguna de estas menciones incluye requisito de idioma, diversidad lingüística, ni representación geográfica de los red-teamers.

---

### Q4: ¿Menciona Global South, LATAM, o países en desarrollo?

**Respuesta: No**

La búsqueda de términos como "Global South", "Latin America", "LATAM", "developing countries", "low-income", "Africa", "Asia", "emerging economies" y "region" en el texto completo del documento no produce ningún resultado relevante. Las únicas referencias geográficas en todo el documento son a:

- Los Estados Unidos y su gobierno ("the U.S. government and its partners", Sección 2.1)
- California y Florida (mención a legislación estatal de proveniencia de contenido de IA, Sección 2.3 — nota sobre Persuasion)
- El Frontier Model Forum (industria, sin especificación geográfica)

**Cita:** "This process draws on our own internal research and signals, and where appropriate incorporates feedback from academic researchers, independent domain experts, industry bodies such as the Frontier Model Forum, and the U.S. government and its partners." (Sección 2.1)

No se encontró mención al Global South, LATAM ni países en desarrollo.

---

### Q5: ¿Sus umbrales de riesgo consideran contextos de baja infraestructura (sin GPU, sin equipo de seguridad local)?

**Respuesta: No**

El documento define umbrales de riesgo (High y Critical) y los criterios para clasificar riesgos como "Tracked Categories", pero en ningún momento diferencia por contexto de infraestructura del actor amenazante o del usuario. La definición de "net new risk" hace referencia a herramientas disponibles en 2021, pero no a contextos de bajo recurso:

> "Net new: The outcome cannot currently be realized as described (including at that scale, by that threat actor, or for that cost) with existing tools and resources (e.g., available as of 2021) but without access to frontier AI." (Sección 2.1, criterio 4)

La noción de "novice actor" en el umbral de bio incluye solo "anyone with a basic relevant technical background" (Tabla 1), sin considerar si el actor tiene o no infraestructura computacional local, equipo de seguridad, o acceso a GPU. El marco asume implícitamente actores con acceso a la API de OpenAI, sin contemplar asimetrías de infraestructura entre regiones.

No se encontró mención a contextos de baja infraestructura, países sin GPU, ni ausencia de equipos de seguridad locales.

---

## Observaciones Adicionales Relevantes

### Lo que el documento SÍ cubre bien

1. **Estructura de umbrales clara:** Distingue entre capacidad "High" (amplifica vectores existentes de daño severo) y "Critical" (introduce vectores completamente nuevos). Esto es operacionalmente preciso.

2. **Criterio de "marginal risk":** El Sección 4.3 reconoce que si otro desarrollador lanza un modelo con capacidad High/Critical sin salvaguardas, OpenAI podría ajustar sus propias salvaguardas a la baja, lo que plantea un problema de incentivos perversos en seguridad global.

3. **Transparencia parcial:** Compromete publicar resultados de evaluaciones y decisiones de despliegue para modelos frontier, incluyendo información sobre salvaguardas cuando se supera el umbral High.

4. **Gobernanza interna:** El Safety Advisory Group (SAG) tiene poder de recomendación pero no de veto final — OpenAI Leadership tiene la decisión final, lo que limita la independencia del proceso.

### Brechas críticas desde una perspectiva de AI Safety global

1. **Anglocentrismo implícito:** Todo el marco asume que los actores amenazantes y usuarios operan en inglés. No evalúa si un modelo es igualmente capaz de proveer uplift bioweapon o cyberattack en español, árabe, mandarín, etc. Esto es una brecha de cobertura real.

2. **Ausencia de perspectiva geopolítica:** El único actor estatal mencionado es el gobierno de EE.UU. No hay consideración de cómo el framework aplica a jurisdicciones sin regulación equivalente, ni a actores en países donde OpenAI opera pero sin controles locales.

3. **Supuestos de infraestructura occidentales:** Los umbrales de "marginal risk" y "novice actor" están calibrados para contextos con acceso fluido a internet, computación, y laboratorios. No consideran el efecto diferencial del uplift de IA en regiones donde la barrera de entrada a capacidades peligrosas es distinta.

4. **Red-teaming no representativo:** Los "independent domain experts" y "third-party evaluators" no tienen requisito de diversidad geográfica, lingüística ni cultural. El riesgo de sesgo de cobertura es alto.

5. **Categorías de Research no definidas operacionalmente:** Persuasión, que se menciona como excluida del framework pero relevante globalmente (especialmente para desinformación en LATAM y Africa), queda fuera sin justificación robusta.

---

*Análisis realizado el 2026-06-19. Fuente primaria: PDF oficial de OpenAI CDN, versión del 15 de abril de 2025.*
