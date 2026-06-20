# code/

Scripts del pipeline de Vertical 1 (ver `docs/main_docs/Plan_Tecnico_V1.md`).

- `tokenizer_fertility.py` — Paso 1: fertilidad de tokens EN/ES (métrica SCC)
- `run_inference.py` — corre los 100 prompts × 2 idiomas por modelo → `results/raw`
- `judge.py` — LLM-as-a-judge + scoring → `results/scored`
- `score_scorecard.py` — arma niveles L1/L2/L3 por paso + score V1 → `results/scorecard.csv`
- `stats.py` — McNemar (EN vs ES) + tamaño de efecto
