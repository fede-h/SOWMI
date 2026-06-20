# Google DeepMind — Frontier Safety Framework v3.0 (2025)

**Versión:** 3.0
**Fecha de publicación:** 22 de septiembre de 2025
**URL oficial:** https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/strengthening-our-frontier-safety-framework/frontier-safety-framework_3.pdf
**Blog de anuncio:** https://deepmind.google/blog/strengthening-our-frontier-safety-framework/

---

## Resumen estructural del documento

El FSF v3.0 es un documento de 16 páginas organizado en 5 secciones:
- **Sección 1** – Framework: Scope, CCLs, Risk Assessment Process, Mitigations, Risk Acceptance Criteria
- **Sección 2** – Misuse: CBRN, Cyber, Harmful Manipulation CCLs
- **Sección 3** – Machine Learning R&D CCLs
- **Sección 4** – Misalignment (Exploratory Approach)
- **Sección 5** – Updates and Disclosures

---

## Análisis de las 5 Preguntas

---

### Q1. ¿Menciona evaluación en idiomas distintos del inglés?

**Respuesta: Parcial**

El documento menciona "multilingüidad" como una de las áreas de evaluación de capacidades generales del modelo, pero únicamente en un sentido técnico superficial, sin especificar qué idiomas, con qué protocolos o bajo qué estándar de cobertura. La mención aparece en un listado con otras capacidades generales:

> "These evaluations include a broad range of areas, including general capability evaluations, model behavior, efficiency, coding capabilities, **multilinguality**, or reasoning." (Sección 1.3, p. 5)

No hay ninguna otra mención a evaluación multilingüe en el resto del documento. No se especifica qué se evalúa en materia multilingüe, bajo qué metodología, con qué umbrales o con qué frecuencia. La mención es de pasada y no se desarrolla.

---

### Q2. ¿Sus benchmarks de capacidades peligrosas (CBRN, cyber, autonomía, ML R&D) existen o se evalúan en español/portugués?

**Respuesta: No**

El documento no menciona en ningún momento el español, el portugués ni ningún otro idioma específico en el contexto de sus benchmarks de capacidades peligrosas. Las definiciones de CCLs para CBRN, Cyber, Harmful Manipulation y ML R&D (Secciones 2.2 y 3.2) están formuladas en términos de capacidad de "uplift" o daño esperado, sin ninguna referencia a la dimensión lingüística de las evaluaciones.

Por ejemplo, el CBRN CCL se define como:

> "**CBRN uplift level 1:** Provides low to medium resourced actors uplift in reference scenarios resulting in additional expected harm at severe scale." (Tabla 2.2.1.a, p. 10)

El Cyber CCL:

> "**Cyber uplift level 1:** Provides sufficient uplift with high impact cyber attacks for additional expected harm at severe scale." (Tabla 2.2.2.a, p. 10)

Ninguna tabla de CCL menciona dimensiones lingüísticas. No se encontró mención alguna a evaluaciones en español o portugués.

---

### Q3. ¿El red-teaming independiente/externo especifica múltiples idiomas?

**Respuesta: No**

El documento menciona el red-teaming como parte del proceso de evaluación de mitigaciones, tanto para misuse CCLs (Sección 2.1.2) como para ML R&D CCLs (Sección 3.1.2), pero en ningún caso especifica idiomas, regiones geográficas ni diversidad lingüística de los equipos de red-teaming.

La referencia al red-teaming en la Sección 2.1.2 (p. 8) es:

> "Assessing the robustness of these mitigations against the risk posed through testing (e.g. automated evaluations, **red teaming**) and threat modeling research."

Y en la Sección 3.1.2 (p. 12):

> "Assessing the robustness of these mitigations against the risk posed in both internal and external deployment through testing (e.g. automated evaluations, **red teaming**) and threat modeling research."

El documento menciona la posibilidad de involucrar "external actors, including governments" (Sección 1.3, p. 5):

> "Where appropriate, we may engage relevant and appropriate external actors, including governments, to inform our responsible development and deployment practices."

No se especifica diversidad lingüística, geográfica ni inclusión de equipos de red-teaming en idiomas distintos del inglés.

---

### Q4. ¿Menciona Global South, LATAM, o países en desarrollo?

**Respuesta: No**

El documento no contiene ninguna mención a "Global South", "Latin America", "LATAM", "developing countries", "países en desarrollo", "economías emergentes" ni ningún término equivalente. La única dimensión geográfica del documento es una referencia general al bienestar global como objetivo:

> "The safety and security of frontier AI models is a **global public good**." (Overview, p. 2)

Esta afirmación es declarativa y no se traduce en ningún mecanismo, benchmark, criterio de evaluación o consideración operativa que tome en cuenta contextos de países no angloparlantes, del Sur Global o de América Latina. No se encontró mención alguna.

---

### Q5. ¿Sus umbrales (Critical Capability Levels) consideran contextos de baja infraestructura?

**Respuesta: No**

Los CCLs definidos en el FSF v3.0 están formulados en términos de capacidad de "uplift" para actores con diferentes niveles de recursos (bajo/mediano/alto), pero esta distinción está orientada a calibrar la amenaza del adversario, no a considerar contextos de despliegue en infraestructuras débiles. El documento no menciona en ningún momento escenarios de baja infraestructura tecnológica, conectividad limitada, ausencia de sistemas regulatorios maduros u otros rasgos característicos del Sur Global.

La única referencia a "recursos" del actor amenazante aparece en CBRN CCL:

> "**CBRN uplift level 1:** Provides **low to medium resourced actors** uplift in reference scenarios resulting in additional expected harm at severe scale." (Tabla 2.2.1.a, p. 10)

Esta distinción ("low to medium resourced actors") se refiere a la capacidad del actor malicioso para ejecutar un ataque CBRN, no al contexto de despliegue del modelo en entornos con baja infraestructura digital. Los CCLs de ML R&D también mencionan recursos computacionales:

> "ML R&D automation level 1: Can fully automate the work of any team of researchers at Google focused on improving AI capabilities, with approximately comparable **all-inclusive costs**." (Tabla 3.2.1.a, p. 14)

Aquí "all-inclusive costs" hace referencia a la equiparación de costos con los de Google, no a contextos de baja infraestructura. No se encontró mención alguna a estos contextos como variable en la definición de CCLs.

---

## Diferencias clave respecto a otros frameworks de safety

El FSF v3.0 de Google DeepMind se distingue por su **foco técnico-interno** y su **omisión casi total de contexto geográfico y lingüístico diverso**. A diferencia de lo que podría esperarse de una empresa con presencia global como Google, el documento no traduce su declaración de que la seguridad del AI es "un bien público global" en ningún mecanismo concreto de inclusión regional o lingüística. Los benchmarks de evaluación de capacidades peligrosas (CBRN, Cyber, ML R&D) están formulados en abstracto, sin referencia a las diferencias en cómo estas capacidades podrían manifestarse o ser explotadas en contextos de baja infraestructura o en idiomas distintos del inglés. El único guiño a la multilingüidad aparece en una lista de capacidades generales del modelo (Sección 1.3), pero sin vinculación a los protocolos de seguridad. Los CCLs utilizan la variable "nivel de recursos del actor amenazante" exclusivamente para calibrar el riesgo de exfiltración y la robustez de las mitigaciones, no para incorporar heterogeneidad geográfica en la evaluación de riesgos de despliegue. El red-teaming, tanto interno como externo, no tiene ningún requerimiento de diversidad lingüística o geográfica explicitado. En comparación con frameworks que sí mencionan equipos de evaluadores diversos o contextos de uso global diferenciado, el FSF v3.0 presenta una perspectiva centralizada, orientada a grandes actores estatales y corporativos, y silenciosa respecto al Sur Global, América Latina y los contextos de uso fuera del mundo angloparlante.
