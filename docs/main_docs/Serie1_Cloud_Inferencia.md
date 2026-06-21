# Serie 1 — Cómo correr la inferencia en la nube (repartida entre todos)

**Objetivo:** que ninguna máquina sola cargue toda la inferencia. Repartimos los 2 modelos × 2 idiomas entre el equipo, usando GPUs gratuitas en la nube.

**Workload total:** 2 modelos (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct) × 200 prompts c/u (100 EN + 100 ES) ≈ 400 inferencias. Es **chico**: ~30–90 min por bloque de 100 prompts en una GPU T4 gratis.

---

## TL;DR (recomendación)

**Gratis y de sobra: Kaggle (principal) + Colab (secundario), en 4-bit, con `transformers`.** Split por **modelo × idioma** → 4 bloques independientes + 1 integrador. Acepten **ya** la licencia de Llama-3.1 en HuggingFace (tarda en aprobarse). Si lo gratis se complica, **together.ai** da $25 de crédito y resuelve las 400 inferencias por menos de $1 sin tocar GPUs.

---

## 1. Cuadro diferencial — dónde correr

| Criterio | (a) Laptop solo CPU | (b) Laptop GPU 6–8 GB | (c) Cloud gratis T4 (Colab/Kaggle) | (d) Cloud pago barato (RunPod/Vast) |
|---|---|---|---|---|
| **¿Sirve para 7-8B?** | Sí, pero lentísimo | Solo en **4-bit** | **Sí** ✅ | **Sí, cómodo** |
| **Tiempo ~100 prompts** | **Horas (3–10 h+)** | ~1–2 h (4-bit) | **~30–90 min** | **~15–40 min** |
| **VRAM / cuantización** | usa RAM, fp32/fp16, muy lento | **4-bit obligatorio** | **4-bit recomendado** (fp16 va al límite, OOM) | fp16 si ≥24 GB; si no 4-bit |
| **Coste** | $0 | $0 | **$0** | **<$1 total** |
| **Fricción de setup** | baja (pero penoso esperar) | media (CUDA, bitsandbytes) | **baja** (notebook + GPU 1 click) | media (cuenta, pod, SSH) |
| **Límites** | ninguno | ninguno | Colab: idle ~90 min, ~12 h máx, cuota variable · Kaggle: **30 h/sem**, ~12 h/sesión, **background** | pagás aunque esté idle |
| **Mejor uso** | solo smoke test 2-3 prompts | quien ya tenga RTX en la laptop | **caso base del equipo** | si se agota lo gratis o se necesita velocidad |

**Conclusión:** correr local en CPU es inviable para 100 prompts (horas). **Usamos cloud gratis (Kaggle/Colab T4).**

---

## 2. Por qué Kaggle primero

- **30 h de GPU por semana garantizadas** (cuota visible), por persona.
- **Ejecución en background**: sigue corriendo aunque cierres la pestaña → no se pierde el trabajo por desconexión (el gran problema de Colab).
- GPU **T4 ×2** (32 GB combinados) o **P100 16 GB**.

Colab usa la misma T4 16 GB pero corta por inactividad (~90 min) y tiene cuotas variables no publicadas → lo usamos como segunda máquina.

---

## 3. Reparto entre 4–5 personas (split por modelo × idioma)

| Persona | Tarea | Plataforma | Output |
|---|---|---|---|
| **P1** | Qwen2.5-7B — **100 EN** | Kaggle (T4) | `results/raw/Qwen2.5-7B-Instruct_en_responses.csv` |
| **P2** | Qwen2.5-7B — **100 ES** | Kaggle o Colab | `results/raw/Qwen2.5-7B-Instruct_es_responses.csv` |
| **P3** | Llama-3.1-8B — **100 EN** | Kaggle (T4) | `results/raw/Llama-3.1-8B-Instruct_en_responses.csv` |
| **P4** | Llama-3.1-8B — **100 ES** | Colab (T4) | `results/raw/Llama-3.1-8B-Instruct_es_responses.csv` |
| **P5** | Merge de los 4 CSV + `judge.py` | Laptop (sin GPU si judge = reglas) | scores + scorecard |

**Por qué modelo × idioma:** cada persona **carga un solo modelo** (una descarga, gating de Llama solo para P3/P4), bloques cortos (~30–90 min), y los 4 CSV son disjuntos → **merge sin conflictos**. El script ya soporta `--lang` y nombra el archivo con el sufijo del idioma, así que no se pisan.

---

## 4. Receta lista para pegar (celda de Colab / Kaggle)

```python
# 1. Instalar dependencias
!pip install -q transformers torch accelerate sentencepiece bitsandbytes

# 2. Traer el repo (o subir prompts.csv + run_inference.py a mano)
!git clone https://github.com/fede-h/SOWMI.git
%cd SOWMI/code

# 3. (Solo P3/P4, Llama) login a HuggingFace con tu token (acepta antes la licencia en la web)
# from huggingface_hub import login; login("hf_tu_token")

# 4. Correr TU bloque. Cambiá --model y --lang según tu asignación:
#    P1: --model Qwen/Qwen2.5-7B-Instruct  --lang en
#    P2: --model Qwen/Qwen2.5-7B-Instruct  --lang es
#    P3: --model meta-llama/Llama-3.1-8B-Instruct  --lang en
#    P4: --model meta-llama/Llama-3.1-8B-Instruct  --lang es
!python run_inference.py \
    --model Qwen/Qwen2.5-7B-Instruct \
    --prompts ../prompts/prompts.csv \
    --lang en \
    --load-in-4bit \
    --max-new-tokens 512

# 5. Descargar el CSV resultante de ../results/raw/ y subirlo al repo (o pasárselo a P5)
```

**Importante:** usen siempre `--load-in-4bit` en la T4 (sin esto, fp16 da out-of-memory).

---

## 5. Gotchas (leer antes de correr)

- **fp16 NO entra en la T4 16 GB.** Un 7-8B en fp16 son ~15-16 GB solo de pesos; con el KV cache da **OOM**. Por eso `--load-in-4bit` (baja a ~5-6 GB, calidad ≈96% de fp16 y para greedy decoding la diferencia es mínima).
- **Llama-3.1 está gated.** Hay que: (1) cuenta HF, (2) **aceptar la licencia Meta** en la página del modelo, (3) esperar aprobación (minutos a un par de días → **háganlo YA**), (4) crear un **token Read** y loguearse. **Qwen2.5 no está gated** → empiecen por Qwen mientras esperan Llama.
- **No usar vLLM acá.** Para 200 prompts secuenciales la ganancia es marginal y mete más fricción + OOM en T4. `transformers` plain alcanza.
- **Judge sin GPU:** `judge.py --rule-based` corre en cualquier laptop, gratis. Si quieren más señal, GPT-4o vía API (también sin GPU). **Eviten Llama Guard 3 como juez** salvo necesidad: es ~8B y necesitaría otra GPU.
- **Guarden incremental:** si una sesión se cae, no perder todo. (El script guarda al final; para bloques largos conviene bajar el CSV apenas termina.)

---

## 6. Reglas para que el merge salga limpio (P5)

- **Schema de CSV idéntico** (ya lo garantiza `run_inference.py`: mismas columnas).
- **Nombres de archivo únicos** por persona (el sufijo `_en`/`_es` ya los separa).
- Cada quien commitea **solo su CSV**; P5 concatena y corre `judge.py` sobre cada modelo (juntando EN+ES del mismo modelo) → `stats.py` → `score_scorecard.py`.

---

## Plan B (si lo gratis falla): together.ai
$25 de crédito al registrarse, sirve Qwen2.5-7B y Llama-3.1-8B por API. 400 inferencias ≈ 240k tokens → **<$1**. Cero GPU, cero descargas, cero gating. Costo: hay que adaptar `run_inference.py` a llamadas API en vez de `transformers` local (cambio chico).
