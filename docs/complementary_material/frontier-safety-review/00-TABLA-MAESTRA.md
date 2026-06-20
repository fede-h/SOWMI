# Frontier Safety Frameworks — Auditoría multilingüe / Sur Global

Evidencia directa de los 12 frameworks listados en el *International AI Safety Report 2026*.
Revisión por framework en los archivos `01`–`12` de esta carpeta.

**Preguntas:**
- **Q1** — ¿Menciona evaluación en idiomas ≠ inglés?
- **Q2** — ¿Benchmarks de capacidades peligrosas en español/portugués?
- **Q3** — ¿Red-teaming independiente exige múltiples idiomas?
- **Q4** — ¿Menciona Global South / LATAM / países en desarrollo?
- **Q5** — ¿Umbrales consideran contextos de baja infraestructura?

| # | Framework (versión) | Q1 | Q2 | Q3 | Q4 | Q5 |
|---|---------------------|----|----|----|----|----|
| 1 | Anthropic — RSP v3.3 (may 2026) | No | No | No | No | No |
| 2 | OpenAI — Preparedness Framework v2 (abr 2025) | No | No | No | No | No |
| 3 | Google DeepMind — FSF v3.0 (2025) | **Parcial** | No | No | No | No |
| 4 | Meta — Advanced AI Scaling Framework v2 (2025/26) | No | No | No | No | No |
| 5 | Microsoft — Frontier Governance Framework v1 (feb 2025) | No | No | No | No | No |
| 6 | Amazon — Frontier Model Safety Framework (feb 2025) | No | No | No | No | No |
| 7 | NVIDIA — Frontier AI Risk Assessment (ago 2025) | No | No | No | No | No |
| 8 | xAI — Risk Management Framework (ago 2025) | No | No | No | No | No |
| 9 | Cohere — Secure AI Frontier Model Framework (feb 2025) | No | No | **Parcial** | No | No |
| 10 | Magic — AGI Readiness Policy v1.0 (jul 2024) | No | No | No | No | No |
| 11 | Naver — AI Safety Framework Beta (nov 2024) | **Parcial** | No | No | No | No |
| 12 | G42 — Frontier AI Safety Framework (feb 2025) | **Parcial** | No | No | No | No |

## Citas de los "Parcial" (los únicos no-No del cuadro)

- **DeepMind Q1** — *"These evaluations include a broad range of areas, including general capability evaluations, model behavior, efficiency, coding capabilities, multilinguality, or reasoning."* (§1.3, p.5). Mención al pasar, sin protocolo ni idioma definido.
- **Cohere Q3** — *"Red teaming exercises may include independent external parties, such as NIST and Humane Intelligence."* Especifica independencia, no idiomas.
- **Naver Q1** — *"training and evaluating language models with local datasets within the proper cultural and societal context."* Solo aplica a coreano (benchmarks SQuARe, KoSBi, KoBBQ).
- **G42 Q1** — *"Models created to generate output in a specific language, such as Arabic or Hindi, may be tested in those languages."* (§2). Condicional ("may"), no obligatorio; ejemplifica árabe/hindi, nunca español/portugués.

## Veredicto sobre la hipótesis del paper

> *Ninguno de los 12 menciona evaluación en español o portugués; ninguno exige red-teaming multilingüe; ninguno considera LATAM como contexto de despliegue relevante.*

**Confirmada en su totalidad:**

1. **Español/portugués (Q2): 12/12 No.** Cero frameworks evalúan capacidades peligrosas en estos idiomas. Confirmado.
2. **Red-teaming multilingüe obligatorio (Q3): 0/12.** El único "Parcial" (Cohere) especifica *independencia*, no idiomas. Confirmado.
3. **LATAM como contexto de despliegue (Q4): 12/12 No.** Confirmado.
4. **Idiomas ≠ inglés en general (Q1): 8/12 No, 4 Parcial.** Los 4 parciales son menciones genéricas (DeepMind), o referidas a coreano/árabe/hindi (Naver, G42) — **ninguno** cubre español o portugués. La hipótesis estricta (español/portugués) se sostiene.
5. **Baja infraestructura (Q5): 12/12 No.** Los umbrales modelan al *atacante* ("moderately resourced", "state programs", expertise PhD/STEM), nunca al *contexto receptor* sin GPU ni equipo de seguridad local.

## Hallazgos transversales para sección 2 / conclusiones

- **Modelo de amenaza Norte-Global implícito.** Todos definen el riesgo por capacidad del modelo + recursos del atacante, asumiendo infraestructura defensiva occidental. Un modelo "por debajo del umbral" en EE.UU. puede ser peligroso donde no hay capacidad institucional de respuesta (argumento central para extender el OWMI).
- **Paradoja multilingüe.** Las dos empresas con más I+D multilingüe — **Cohere** (Aya, 101 idiomas) y **Naver/G42** (soberanía lingüística como bandera) — **no trasladan nada de eso a su framework de seguridad**. Evidencia fuerte: ni siquiera quienes podrían, lo hacen.
- **G42 / Naver: retórica vs. implementación.** Se presentan como del Sur Global / no-occidentales, pero su metodología replica el estándar del Norte y, donde testean en idioma local, es árabe/hindi/coreano — nunca lenguas latinoamericanas.
- **xAI:** la brecha más crítica operativamente — Grok se despliega en X a cientos de millones de hispano/lusohablantes sin ninguna evaluación en esos idiomas.
- **Madurez desigual:** Anthropic/OpenAI/DeepMind/Meta son documentos extensos y técnicos; Magic (~1 pág) y NVIDIA (15 pág, admite no desarrollar modelos frontier) son mínimos. La ausencia es uniforme **independientemente** de la madurez del documento — no es un descuido de los frameworks pobres, es un punto ciego sistémico del sector.
