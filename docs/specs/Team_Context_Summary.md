# Contexto del proyecto — Resumen para el equipo

## Actualización — Sábado 20 de junio de 2026, 14:05

### Corrección sobre el entregable

Al principio asumimos que solo había que entregar un PDF. **No es así.** El hackathon pide dos cosas:

1. **Un proyecto funcional** — una herramienta, evaluación, análisis de política o contribución de investigación. → Nuestra evaluación de modelos + el dataset de prompts en español ES esto.
2. **Un research report en PDF** — armado con el template oficial.

**Lo que se juzga es el report.** Textual del template: *"Your project will be judged on the quality of this written report."*

Datos clave del template:
- **Largo recomendado: ~4 páginas** (sin contar referencias ni apéndice). Distribución sugerida: Introducción + Related Work 1p, Methods + Results 2.5p, Discussion 0.5p.
- Estructura fija: Abstract (150–250 palabras) → Introduction (con lista de contribuciones) → Related Work → Methods → Results (con al menos 1 figura) → Discussion + Limitations + Future Work → Conclusion → Code & Data → References → **Appendix (acá van los prompts y resultados extendidos)** → LLM Usage Statement.
- **Implicancia importante:** los 6 pasos completos de Vertical 1 no entran enteros en 4 páginas. El cuerpo resume; los prompts, métricas detalladas y resultados extendidos van al Appendix.

### Cómo se juzga (rubric oficial — ver "Apart Sprint Evaluation Rubric.txt")

Se puntúa en 3 dimensiones independientes, de 1 a 5:
1. **Impact Potential & Innovation** — ¿importaría para AI safety si funciona? ¿es genuinamente nuevo o replica algo reciente? (para 4–5 exige novedad real, no replicación)
2. **Execution Quality** — metodología sólida, resultados interpretables, validación convincente, limitaciones reconocidas.
3. **Presentation & Clarity** — claro, bien estructurado, sin verborragia.

Reglas que nos afectan directo: **"quality over quantity"** (4 páginas enfocadas > 10 ruidosas); *experimentos dispersos que no cierran restan en Execution*; *verborragia que tapa lo importante resta en Presentation*. Nivel 3 = trabajo sólido de fin de semana; Nivel 5 = top 5–10%.

### Mapeo del esqueleto de entregable (Vertical 1) a las dimensiones experimentales

Nuestro documento conjunto *"Vertical 1 — Data curation in spanish"* es el esqueleto del entregable. Sus 6 pasos se mapean así a las dimensiones de prueba y métricas:

| Paso de Vertical 1 | Métrica | Dimensión experimental |
|---|---|---|
| Paso 1 — Fertilidad de tokens (cobertura de corpus) | SCC | Representación del español en pretraining |
| Paso 2 — Cobertura y puntos ciegos dialectales | RCS | Variantes regionales (rioplatense, etc.) |
| Paso 3 — Filtrado semántico / sobre-bloqueo | SFV, FRR | Over-refusal |
| Paso 4 — Probe de conocimiento peligroso | Δ ASR | Jailbreak + code-switching |
| Paso 5 — Toxicidad, sesgos y estereotipos locales | BSS | Toxicidad / sesgo |
| Paso 6 — Calidad factual y alucinación | FES, FCR | Alucinación + calibración |

---

## Qué estamos haciendo y por qué

### El problema central

Los modelos de IA como GPT, Claude o Llama son evaluados casi exclusivamente en inglés. Cuando una empresa, hospital o gobierno en América Latina los adopta, asume que si el modelo es "seguro" en inglés, también lo es en español. Esa suposición es falsa.

Hay evidencia creciente de que los modelos fallan más en español: aceptan pedidos que rechazan en inglés, alucian más sobre temas locales, y pueden ser manipulados más fácilmente con jerga regional o code-switching. El paper M-ALERT (2024) ya documentó esta inestabilidad entre idiomas europeos. El trabajo de Marx & Dunaiski (2026) mostró que las tasas de jailbreak suben de 59.8% a 75.8% cuando se usan idiomas distintos al inglés.

**Nadie lo midió sistemáticamente para español latinoamericano.**

---

### Qué vamos a aportar

El equipo está construyendo el **Spanish Model Safety Maturity Framework** (nombre tentativo), que extiende el OWMI (ya desarrollado por Mauricio) para evaluar seguridad en español específicamente.

El framework propone que una organización NO debería considerar un modelo seguro si esa seguridad no fue validada empíricamente en el idioma donde lo va a usar. La frase guía del paper es:

> *"Safe in English ≠ Safe in Spanish"*

El aporte tiene tres partes:
1. Una **matriz de madurez** adaptada al español (3 verticales, scoring L1/L2/L3)
2. Una **taxonomía de riesgos** específica para modelos usados en español
3. Un **protocolo de evaluación** con prompts reales en español y resultados sobre modelos concretos

---

### Las 3 verticales del framework (qué evalúa cada una)

**Vertical 1 — Spanish Upstream Data Curation (35% del score)**
¿El modelo fue entrenado con datos en español de calidad y con filtros de seguridad en español? ¿Sabe algo peligroso en español que no debería saber? ¿Alucina sobre temas locales de salud, derecho o finanzas?

**Vertical 2 — Spanish Weight Provenance & Robustness (25% del score)**
¿Podemos verificar que el modelo que usa la organización es el que fue evaluado? ¿Si alguien le hace fine-tuning en español, pierde su seguridad? ¿Tiene watermarking que sobreviva adaptaciones locales?

**Vertical 3 — Spanish Tiered Release & Testing (40% del score)**
¿El modelo fue testeado adversarialmente en español antes de ser usado? ¿Se probaron jailbreaks en español, variantes regionales, spanglish, prompt injection en documentos en español?

---

### Los experimentos concretos

Los experimentos son todos en español. Se van a correr en 2-4 modelos (al menos uno open-weight, al menos uno cerrado). Los prompts cubren:

**Dimensión 1 — Jailbreaks y contenido dañino (el grueso)**
- ¿El modelo rechaza pedidos dañinos en español?
- ¿Los rechaza igual en español rioplatense que en español neutro?
- ¿Code-switching (mezcla español-inglés) lo confunde?
- ¿Multi-turn funciona para bajar las defensas?

**Dimensión 2 — Over-refusal**
- ¿El modelo rechaza cosas que NO debería rechazar? (Una consulta médica legítima, una pregunta sobre historia política argentina, etc.)
- Esto importa porque un modelo que rechaza todo es inútil, no seguro.

**Dimensión 3 — Alucinaciones en dominios locales**
- ¿El modelo inventa datos sobre sistemas de salud argentino/latinoamericano?
- ¿Cita legislación que no existe?
- ¿Confunde instituciones regionales?

**Dimensión 4 — Prompt injection**
- Si le pasás un documento en español con instrucciones maliciosas embebidas, ¿el modelo las sigue?

---

### Benchmarks existentes que debemos citar y diferenciarnos

| Benchmark | Qué hace | Por qué nos diferenciamos |
|---|---|---|
| LinguaSafe | Seguridad en 12 idiomas, 45.000 instancias | No incluye español latinoamericano; no tiene scoring organizacional |
| M-ALERT | Seguridad en 5 idiomas europeos | No incluye español de LATAM; no tiene variantes dialectales |
| "Spanish Is Not Just One" | Dialecto implícito de modelos en 7 variantes | No mide seguridad; mide preferencia dialectal lingüística |
| MultiJail | Jailbreaks en 9 idiomas | No tiene español latinoamericano ni marco organizacional |
| TELEIA | Competencia gramatical en español | No mide seguridad; mide capacidad lingüística |

**Nuestra diferencia:** El único framework que combina evaluación de seguridad + variantes dialectales latinoamericanas + scoring organizacional (L1/L2/L3) + extensión del OWMI.

---

### Estado actual del trabajo

| Componente | Estado |
|---|---|
| OWMI base | ✅ Completo |
| Revisión de literatura multilingüe | ✅ Completo |
| Esqueleto del framework | ✅ Completo |
| Análisis de Frontier Safety Frameworks | ⏳ Pendiente |
| Dataset de prompts en español | ⏳ Pendiente |
| Experimentos en modelos | ⏳ Pendiente |
| Scorecard de ejemplo | ✅ Ver Sample_Scorecard.md |
| Paper unificado | ⏳ Pendiente |
