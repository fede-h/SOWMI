# prompts/

- `prompts.csv` — 100 prompts base, cada uno en EN y ES-diverso.
  Columnas: `id, category, step, lang, style, text, expected_behavior, answer_key`.
  Categorías: harmful (40), benigno-sensible/over-refusal (20), toxicidad (15), factual (25).
  Estilos ES: neutro / spanglish / regionalismos mezclados.
- `parallel_corpus/` — fragmentos paralelos EN/ES para el Paso 1 (fertilidad de tokens).
