# S-OWMI — MVP y estructura del trabajo

**Fecha:** 20/06/2026 (post-meet)
**Qué es esto:** el blueprint de cómo va a ir todo el trabajo, ANTES de pasarlo al template oficial. Sirve para alinear al equipo sobre la estructura y para construir el MVP primero.

---

## Decisiones del equipo (de la meet)

| Tema | Decisión |
|---|---|
| Foco | **Dirección de trabajo (a confirmar):** enfocarse en **Vertical 1** (Spanish Upstream Data Curation) y dejar V2/V3 en versión reducida o Future Work. El equipo todavía evalúa si las achica o las saca del todo. |
| Nombre | **S-OWMI** |
| Scope de modelos | Solo **open-weight / open source** |
| Audiencia | Organismos del Sur Global (gobierno, salud, fintech) que adoptan modelos open-source **por costo** (no pueden pagar APIs cerradas) |
| Variantes de español | **neutro + spanglish + variantes regionales mezcladas a la vez** (NO se compara región por región; la diversidad es parte del set "español") |
| Repo | GitHub (link en Code & Data) |

### Por qué esto cierra el problema del solapamiento V1/V3
Confirmado: al puntuar **solo V1**, el Paso 4 (jailbreak / ΔASR) ya no se cuenta dos veces, porque V3 no produce un score separado. El solapamiento solo era problema si ambas verticales puntuaban en el índice. Queda resuelto.

---

## La idea en una frase (theory of change — clave para el rubric)

> Los organismos del Sur Global adoptan modelos open-weight por costo y los ajustan con datos locales sensibles en español — pero no tienen forma de saber si el modelo es seguro en español. **S-OWMI Vertical 1 les da una forma auditable y basada en evidencia de evaluar la seguridad de curación de datos en español antes de adoptar.**

Es la respuesta a "¿a quién va dirigido y por qué importa?". Va en el Abstract, la Intro y la Discussion.

---

## PARTE A — Estructura del deliverable (mapeada al template, ~4 páginas)

### Abstract (150–250 palabras)
Problema (open-weight por costo en el GS; safety en inglés no transfiere al español) → approach (S-OWMI V1 sobre N modelos open-weight) → resultado clave (el gap inglés↔español + scorecard) → takeaway (un modelo "seguro" en inglés puede no serlo en español).

### 1. Introduction (~0.5p)
- A quién va: organismos GS que eligen open-source por dinero.
- Por qué importa: la theory of change de arriba.
- Threat model: open-weight = guardrails removibles (abliteration); español = alineación más débil (SS-Neurons indexadas al inglés).
- **Contribuciones** (lista explícita — el template las pide):
  1. S-OWMI Vertical 1: índice auditable de seguridad de curación de datos en español para modelos open-weight.
  2. Evaluación empírica de [2–4] modelos open-weight que muestra el gap de seguridad en español.
  3. Scorecard organizacional: cómo un organismo interpreta el resultado para decidir adopción.

### 2. Related Work (~0.5p)
- Multilingual safety: M-ALERT, LinguaSafe, MultiJail/Marx&Dunaiski, Yong, Yoo, Shen, Deng.
- Variantes: Spanish Is Not Just One.
- Gap que llenamos: nadie cubre español LATAM + scorecard organizacional + gobernanza open-weight juntos.
- (Detalle en Related_Work_Justifications.md.)

### 3. Methods (~1.25p)
- Modelos: [2–4 open-weight], al menos uno chico ejecutable (ej. Llama 3.1, Qwen2.5, Mistral).
- Condiciones lingüísticas: **inglés (baseline) vs español-diverso** (neutro + spanglish + regionalismos mezclados).
- Protocolo = los 6 pasos de Vertical 1 con sus métricas:
  - Paso 1 — Fertilidad de tokens → SCC
  - Paso 2 — Robustez ante variantes mezcladas → RCS
  - Paso 3 — Filtrado semántico / over-refusal → SFV, FRR
  - Paso 4 — Probe de conocimiento peligroso → ΔASR
  - Paso 5 — Toxicidad / sesgos locales → BSS
  - Paso 6 — Factualidad / alucinación → FES, FCR
- Evaluación: LLM-judge binario + revisión humana de muestra (~20%).
- Recortes (a Future Work): inyección visual (MLingualFC) y cruce NER regulatorio.
- Reproducibilidad: repo GitHub con prompts y scripts.

### 4. Results (~1.25p)
- Scorecard por modelo: nivel L1/L2/L3 por paso + score V1 global.
- Comparación inglés vs español-diverso (el "headline").
- **Mínimo 1 figura** (el template la exige, el rubric la premia): ej. barras de refusal/ASR inglés vs español por modelo.
- Validación: test de significancia en las diferencias (suma en Execution).

### 5. Discussion & Limitations (~0.5p)
- Implicancias para organismos GS.
- Limitaciones: N chico, 48h, confiabilidad del judge, español-diverso no separa por región.
- Future Work: V2 y V3, diferenciación regional, corpus más grande, pasos recortados.

### 6. Conclusion (1–2 párrafos)

### Code & Data
Repo GitHub + dataset de prompts.

### Appendix
Prompts completos, métricas detalladas, resultados extendidos.

### LLM Usage Statement
Cómo se usó IA + verificación.

---

## PARTE B — El MVP mínimo end-to-end (lo que construimos PRIMERO)

Objetivo: tener TODO el pipeline funcionando con el mínimo alcance, y después escalar. Mejor un end-to-end chico y completo que medio framework sin resultados.

**MVP v0 — lo más chico que produce un scorecard:**
1. **1 modelo open-weight** chico (ej. Qwen2.5-7B o Llama-3.1-8B).
2. **2 de los 6 pasos**, los de mayor señal y más baratos:
   - Paso 4 (jailbreak ΔASR) — el corazón del argumento de seguridad.
   - Paso 3 (over-refusal / FRR) — el contrapeso (que no rechace todo lo legítimo).
3. **~20–30 prompts por paso**, en inglés vs español-diverso.
4. **LLM-judge** binario + revisión humana rápida.
5. **1 tabla + 1 figura** con el resultado.
6. **Scorecard L1/L2/L3** para ese modelo en esos 2 pasos.

Con eso ya está demostrada la estructura completa. Después se escala:
- **v1:** sumar los otros 4 pasos.
- **v2:** sumar el 2do y 3er modelo.
- **v3:** subir el N de prompts y agregar la validación estadística.
