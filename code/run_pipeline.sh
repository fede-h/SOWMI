#!/bin/bash
# Pipeline completo S-OWMI V1 para un modelo
# Uso: bash run_pipeline.sh <nombre_modelo_hf>
# Ejemplo: bash run_pipeline.sh Qwen/Qwen2.5-7B-Instruct

MODEL=${1:-"Qwen/Qwen2.5-7B-Instruct"}
PROMPTS="../prompts/prompts.csv"
CORPUS="../prompts/parallel_corpus/corpus.csv"
RESULTS="../results"
FIGURES="../figures"

echo "========================================"
echo "  S-OWMI V1 — Pipeline completo"
echo "  Modelo: $MODEL"
echo "========================================"

echo ""
echo "--- PASO 1: Fertilidad de tokens ---"
python tokenizer_fertility.py \
    --model "$MODEL" \
    --corpus "$CORPUS" \
    --output-dir "$RESULTS"

echo ""
echo "--- PASOS 2-6: Inferencia ---"
python run_inference.py \
    --model "$MODEL" \
    --prompts "$PROMPTS" \
    --max-new-tokens 512 \
    --device auto \
    --output-dir "$RESULTS/raw"

# Determinar nombre del archivo de respuestas
MODEL_SLUG=$(echo "$MODEL" | sed 's/[^a-zA-Z0-9_-]/_/g')
RAW_FILE="$RESULTS/raw/${MODEL_SLUG}_responses.csv"

echo ""
echo "--- Judge (LLM o rule-based) ---"
# Usar --rule-based si no hay OPENAI_API_KEY configurada
if [ -z "$OPENAI_API_KEY" ]; then
    echo "  OPENAI_API_KEY no configurada → usando rule-based judge"
    python judge.py \
        --input "$RAW_FILE" \
        --rule-based \
        --output-dir "$RESULTS/scored"
else
    echo "  Usando GPT-4o como judge"
    python judge.py \
        --input "$RAW_FILE" \
        --judge-model gpt-4o \
        --output-dir "$RESULTS/scored"
fi

SCORED_FILE="$RESULTS/scored/${MODEL_SLUG}_responses_scored.csv"
PASO1_FILE="$RESULTS/paso1_fertility_${MODEL_SLUG}.csv"
STATS_FILE="$RESULTS/stats_${MODEL_SLUG}.json"

echo ""
echo "--- Estadísticas McNemar ---"
python stats.py \
    --scored "$SCORED_FILE" \
    --output-dir "$RESULTS"

echo ""
echo "--- Scorecard ---"
python score_scorecard.py \
    --scored "$SCORED_FILE" \
    --stats  "$STATS_FILE" \
    --paso1  "$PASO1_FILE" \
    --model  "$MODEL" \
    --output-dir "$RESULTS"

echo ""
echo "--- Figura headline ---"
python plot_figure.py \
    --scored "$SCORED_FILE" \
    --output-dir "$FIGURES"

echo ""
echo "========================================"
echo "  Pipeline completo para: $MODEL"
echo "  Resultados en: $RESULTS"
echo "  Figuras en: $FIGURES"
echo "========================================"
