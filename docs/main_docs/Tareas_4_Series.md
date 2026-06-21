# Plan técnico — 4 series de trabajo (S-OWMI Vertical 1)

**Objetivo:** dividir todo lo técnico que queda en 4 series de carga similar y con la menor dependencia posible entre ellas. Cada serie tiene un dueño, puede **arrancar ya** con trabajo independiente, y solo sincroniza con las demás en un punto fino al final.

**Estado base (ya hecho):** dataset de 200 prompts (`prompts/prompts.csv`), corpus paralelo (`prompts/parallel_corpus/corpus.csv`), y todos los scripts del pipeline (`code/`). Decisión: alcance expandido (Pasos 1, 3, 4, 5, 6) + GPU disponible. Modelos: Qwen2.5-7B-Instruct y Llama-3.1-8B-Instruct.

**La única dependencia real:** la inferencia (Serie 1) tiene que correr antes de que las Series 2 y 3 cierren sus números. Por eso cada serie tiene trabajo "que se puede hacer ya" (sin esperar) y trabajo "post-inferencia". Además, **cada serie redacta su propia sección del paper**, así no hay un único cuello de botella de escritura.

---

## Serie 1 — Ejecución empírica (correr los modelos)
**Dueño:** ___ (quien tenga la GPU)

**Qué se puede hacer YA (no depende de nadie):**
- [ ] Setup del entorno: `pip install -r code/requirements.txt`, verificar acceso GPU.
- [ ] Conseguir acceso a los modelos en HuggingFace (Llama 3.1 requiere aceptar licencia).
- [ ] Smoke test: correr `run_inference.py` con 2-3 prompts para validar que el modelo carga y responde.
- [ ] Paso 1 (fertilidad): `tokenizer_fertility.py` para ambos modelos (no requiere inferencia, es rápido).

**Trabajo central:**
- [ ] Inferencia Qwen2.5-7B: 200 prompts (EN + ES) → `results/raw/`
- [ ] Inferencia Llama-3.1-8B: 200 prompts (EN + ES) → `results/raw/`
- [ ] Judge: `judge.py` sobre ambos (Llama Guard 3 para harmful / GPT-4o para over-refusal, sesgo, factualidad; o `--rule-based` como fallback) → `results/scored/`

**Entrega:** `results/raw/*.csv`, `results/scored/*.csv`, `results/paso1_*.csv` para los 2 modelos.
**Escribe en el paper:** sub-bloque de Methods sobre setup de ejecución (modelos, hardware, parámetros de generación, judge).

---

## Serie 2 — Análisis cuantitativo + sección Results
**Dueño:** ___

**Qué se puede hacer YA:**
- [ ] Generar un CSV "mock" de respuestas (5-10 filas a mano) y correr `stats.py`, `score_scorecard.py` y `plot_figure.py` end-to-end para validar que los scripts funcionan y entender los outputs.
- [ ] Definir el formato exacto de la tabla y la figura headline para el paper (qué ejes, qué colores, qué se compara).

**Trabajo central (cuando Serie 1 entregue `results/scored/`):**
- [ ] `stats.py` por modelo → McNemar (EN vs ES) + Cohen's h por paso + p-values.
- [ ] `score_scorecard.py` por modelo → niveles L1/L2/L3 por paso + score V1 global.
- [ ] `plot_figure.py` → figura headline (EN vs ES por paso/modelo) + figura ΔASR.
- [ ] Sanity check: ¿los números tienen sentido? ¿el ΔASR es positivo como predice la hipótesis?

**Entrega:** `results/stats_*.json`, `results/scorecard.csv`, `figures/*.png`.
**Escribe en el paper:** sección **Results** completa (Tabla 1 con números reales, figura, narrativa del scorecard).

---

## Serie 3 — Validación cualitativa + sección Discussion
**Dueño:** ___

**Qué se puede hacer YA:**
- [ ] QA del dataset: revisar las 200 filas de `prompts.csv` — que las traducciones ES estén bien, que los estilos (neutro/spanglish/mixto) sean genuinos, que las answer_keys factuales sean correctas.
- [ ] Definir el protocolo de revisión humana: criterios para marcar una respuesta como fallo/no-fallo, plantilla de notas.

**Trabajo central (cuando Serie 1 entregue `results/scored/`):**
- [ ] Revisión humana del 20% (`judge.py` ya marca la muestra en `*_human_review.csv`): leer ~80-120 respuestas, comparar con la etiqueta del judge, reportar accuracy del judge (clave para Execution del rubric).
- [ ] Análisis de errores por estilo: ¿spanglish o mixto rompen más la defensa que el neutro? (alimenta el argumento de "español-diverso" y el Paso 2 cualitativo).
- [ ] Ejemplos cualitativos: 2-3 casos donde el modelo rechaza en inglés y cumple en español (para mostrar en el paper).

**Entrega:** muestra humana validada + accuracy del judge + hallazgos cualitativos + ejemplos.
**Escribe en el paper:** **Discussion + Limitations** (qué significa para organismos, confiabilidad del judge, qué estilo es más vulnerable).

---

## Serie 4 — Marco del paper + entrega final
**Dueño:** ___

**Independiente de los resultados — se puede hacer casi todo YA:**
- [ ] Pulir **Introduction** y **Related Work** (las fuentes ya están en `Related_Work_Justifications.md`).
- [ ] Redactar **Abstract** y **Conclusion** (con huecos para los números finales).
- [ ] Armar el **Appendix**: tabla de prompts, descripción de metodología extendida.
- [ ] **LLM Usage Statement** + sección Code & Data.
- [ ] Pasar todo al **template oficial** (`Global South AI Safety hackathon submission template`), respetar ~4 páginas.
- [ ] Referencias / bibliografía en formato consistente.

**Cierre (al final, integrando a las demás series):**
- [ ] Insertar los números de Serie 2 en Results y los hallazgos de Serie 3 en Discussion.
- [ ] Pase final de coherencia y largo (4 páginas, "quality over quantity").
- [ ] Exportar el PDF final y subirlo.

**Entrega:** el research report final en el template oficial, listo para enviar.

---

## Mapa de dependencias (resumen)

```
Serie 1 (inferencia) ──> results/scored/ ──┬──> Serie 2 (stats/figuras/Results)
                                           └──> Serie 3 (revisión/Discussion)

Serie 4 (marco del paper) ── independiente ──> integra Results+Discussion al final
```

- **Series 2, 3 y 4 arrancan ya** con su bloque "se puede hacer YA" (mock data, QA de dataset, redacción del marco).
- El único hand-off duro es `results/scored/` de Serie 1 → Series 2 y 3.
- Cada serie escribe su propia sección → no hay un solo redactor saturado; Serie 4 ensambla.
