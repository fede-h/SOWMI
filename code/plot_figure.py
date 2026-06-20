"""
Figura headline — EN vs ES failure rate por paso y modelo
Genera el gráfico principal del paper (barras agrupadas EN / ES por paso).

Uso:
    python plot_figure.py --scored results/scored/ModelA_scored.csv [results/scored/ModelB_scored.csv ...]
    python plot_figure.py --scorecard results/scorecard.csv --output figures/headline_en_vs_es.png

Output:
    figures/headline_en_vs_es.png   — figura para el paper
    figures/delta_asr_by_model.png  — gráfico de ΔASR por modelo
"""

import argparse
import csv
from pathlib import Path
from collections import defaultdict

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import numpy as np
except ImportError:
    raise SystemExit("ERROR: pip install matplotlib numpy")


STEP_SHORT = {
    "paso3": "Over-refusal\n(Paso 3)",
    "paso4": "Jailbreak\n(Paso 4)",
    "paso5": "Sesgo\n(Paso 5)",
    "paso6": "Factualidad\n(Paso 6)",
}

COLORS = {
    "en": "#4C72B0",
    "es": "#DD8452",
}


def load_scored_files(paths: list[str]) -> dict[str, list[dict]]:
    by_model = {}
    for path in paths:
        rows = []
        with open(path, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                row["is_failure"] = int(row["is_failure"])
                rows.append(row)
        model = rows[0]["model"] if rows else Path(path).stem
        by_model[model] = rows
    return by_model


def compute_failure_rates(rows: list[dict]) -> dict[str, dict[str, float]]:
    by_step_lang: dict[str, dict[str, list]] = defaultdict(lambda: {"en": [], "es": []})
    for row in rows:
        step = row["step"]
        lang = row["lang"]
        if step in STEP_SHORT:
            by_step_lang[step][lang].append(row["is_failure"])

    result = {}
    for step in STEP_SHORT:
        result[step] = {}
        for lang in ("en", "es"):
        	items = by_step_lang[step][lang]
        	result[step][lang] = sum(items) / len(items) if items else 0.0
    return result


def plot_grouped_bars(by_model: dict[str, list[dict]], output_path: str):
    steps = list(STEP_SHORT.keys())
    n_steps = len(steps)
    n_models = len(by_model)
    model_names = list(by_model.keys())

    bar_width = 0.35
    group_width = bar_width * 2 + 0.1
    x = np.arange(n_steps) * (group_width * n_models + 0.4)

    fig, ax = plt.subplots(figsize=(max(10, n_steps * 2.5), 5))

    for mi, (model_name, rows) in enumerate(by_model.items()):
        rates = compute_failure_rates(rows)
        offset = mi * group_width

        for li, lang in enumerate(("en", "es")):
            lang_offset = offset + li * bar_width
            heights = [rates[step][lang] * 100 for step in steps]
            bars = ax.bar(
                x + lang_offset, heights,
                bar_width, label=f"{model_name} ({lang.upper()})" if n_models > 1 else lang.upper(),
                color=COLORS[lang], alpha=0.85 if mi == 0 else 0.60,
                hatch="" if mi == 0 else "//",
                edgecolor="white", linewidth=0.8,
            )
            for bar, h in zip(bars, heights):
                if h > 0:
                    ax.text(
                        bar.get_x() + bar.get_width() / 2,
                        bar.get_height() + 0.8,
                        f"{h:.0f}%", ha="center", va="bottom",
                        fontsize=7, color="#333333",
                    )

    center_offset = (group_width * n_models) / 2 - bar_width / 2
    ax.set_xticks(x + center_offset)
    ax.set_xticklabels([STEP_SHORT[s] for s in steps], fontsize=9)
    ax.set_ylabel("Failure rate (%)", fontsize=10)
    ax.set_ylim(0, 110)
    ax.set_title(
        "S-OWMI V1 — Failure rate: English vs Spanish-diverse\n(higher = more failures = worse safety alignment)",
        fontsize=11, pad=12,
    )
    ax.axhline(50, color="gray", linewidth=0.7, linestyle="--", alpha=0.5)
    ax.legend(fontsize=9, loc="upper right")
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linewidth=0.5)

    fig.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Figura guardada: {output_path}")


def plot_delta_asr(by_model: dict[str, list[dict]], output_path: str):
    steps = list(STEP_SHORT.keys())
    model_names = list(by_model.keys())
    n_models = len(model_names)

    deltas_by_model = {}
    for model_name, rows in by_model.items():
        rates = compute_failure_rates(rows)
        deltas_by_model[model_name] = [
            rates[s]["es"] * 100 - rates[s]["en"] * 100 for s in steps
        ]

    x = np.arange(len(steps))
    bar_width = 0.6 / max(n_models, 1)

    fig, ax = plt.subplots(figsize=(9, 4.5))

    for mi, (model_name, deltas) in enumerate(deltas_by_model.items()):
        offset = (mi - (n_models - 1) / 2) * bar_width
        colors = ["#d62728" if d > 0 else "#2ca02c" for d in deltas]
        ax.bar(x + offset, deltas, bar_width, label=model_name, color=colors, alpha=0.8, edgecolor="white")

    ax.axhline(0, color="black", linewidth=1.2)
    ax.set_xticks(x)
    ax.set_xticklabels([STEP_SHORT[s] for s in steps], fontsize=9)
    ax.set_ylabel("ΔASR (ES − EN, percentage points)", fontsize=10)
    ax.set_title("S-OWMI V1 — Gap between Spanish and English failure rates\n(positive = model fails MORE in Spanish than English)", fontsize=11, pad=10)
    ax.legend(fontsize=9)
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linewidth=0.5)

    red_patch = mpatches.Patch(color="#d62728", label="Spanish worse (positive ΔASR)")
    green_patch = mpatches.Patch(color="#2ca02c", label="Spanish better / equal")
    ax.legend(handles=[red_patch, green_patch], fontsize=8, loc="lower right")

    fig.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Figura delta guardada: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Plot S-OWMI V1 headline figure")
    parser.add_argument("--scored", nargs="+", help="Uno o más CSV scored de judge.py")
    parser.add_argument("--output-dir", default="../figures")
    args = parser.parse_args()

    if not args.scored:
        print("ERROR: proveer --scored <archivo.csv> [archivo2.csv ...]")
        return

    by_model = load_scored_files(args.scored)
    print(f"Modelos: {list(by_model.keys())}")

    out_dir = Path(args.output_dir)
    plot_grouped_bars(by_model, str(out_dir / "headline_en_vs_es.png"))
    plot_delta_asr(by_model, str(out_dir / "delta_asr_by_model.png"))


if __name__ == "__main__":
    main()
