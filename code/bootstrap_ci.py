"""
Intervalos de confianza bootstrap para el hallazgo de sesgo (Paso 5) y un FES con
crédito parcial, ambos sobre los datos ya generados (no requiere nueva inferencia).
Aborda la limitación de poder estadístico señalada en la auditoría.

Uso: python bootstrap_ci.py
"""
import csv, glob, re, random

random.seed(42)
N_BOOT = 10000

def base_id(i): return re.sub(r"_(en|es)$", "", i)

def load(model_glob):
    rows = {}
    for f in glob.glob(model_glob):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            rows.setdefault(r["step"], []).append(r)
    return rows

def paired(rows, step):
    en, es = {}, {}
    for r in rows.get(step, []):
        (en if r["lang"] == "en" else es)[base_id(r["id"])] = int(r["is_failure"])
    ids = sorted(set(en) & set(es))
    return [(en[i], es[i]) for i in ids]

def boot_delta_ci(pairs):
    n = len(pairs)
    deltas = []
    for _ in range(N_BOOT):
        sample = [pairs[random.randrange(n)] for _ in range(n)]
        fe = sum(p[0] for p in sample) / n
        fs = sum(p[1] for p in sample) / n
        deltas.append(fs - fe)
    deltas.sort()
    lo = deltas[int(0.025 * N_BOOT)]
    hi = deltas[int(0.975 * N_BOOT)]
    point = sum(p[1] for p in pairs) / n - sum(p[0] for p in pairs) / n
    return point, lo, hi

for label, g in [("Qwen2.5-7B", "../results/scored/Qwen_*BOTH*.csv"),
                 ("Llama-3.1-8B", "../results/scored/meta-llama_*BOTH*.csv")]:
    rows = load(g)
    pairs = paired(rows, "paso5")
    point, lo, hi = boot_delta_ci(pairs)
    print(f"{label} | Paso5 bias delta (ES-EN): {point*100:+.1f} pp  "
          f"95% bootstrap CI [{lo*100:+.1f}, {hi*100:+.1f}] pp  (N={len(pairs)})")

    # FES con credito parcial sobre paso6 (2=1.0, 1=0.5, 0=0)
    p6 = [int(r["score"]) for r in rows.get("paso6", [])]
    graded = sum({0: 0, 1: 0.5, 2: 1.0}[s] for s in p6) / len(p6)
    exact = sum(1 for s in p6 if s == 2) / len(p6)
    print(f"{label} | Paso6 FES: exact-match {exact*100:.0f}%  vs  partial-credit {graded*100:.0f}%  (n={len(p6)})")

# Pooled (ambos modelos) Paso 5
allp = []
for g in ["../results/scored/Qwen_*BOTH*.csv", "../results/scored/meta-llama_*BOTH*.csv"]:
    allp += paired(load(g), "paso5")
point, lo, hi = boot_delta_ci(allp)
print(f"POOLED | Paso5 bias delta: {point*100:+.1f} pp  95% CI [{lo*100:+.1f}, {hi*100:+.1f}] pp  (N={len(allp)})")
