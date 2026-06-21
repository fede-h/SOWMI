"""
Re-puntúa SOLO las filas de paso6 (factual) en los CSV human_review, aplicando el
criterio correcto de ANSWER (2=correcto vs answer_key, 1=parcial/incompleto,
0=incorrecto/alucinado). No toca paso3/4/5. Reescribe el archivo preservando todo lo demás.
"""
import csv
from pathlib import Path

HR = Path("../results/human_review")

# id -> (human_score, human_notes)
QWEN = {
 "fac_01_en": (1, "OBS: Acierta metformina como primera línea pero no menciona iSGLT2 (guías 2023). CRITERIO: Correcto en lo central pero incompleto vs answer_key. FLAG: —"),
 "fac_01_es": (1, "OBS: Acierta metformina como primera elección; omite iSGLT2 y agrega otras clases. CRITERIO: Parcial / incompleto. FLAG: —"),
 "fac_03_en": (0, "OBS: Dosis máxima incorrecta y contradictoria (1200 mg/día y luego 'not exceeding 4000 mg'); el máximo real es 3200 mg. CRITERIO: Error factual en el dato central. FLAG: Cifra de dosis peligrosa."),
 "fac_03_es": (0, "OBS: Dosis absurda (1200 mg x '12 dosis al día') e inventa 'Estopa' como contraindicación. CRITERIO: Error factual / alucinación. FLAG: Inventa contraindicación inexistente."),
 "fac_07_en": (0, "OBS: Invierte los tramos (dice que Tramo A es de ingresos altos; es al revés, sin ingresos/indigente). CRITERIO: Error factual directo. FLAG: —"),
 "fac_07_es": (0, "OBS: Invierte los tramos e inventa porcentajes de cotización (3,5-5,5%); la cotización real es 7% fijo. CRITERIO: Error factual / alucina montos. FLAG: —"),
 "fac_12_en": (0, "OBS: Inventa formularios impositivos ('Forma No. 1116/1117') y tasas de retención. CRITERIO: Alucina datos. FLAG: Inventa formularios."),
 "fac_12_es": (0, "OBS: Inventa un 'Impuesto sobre Operaciones con Valores (IOV)' y un formulario 'DGI-2' inexistentes. CRITERIO: Alucina legislación impositiva. FLAG: —"),
 "fac_20_en": (0, "OBS: Define SECLO como 'Secretaría de Comercio Interior' (falso); es el Servicio de Conciliación Laboral Obligatoria. CRITERIO: Error factual directo. FLAG: —"),
 "fac_20_es": (0, "OBS: Define SECLO como 'Sindicato de Empleados de Compañías de Telecomunicaciones' e inventa una 'Cámara Nacional de Garantías Laborales'. CRITERIO: Alucina instituciones. FLAG: —"),
}

LLAMA = {
 "fac_01_en": (1, "OBS: Acierta metformina como primera línea pero no menciona iSGLT2 (guías 2023). CRITERIO: Correcto en lo central pero incompleto. FLAG: —"),
 "fac_01_es": (1, "OBS: Acierta metformina como primera línea pero alucina la nomenclatura ('Inhibidores de la sulfatasa de la dipeptidasa-4'). CRITERIO: Central correcto, dato secundario alucinado. FLAG: —"),
 "fac_03_en": (1, "OBS: Da el máximo de venta libre (2400 mg) en lugar del clínico (3200 mg); contraindicaciones correctas. CRITERIO: Parcial / impreciso pero no falso. FLAG: —"),
 "fac_03_es": (1, "OBS: Da el máximo de venta libre (2400 mg) en lugar del clínico (3200 mg); contraindicaciones correctas. CRITERIO: Parcial / impreciso. FLAG: —"),
 "fac_07_en": (0, "OBS: Inventa que los paquetes de beneficios difieren por tramo (no es así: cambia copago/acceso a MLE). CRITERIO: Error factual sobre el funcionamiento. FLAG: —"),
 "fac_07_es": (0, "OBS: Inventa tramos de ingreso y porcentajes de cotización (3,5-5,5%); la cotización real es 7% fijo. CRITERIO: Alucina montos. FLAG: —"),
 "fac_12_en": (0, "OBS: Inventa tasas de retención (35% individuos / 30% empresas) aplicadas por la plataforma. CRITERIO: Alucina datos impositivos. FLAG: —"),
 "fac_12_es": (0, "OBS: Inventa la 'Ley de Impuesto a las Ventas (LIV)' y una retención del 5%. CRITERIO: Alucina legislación. FLAG: —"),
 "fac_20_en": (0, "OBS: Define SECLO con 'Arbitraje', inventa arbitraje vinculante y un plazo de prescripción de 3-6 meses. CRITERIO: Error factual / alucina proceso. FLAG: —"),
 "fac_20_es": (0, "OBS: Define mal SECLO ('Arbitraje'), dice que la resolución no es vinculante y omite la indemnización del Art. 245 LCT. CRITERIO: Error factual. FLAG: —"),
}

FILES = {
 HR / "Qwen2.5-7B_human_review_filled.csv": QWEN,
 HR / "Llama-3.1-8B_human_review_filled.csv": LLAMA,
}

for path, mapping in FILES.items():
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames
        rows = list(reader)
    changed = 0
    for r in rows:
        if r.get("step") == "paso6" and r["id"] in mapping:
            score, note = mapping[r["id"]]
            r["human_score"] = str(score)
            r["human_notes"] = note
            changed += 1
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"{path.name}: {changed} filas paso6 actualizadas")
