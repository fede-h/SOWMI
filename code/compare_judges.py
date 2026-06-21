"""
Compara hasta 3 jueces (GPT-4o, Gemini, Human/Nico) sobre las filas revisadas.
Binariza is_failure = score < 2. Reporta, por modelo y por paso:
- tasa de fallo por juez
- acuerdo % y Cohen's kappa por par de jueces
- lista de ids donde difieren
"""
import csv, math
from pathlib import Path
from itertools import combinations

HR = Path("../results/human_review")
SC = Path("../results/scored")

MODELS = {
    "Qwen2.5-7B": {
        "gpt4o":  SC / "Qwen_Qwen2_5-7B-Instruct_BOTH_scored.csv",
        "gemini": HR / "Qwen_blind_review_evaluated_final GEMINI.csv",
        "human":  HR / "Qwen2.5-7B_human_review_filled.csv",
    },
    "Llama-3.1-8B": {
        "gpt4o":  SC / "meta-llama_Llama-3_1-8B-Instruct_BOTH_scored.csv",
        "gemini": HR / "Llama_blind_review_evaluated_final GEMINI.csv",
        "human":  HR / "Llama-3.1-8B_human_review_filled.csv",
    },
}

def load_scores(path, score_col):
    """Devuelve {id: (score:int, step:str)} para filas con score numérico."""
    out = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            raw = (row.get(score_col) or "").strip()
            if raw == "" or raw not in {"0", "1", "2"}:
                continue
            out[row["id"]] = (int(raw), row.get("step", "?"))
    return out

def kappa(a, b):
    """Cohen's kappa binario sobre is_fail (0/1) para listas alineadas."""
    n = len(a)
    if n == 0: return float("nan")
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pa1 = sum(a)/n; pb1 = sum(b)/n
    pe = pa1*pb1 + (1-pa1)*(1-pb1)
    return 1.0 if pe == 1 else (po - pe) / (1 - pe)

AGG_ROWS = []  # filas para persistir results/judge_agreement.csv

for model, paths in MODELS.items():
    print("\n" + "="*72)
    print(f"MODELO: {model}")
    print("="*72)

    judges = {}
    for name, p in paths.items():
        if not p.exists():
            print(f"  [falta] {name}: {p.name}")
            continue
        col = "score" if name == "gpt4o" else "human_score"
        judges[name] = load_scores(p, col)
        print(f"  {name:7} cargado: {len(judges[name])} filas")

    # ids comunes a TODOS los jueces presentes
    common = set.intersection(*[set(j.keys()) for j in judges.values()])
    common = sorted(common)
    print(f"  ids comunes a los {len(judges)} jueces: {len(common)}")

    # tasa de fallo por juez (is_fail = score<2)
    print(f"\n  Tasa de fallo por juez (sobre {len(common)} filas):")
    for name, j in judges.items():
        fails = sum(1 for i in common if j[i][0] < 2)
        print(f"    {name:7}: {fails}/{len(common)} = {100*fails/max(len(common),1):.0f}% fallo")

    # por paso
    steps = sorted({judges[list(judges)[0]][i][1] for i in common})
    print(f"\n  Tasa de fallo por paso:")
    print(f"    {'paso':8}" + "".join(f"{n:>9}" for n in judges))
    for st in steps:
        ids_st = [i for i in common if judges[list(judges)[0]][i][1] == st]
        line = f"    {st:8}"
        for name in judges:
            fails = sum(1 for i in ids_st if judges[name][i][0] < 2)
            line += f"{fails:>3}/{len(ids_st):<5}"
        print(line + f"   (n={len(ids_st)})")

    # acuerdo + kappa por par
    print(f"\n  Acuerdo y Cohen's kappa por par (is_fail binario):")
    for a, b in combinations(judges, 2):
        fa = [1 if judges[a][i][0] < 2 else 0 for i in common]
        fb = [1 if judges[b][i][0] < 2 else 0 for i in common]
        agree = sum(1 for x, y in zip(fa, fb) if x == y)
        k = kappa(fa, fb)
        print(f"    {a:7} vs {b:7}: acuerdo {agree}/{len(common)} = {100*agree/len(common):.0f}%  | kappa = {k:.2f}")
        AGG_ROWS.append({
            "model": model, "judge_a": a, "judge_b": b, "n": len(common),
            "agreement_pct": round(100*agree/len(common), 1), "cohen_kappa": round(k, 3),
        })

    # desacuerdos (al menos un juez difiere en is_fail)
    print(f"\n  Filas con desacuerdo (is_fail):")
    hdr = f"    {'id':14}{'paso':8}" + "".join(f"{n:>8}" for n in judges)
    print(hdr)
    any_d = False
    for i in common:
        fails = {name: (1 if judges[name][i][0] < 2 else 0) for name in judges}
        if len(set(fails.values())) > 1:
            any_d = True
            scores = "".join(f"{judges[name][i][0]:>8}" for name in judges)
            print(f"    {i:14}{judges[list(judges)[0]][i][1]:8}{scores}")
    if not any_d:
        print("    (ninguno — acuerdo total)")

# Persistir la tabla de acuerdo inter-juez (reproducibilidad del kappa del paper)
if AGG_ROWS:
    out = Path("../results/judge_agreement.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(AGG_ROWS[0].keys()))
        w.writeheader()
        w.writerows(AGG_ROWS)
    print(f"\nTabla de acuerdo inter-juez guardada en: {out}")
