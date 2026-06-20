"""
Estadísticas — McNemar EN vs ES + tamaño de efecto
Compara el comportamiento del modelo en inglés vs español-diverso para los mismos prompts.

Hipótesis: el modelo falla MÁS en español que en inglés (ΔASR > 0 para paso4; ΔFRR > 0 para paso3).
Test estadístico: McNemar (pareado binario sobre los pares discordantes).
Tamaño de efecto: Cohen's h (diferencia entre proporciones pareadas).

Uso:
    python stats.py --scored ../results/scored/Qwen2.5_7B_Instruct_responses_scored.csv
    python stats.py --scored ../results/scored/Llama_3.1_8B_scored.csv --output-dir ../results

Output:
    results/stats_<model_slug>.json   — p-values, effect sizes, ΔASR, ΔFRR por paso
    Imprime tabla resumen en consola
"""

import argparse
import csv
import json
import math
import re
from pathlib import Path
from collections import defaultdict


def slugify(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_-]", "_", name)


def load_scored(path: str) -> list[dict]:
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["is_failure"] = int(row["is_failure"])
            row["score"] = int(row["score"])
            rows.append(row)
    return rows


def get_base_id(row_id: str) -> str:
    return re.sub(r"_(en|es)$", "", row_id)


def mcnemar(n01: int, n10: int) -> float:
    """McNemar p-value (continuity-corrected)."""
    total = n01 + n10
    if total == 0:
        return 1.0
    chi2 = (abs(n01 - n10) - 1) ** 2 / total
    return chi2_to_p(chi2, df=1)


def chi2_to_p(chi2: float, df: int = 1) -> float:
    """Aproximación de p-value via distribución chi2 (df=1)."""
    if chi2 <= 0:
        return 1.0
    x = chi2 / 2.0
    p = math.exp(-x)
    if df == 1:
        term = p
        result = p
        for k in range(1, 30):
            term *= x / k
            result += term
        return min(max(1 - result + p, 0.0), 1.0)
    return 1.0


def cohen_h(p1: float, p2: float) -> float:
    """Cohen's h para diferencia entre dos proporciones."""
    phi1 = 2 * math.asin(math.sqrt(max(0, min(1, p1))))
    phi2 = 2 * math.asin(math.sqrt(max(0, min(1, p2))))
    return phi1 - phi2


def analyze_step(pairs_en: dict, pairs_es: dict, step: str, expected_behavior: str) -> dict:
    common_ids = set(pairs_en.keys()) & set(pairs_es.keys())
    n = len(common_ids)
    if n == 0:
        return {"step": step, "n_pairs": 0, "error": "No matching pairs"}

    n00 = n01 = n10 = n11 = 0
    failures_en = failures_es = 0

    for base_id in common_ids:
        fail_en = pairs_en[base_id]["is_failure"]
        fail_es = pairs_es[base_id]["is_failure"]
        failures_en += fail_en
        failures_es += fail_es
        if fail_en == 0 and fail_es == 0:
            n00 += 1
        elif fail_en == 0 and fail_es == 1:
            n01 += 1
        elif fail_en == 1 and fail_es == 0:
            n10 += 1
        else:
            n11 += 1

    rate_en = failures_en / n
    rate_es = failures_es / n
    delta = rate_es - rate_en
    p_val = mcnemar(n01, n10)
    h = cohen_h(rate_es, rate_en)

    return {
        "step": step,
        "expected_behavior": expected_behavior,
        "n_pairs": n,
        "failure_rate_en": round(rate_en, 4),
        "failure_rate_es": round(rate_es, 4),
        "delta_es_minus_en": round(delta, 4),
        "n00_both_ok": n00,
        "n01_only_es_fails": n01,
        "n10_only_en_fails": n10,
        "n11_both_fail": n11,
        "mcnemar_p_value": round(p_val, 6),
        "significant_p05": p_val < 0.05,
        "cohen_h": round(h, 4),
        "effect_size": "large" if abs(h) >= 0.5 else "medium" if abs(h) >= 0.2 else "small",
    }


def main():
    parser = argparse.ArgumentParser(description="Estadísticas McNemar — S-OWMI V1")
    parser.add_argument("--scored", required=True, help="CSV scored (output de judge.py)")
    parser.add_argument("--output-dir", default="../results")
    args = parser.parse_args()

    rows = load_scored(args.scored)
    model_name = rows[0].get("model", "unknown") if rows else "unknown"
    print(f"Modelo: {model_name}")
    print(f"Total respuestas: {len(rows)}")

    by_step: dict[str, dict[str, dict]] = defaultdict(lambda: {"en": {}, "es": {}})
    step_behavior: dict[str, str] = {}

    for row in rows:
        step = row["step"]
        lang = row["lang"]
        base_id = get_base_id(row["id"])
        by_step[step][lang][base_id] = row
        if step not in step_behavior:
            step_behavior[step] = row["expected_behavior"]

    step_order = ["paso3", "paso4", "paso5", "paso6"]
    step_names = {
        "paso3": "Over-refusal (FRR)",
        "paso4": "Harmful/jailbreak (ΔASR)",
        "paso5": "Toxicidad/sesgo (BSS)",
        "paso6": "Factualidad (FES/FCR)",
    }

    results = []
    print(f"\n{'='*70}")
    print(f"{'Step':<22} {'N':>4} {'Fail EN':>8} {'Fail ES':>8} {'Delta':>7} {'p-value':>9} {'h':>6} {'Sig?':>5}")
    print(f"{'-'*70}")

    for step in step_order:
        if step not in by_step:
            continue
        result = analyze_step(
            by_step[step]["en"],
            by_step[step]["es"],
            step,
            step_behavior.get(step, "?")
        )
        results.append(result)

        name = step_names.get(step, step)
        n = result.get("n_pairs", 0)
        if n == 0:
            print(f"  {name:<22} {'—':>4}")
            continue

        fe = f"{100*result['failure_rate_en']:.1f}%"
        fs = f"{100*result['failure_rate_es']:.1f}%"
        d = f"{result['delta_es_minus_en']:+.3f}"
        p = f"{result['mcnemar_p_value']:.4f}"
        h = f"{result['cohen_h']:+.3f}"
        sig = "✓" if result["significant_p05"] else "·"
        print(f"  {name:<22} {n:>4} {fe:>8} {fs:>8} {d:>7} {p:>9} {h:>6} {sig:>5}")

    print(f"{'='*70}")

    overall_fail_en = sum(r["is_failure"] for r in rows if r["lang"] == "en")
    overall_fail_es = sum(r["is_failure"] for r in rows if r["lang"] == "es")
    total_en = sum(1 for r in rows if r["lang"] == "en")
    total_es = sum(1 for r in rows if r["lang"] == "es")
    headline_delta = (overall_fail_es / max(total_es, 1)) - (overall_fail_en / max(total_en, 1))

    print(f"\n  Headline ΔASR global (ES−EN): {headline_delta:+.3f}")
    print(f"  ({overall_fail_en}/{total_en} fallos EN | {overall_fail_es}/{total_es} fallos ES)")
    print(f"\n  Nota: p-value McNemar: <0.05 → diferencia estadísticamente significativa")
    print(f"        Cohen's h: |h|≥0.5 large, |h|≥0.2 medium, |h|<0.2 small")

    output = {
        "model": model_name,
        "total_responses": len(rows),
        "headline_delta_es_minus_en": round(headline_delta, 4),
        "per_step": results,
    }

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(model_name)
    out_path = out_dir / f"stats_{slug}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\n  Estadísticas guardadas en: {out_path}")


if __name__ == "__main__":
    main()
