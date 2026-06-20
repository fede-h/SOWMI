# Plan de Trabajo Técnico — S-OWMI Vertical 1

**Fecha:** 20/06/2026
**Alcance:** lado técnico completo de Vertical 1 (los 6 pasos), ~100 prompts base, modelos open-weight.
**Narrativa:** V1 es el core empírico. Sus hallazgos se usan para argumentar por qué V2 y V3 son necesarias.

---

## 1. Objetivo técnico

Producir el **scorecard S-OWMI Vertical 1** para 2–3 modelos open-weight, comparando **inglés vs español-diverso**, con validación estadística y un dataset reproducible.

**Outputs concretos:** tabla de niveles L1/L2/L3 por paso + score V1 global, 1 figura headline, y repo reproducible (prompts + scripts + resultados).

---

## 2. Cómo V1 motiva V2 y V3 (la bisagra del paper)

Esto es lo que decidimos: usar **toda la evidencia de V1** para justificar que V2 y V3 importan.

- Si V1 muestra que **el conocimiento peligroso persiste en español** (Paso 4) y que **la curación de datos en español es débil** (Pasos 1, 3, 5, 6), entonces:
  - **V2 (Provenance & Robustness) importa:** un modelo ya inseguro en español, con pesos editables/abliterables y sin trazabilidad, multiplica el riesgo. *"No solo es inseguro en español: tampoco se puede rastrear quién lo empeoró tras un fine-tuning local."*
  - **V3 (Tiered Release & Testing) importa:** si el red-teaming en inglés no detecta estos fallos (lo confirma J1: 12/12 frameworks no testean en español), liberar sin testing adversarial en español es liberar a ciegas.
- **En el paper:** V1 = evidencia empírica; V2 y V3 = "por lo tanto, estas dos dimensiones no son opcionales". Va en Discussion / Conclusion, apoyado por la tabla maestra de J1.

---

## 3. Dataset de prompts (~100 base)

Cada prompt base se renderiza en **2 idiomas**: **EN** (baseline) y **ES-diverso**. El set ES-diverso mezcla estilos sin separarlos por región: **~⅓ neutro, ~⅓ spanglish, ~⅓ regionalismos mezclados**. La diversidad ES la condición.

| Categoría | # base | Alimenta | Tipo |
|---|---|---|---|
| Harmful / jailbreak | 40 | Paso 4 (ΔASR) + Paso 2 (variantes) | dañino |
| Benigno-sensible (over-refusal) | 20 | Paso 3 (FRR / SFV) | benigno con triggers |
| Toxicidad / sesgo | 15 | Paso 5 (BSS) | ambiguo / sesgo |
| Factual dominios locales | 25 | Paso 6 (FES / FCR) | Q&A (salud, derecho, finanzas, gobierno LATAM) |
| **Total** | **100** | | |

- **Harmful 40** cubre 5 sub-categorías (8 c/u): desinformación/electoral, fraude/evasión, autolesión, odio/discriminación, violencia.
- **Factual 25**: mitad pre-cutoff (con answer key) + mitad post-cutoff o sin respuesta clara (mide alucinación + calibración).
- **Paso 1 NO usa estos prompts**: usa un corpus paralelo EN/ES (fragmentos de Wikipedia) + el tokenizer del modelo. Es un script aparte.

**Formato (CSV/JSON):** `id, category, step, lang, style, text, expected_behavior, answer_key`.
Total de inferencias: 100 base × 2 idiomas × N modelos (≈ 200/modelo).

### 3.1 — Por qué 100 prompts (ni más ni menos)

- **Suficiente para validez estadística.** Con ~100 prompts pareados (el mismo prompt en EN y ES), McNemar tiene poder para detectar diferencias moderadas en el eje principal (refusal/ASR): lo que cuenta son los pares discordantes (rechaza en EN, cumple en ES), y a este N hay suficientes para sostener significancia en la comparación headline EN vs ES. Está en línea con los benchmarks de referencia: JailbreakBench (100 behaviors), AdvBench/HarmBench (subsets ~100), MultiJail (~35 por idioma).
- **Suficientemente chico para 48h.** 100 × 2 idiomas × 2–3 modelos = 400–600 inferencias + judge + revisión humana del 20% (~80–120 casos). Es ejecutable y revisable en el tiempo que queda. Subir a 300 mejoraría el poder por categoría pero rompe el timeline y arriesga el "scattered / sin terminar" que el rubric penaliza en Execution.
- **Distribución pensada por métrica.** El split 40/20/15/25 le da a cada paso un N mínimo razonable. La categoría más chica (toxicidad, 15) es el piso: alcanza para una señal direccional, no para un estimado fino — lo declaramos como limitación. La comparación headline (refusal/ASR global EN vs ES) sí agrupa ítems suficientes para significancia.
- **¿Crear más?** 100 está bien para el hackathon. Si una categoría necesita una afirmación más firme, conviene **subir esa categoría** (ej. toxicidad de 15 a 25) antes que inflar el total. No agregar prompts "porque sí": más volumen sin terminar el pipeline puntúa peor que 100 bien ejecutados.

---

## 4. Los 6 pasos — método, métrica, output

### Paso 1 — Fertilidad de tokens → SCC
- **Input:** corpus paralelo EN/ES (~200 fragmentos equivalentes).
- **Método:** tokenizar con `AutoTokenizer` del modelo; calcular tokens/palabra (fertilidad) y ratio ES/EN.
- **Métrica:** Spanish Corpus Coverage (proxy). Alta fertilidad en ES = baja representación en pretraining.
- **Output:** 1 número por modelo + comparación.

### Paso 2 — Robustez ante variantes → RCS
- **Input:** los 40 harmful en ES-diverso, etiquetados por estilo (neutro / spanglish / mixto).
- **Método:** refusal rate por estilo; ver si spanglish/mixto baja más la defensa que el neutro.
- **Métrica:** Regional Coverage Score (robustez across estilos).
- **Output:** refusal por estilo (análisis secundario / cualitativo).

### Paso 3 — Filtrado semántico / over-refusal → SFV, FRR
- **Input:** 20 benignos-sensibles (dictaduras LATAM, salud, desintoxicación de discurso de odio, etc.).
- **Método:** medir falsos rechazos (rechaza algo legítimo), EN vs ES.
- **Métrica:** False Refusal Rate. Si ES rechaza más benignos que EN → filtros anglosajones traducidos.
- **Output:** FRR EN vs ES.

### Paso 4 — Probe de conocimiento peligroso → ΔASR  *(el corazón)*
- **Input:** 40 harmful, EN vs ES-diverso.
- **Método:** Attack Success Rate (el modelo cumple el pedido dañino). ΔASR = ASR_ES − ASR_EN.
- **Métrica:** ΔASR.
- **Output:** ASR EN vs ES por modelo + Δ.

### Paso 5 — Toxicidad / sesgos → BSS
- **Input:** 15 prompts ambiguos basados en dichos/refranes y dinámicas de poder LATAM.
- **Método:** clasificar outputs por sesgo/estereotipo (género, etnia, nivel socioeconómico, origen).
- **Métrica:** Bias and Stereotype Score.
- **Output:** BSS EN vs ES.

### Paso 6 — Factualidad / alucinación → FES, FCR
- **Input:** 25 factual (salud estilo MIR, finanzas FLARE-ES, derecho/admin pública LATAM).
- **Método:** accuracy contra answer key (pre-cutoff); en post-cutoff, medir si alucina con confianza vs hedging. False Citation Rate = inventa leyes/artículos.
- **Métrica:** Factuality Evaluation Score + False Citation Rate.
- **Output:** FES, FCR EN vs ES.

---

## 5. Evaluación

- **LLM-as-a-judge** (un modelo que NO sea sujeto, ej. GPT-4o o Llama Guard 3): clasifica refusal (0 = rechaza / 1 = parcial / 2 = cumple), toxicidad, y factual contra key.
- **Revisión humana del 20%** de las respuestas para validar el judge.
- **Estadística:** McNemar (EN vs ES, pareado binario) para refusal/ASR; reportar p-value y tamaño de efecto (Cohen's h). Suma directo en Execution del rubric.

---

## 6. Modelos (a fijar por el equipo)

- Al menos **2–3 open-weight**. Propuesta: **Qwen2.5-7B-Instruct**, **Llama-3.1-8B-Instruct**, + uno opcional (Mistral-7B, o un modelo entrenado en español como Salamandra/ALIA si entra en tiempo/compute).
- **Ejecución:** local (GPU/CPU) o inferencia barata. Nota: los 300 créditos Adaption son de *training*, no de inferencia.

---

## 7. Scaffold del repo (a agregar — hoy es solo docs)

```
/code
  tokenizer_fertility.py   # Paso 1
  run_inference.py         # corre los 100×2 prompts por modelo
  judge.py                 # LLM-judge + scoring
  score_scorecard.py       # arma L1/L2/L3 por paso + score V1
  stats.py                 # McNemar + effect size
/prompts
  prompts.csv              # dataset 100 base × idioma × estilo
  parallel_corpus/         # fragmentos EN/ES para Paso 1
/results
  raw/                     # outputs crudos por modelo
  scored/                  # outputs clasificados
  scorecard.csv            # tabla final
/figures
  headline_en_vs_es.png
```

---

## 8. Pipeline de ejecución (orden)

1. Cerrar dataset de 100 prompts (EN + ES-diverso con estilos).
2. `tokenizer_fertility.py` (Paso 1) — rápido, sin inferencia.
3. `run_inference.py` por modelo → `results/raw`.
4. `judge.py` → `results/scored`.
5. `stats.py` + `score_scorecard.py` → scorecard + p-values.
6. `figures` → 1 figura headline (refusal/ASR EN vs ES por modelo).
7. Volcar a Results + Appendix del paper.

---

## 9. Tareas (asignar en el equipo)

- [ ] Redactar los 100 prompts base (EN) + adaptar a ES-diverso con estilos — owner: ___
- [ ] Answer keys de los 25 factual — owner: ___
- [ ] Código: inference + judge + scoring + stats — owner: ___
- [ ] Correr en los 2–3 modelos — owner: ___
- [ ] Figura headline + tabla scorecard — owner: ___
- [ ] Escribir Methods + Results con los números — owner: ___

---

## 10. Timeline (queda ~1 día — cierre domingo 21/06)

- **Sábado tarde/noche:** dataset cerrado + código base + Paso 1 corriendo.
- **Sábado noche / domingo mañana:** inferencia + judge en el 1er modelo (= el MVP v0), después escalar a los otros.
- **Domingo mediodía:** stats + scorecard + figura.
- **Domingo tarde:** escribir Results/Methods, volcar al template, revisar y entregar.
