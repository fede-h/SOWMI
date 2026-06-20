"""
Paso 1 — Fertilidad de tokens (Spanish Corpus Coverage proxy)
Calcula el ratio de fertilidad ES/EN por modelo: tokens_por_palabra en ES vs EN.
Alta fertilidad ES = el modelo segmenta más en ES = menos cobertura del español en pretraining.

Uso:
    python tokenizer_fertility.py --model Qwen/Qwen2.5-7B-Instruct --corpus ../prompts/parallel_corpus/corpus.csv
    python tokenizer_fertility.py --model meta-llama/Llama-3.1-8B-Instruct --corpus ../prompts/parallel_corpus/corpus.csv

Output:
    results/paso1_fertility_<model_slug>.csv   — fertilidad por fragmento
    results/paso1_summary.csv                  — SCC por modelo (acumulado)
"""

import argparse
import csv
import json
import os
import re
from pathlib import Path

try:
    from transformers import AutoTokenizer
except ImportError:
    raise SystemExit("ERROR: instalar transformers: pip install transformers")


RESULTS_DIR = Path("../results")


def slugify(model_name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", model_name)


def load_corpus(corpus_path: str) -> list[dict]:
    rows = []
    with open(corpus_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    if not rows:
        raise ValueError(f"Corpus vacío: {corpus_path}")
    required = {"id", "text_en", "text_es", "domain"}
    missing = required - set(rows[0].keys())
    if missing:
        raise ValueError(f"Columnas faltantes en corpus: {missing}")
    return rows


def count_words(text: str) -> int:
    return len(text.split())


def fertility(tokenizer, text: str) -> float:
    tokens = tokenizer.encode(text, add_special_tokens=False)
    words = count_words(text)
    return len(tokens) / max(words, 1)


def run(model_name: str, corpus_path: str, output_dir: Path) -> dict:
    print(f"Cargando tokenizer: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

    corpus = load_corpus(corpus_path)
    print(f"Corpus: {len(corpus)} fragmentos")

    output_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(model_name)
    out_file = output_dir / f"paso1_fertility_{slug}.csv"

    ratios = []
    rows_out = []

    for item in corpus:
        fert_en = fertility(tokenizer, item["text_en"])
        fert_es = fertility(tokenizer, item["text_es"])
        ratio = fert_es / max(fert_en, 0.001)
        ratios.append(ratio)
        rows_out.append({
            "id": item["id"],
            "domain": item.get("domain", ""),
            "words_en": count_words(item["text_en"]),
            "words_es": count_words(item["text_es"]),
            "fertility_en": round(fert_en, 4),
            "fertility_es": round(fert_es, 4),
            "fertility_ratio_es_en": round(ratio, 4),
        })

    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows_out[0].keys())
        writer.writeheader()
        writer.writerows(rows_out)

    avg_ratio = sum(ratios) / len(ratios)
    median_ratio = sorted(ratios)[len(ratios) // 2]

    scc_level = "L3" if avg_ratio < 1.10 else ("L2" if avg_ratio < 1.25 else "L1")

    summary = {
        "model": model_name,
        "n_fragments": len(corpus),
        "avg_fertility_ratio_es_en": round(avg_ratio, 4),
        "median_fertility_ratio_es_en": round(median_ratio, 4),
        "scc_level": scc_level,
        "interpretation": (
            "Tokenizer bien adaptado al español (L3)"
            if scc_level == "L3"
            else "Tokenizer medianamente adaptado (L2)"
            if scc_level == "L2"
            else "Alta sobre-segmentación del español → pretraining data limitado (L1)"
        ),
    }

    print(f"\n=== PASO 1 — {model_name} ===")
    print(f"  Fragmentos analizados: {len(corpus)}")
    print(f"  Ratio ES/EN promedio:  {avg_ratio:.4f}")
    print(f"  Ratio ES/EN mediana:   {median_ratio:.4f}")
    print(f"  Nivel SCC:             {scc_level}")
    print(f"  → {summary['interpretation']}")
    print(f"  Detalle guardado en:   {out_file}")

    return summary


def main():
    parser = argparse.ArgumentParser(description="Paso 1 — Fertilidad de tokens")
    parser.add_argument("--model", required=True, help="Nombre del modelo en HuggingFace")
    parser.add_argument(
        "--corpus",
        default="../prompts/parallel_corpus/corpus.csv",
        help="Ruta al corpus paralelo EN/ES",
    )
    parser.add_argument(
        "--output-dir",
        default=str(RESULTS_DIR),
        help="Directorio de salida para resultados",
    )
    parser.add_argument(
        "--summary-file",
        default=None,
        help="CSV acumulado con resultados de todos los modelos",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    summary = run(args.model, args.corpus, output_dir)

    summary_path = Path(args.summary_file) if args.summary_file else output_dir / "paso1_summary.csv"
    fieldnames = list(summary.keys())
    write_header = not summary_path.exists()
    with open(summary_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(summary)

    print(f"\nResumen acumulado: {summary_path}")


if __name__ == "__main__":
    main()
