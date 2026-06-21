"""
Genera el CSV de revisión ciega a partir del output de judge.py.
Remueve score, label, reasoning, is_failure para que el revisor no pueda ver
la decisión del judge antes de asignar su propio score.

Uso:
    python make_blind_review_csv.py \
        --input ../results/scored/ModelX_scored.csv \
        --output ../results/human_review/ModelX_blind_review.csv
"""

import argparse
import csv
from pathlib import Path

REMOVE_COLS = {"score", "label", "reasoning", "is_failure", "needs_human_review"}
ADD_COLS    = ["human_score", "human_notes"]
KEEP_ORDER  = [
    "id", "category", "subcategory", "step", "lang", "style",
    "model", "prompt", "response", "expected_behavior", "answer_key",
]


def main():
    parser = argparse.ArgumentParser(description="Genera CSV de revisión ciega")
    parser.add_argument("--input",  required=True, help="CSV scored (output de judge.py)")
    parser.add_argument("--output", required=True, help="CSV ciego para el revisor")
    parser.add_argument("--all",    action="store_true",
                        help="Incluir todas las filas (por defecto solo needs_human_review=1)")
    args = parser.parse_args()

    rows = []
    with open(args.input, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not args.all and int(row.get("needs_human_review", 0)) != 1:
                continue
            rows.append(row)

    if not rows:
        print("Sin filas para revisión humana. Usá --all para incluir todas.")
        return

    # Construir fieldnames: columnas visibles en orden + columnas extra al final
    visible = [c for c in KEEP_ORDER if c in rows[0]]
    extra   = [c for c in rows[0] if c not in REMOVE_COLS and c not in visible]
    fieldnames = visible + extra + ADD_COLS

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            clean = {k: v for k, v in row.items() if k not in REMOVE_COLS}
            clean["human_score"] = ""
            clean["human_notes"] = ""
            writer.writerow(clean)

    print(f"CSV ciego generado: {out_path}")
    print(f"Filas para revisión: {len(rows)}")
    print(f"Columnas removidas:  {', '.join(REMOVE_COLS)}")
    print(f"Columnas a completar: human_score, human_notes")


if __name__ == "__main__":
    main()
