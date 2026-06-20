# Literatura relacionada — qué agregar al paper y por qué

Este documento lista los trabajos existentes que deben citarse en el paper del equipo (Spanish Safety Maturity Framework) y en el paper personal de investigación. Para cada uno se explica qué aportan y exactamente qué frase/sección justifican.

---

## M-ALERT (2024)

**Qué es:** Paper que evaluó seguridad en 5 idiomas europeos: inglés, francés, alemán, italiano y español (castellano). Demostró que los modelos muestran alta inconsistencia de seguridad al cambiar de idioma — el mismo prompt dañino puede ser rechazado en inglés y cumplido en español.

**Por qué lo necesitamos:** Es la evidencia más directa de que el problema que nosotros investigamos ya fue documentado en Europa. Nosotros lo extendemos a español latinoamericano, donde nunca se hizo.

**Qué dice exactamente para nosotros:** Que incluso en español "estándar" (europeo) ya hay gaps de seguridad. En español latinoamericano, con menor representación en los datos de entrenamiento y safety alignment, la situación es potencialmente peor — pero nadie lo midió.

**Dónde va en el paper:**
- Introducción: como motivación del problema ("M-ALERT demostró X en Europa; nosotros extendemos esto a LATAM")
- Background: como trabajo previo en evaluación multilingüe de seguridad
- También en el paper personal de Nico, como evidencia de que el gap de traducción/perfiles existe comportamentalmente

---

## LinguaSafe

**Qué es:** Benchmark de seguridad en 12 idiomas con 45.000 instancias. Usa niveles de severidad L0 (consultas benignas que no debería rechazar) a L3 (daño severo que siempre debería rechazar). Incluye over-sensitivity testing — mide también cuándo el modelo rechaza cosas que no debería.

**Por qué lo necesitamos:** Es el trabajo más parecido a lo que hacemos. Cualquier revisor lo va a conocer y va a preguntar en qué nos diferenciamos.

**Qué nos falta de LinguaSafe que nosotros cubrimos:**
- No incluye español latinoamericano (sus idiomas son húngaro, malayo, ruso, serbio, tailandés, coreano, vietnamita, checo, bengalí, árabe, chino e inglés)
- No tiene variantes dialectales (no distingue variantes regionales del mismo idioma)
- No produce un score organizacional — no le dice a una institución si puede confiar en el modelo
- No conecta con gobernanza de open-weight models

**Dónde va en el paper:**
- Background del paper del equipo: mención directa + tabla comparativa con nuestra contribución
- Paper personal de Nico: citarlo como "benchmark más cercano" y articular las diferencias como brecha que justifica la investigación

---

## "Spanish Is Not Just One"

**Qué es:** Dataset de 30 preguntas validadas por lingüistas, distribuidas en 7 variantes del español (Andina, Antillana, Chilena, Caribeña Continental, Mexicana/Centroamericana, Peninsular, Rioplatense). Demuestra que los modelos tienen preferencia implícita por el español peninsular estándar y tratan distinto cada variante.

**Por qué lo necesitamos:** Valida empíricamente que la distinción entre variantes regionales del español no es caprichosa — hay evidencia de que los modelos se comportan diferente en español rioplatense, mexicano o andino. Justifica que nuestros tests incluyan variantes regionales en lugar de un español genérico.

**Qué dice exactamente para nosotros:** Los modelos tienen un "español por defecto" que favorece la variante peninsular. Esto implica que testear solo en español neutro subestima los gaps de seguridad en variantes LATAM.

**Dónde va en el paper:**
- Paper del equipo: mención en Background como justificación de incluir variantes dialectales en el protocolo de evaluación. No expandirse — solo citarlo.
- Paper personal de Nico: citarlo como evidencia de que los perfiles lingüísticos varían por variante regional, lo que refuerza la Hipótesis B (perfiles distintos).

---

## PolygloToxicityPrompts (PTP)

**Qué es:** 425.000 prompts en 17 idiomas, tomados de texto real de internet (no traducidos). Mide toxicidad generada por modelos cuando autocompletan texto. Encontró que la toxicidad sube en idiomas con menos datos de calidad, y que en modelos sin instruction-tuning escala con el tamaño del modelo.

**Por qué lo necesitamos:** Complementa a M-ALERT y LinguaSafe con evidencia de que los gaps de seguridad están correlacionados con la densidad de datos de entrenamiento en cada idioma. Refuerza el argumento de Vertical 1 (Data Curation) del framework.

**Dónde va en el paper:**
- Background del paper del equipo: para justificar Vertical 1 (curaduría de datos en español)
- Una mención es suficiente. No expandirse.

---

## MultiJail / Marx & Dunaiski (2026)

**Qué es:** Demostró que las tasas de jailbreak suben de 59.8% a 75.8% promedio cuando los ataques se hacen en idiomas distintos al inglés, usando multi-turn red-teaming humano. Específicamente, Claude 3.5 Haiku mostró 52.7% de éxito y GPT-4o-mini 83.6% cuando se los ataca en otros idiomas.

**Por qué lo necesitamos:** Es el número más citado en la literatura sobre jailbreak multilingüe. Establece el baseline cuantitativo del problema. Nosotros aplicamos el mismo razonamiento al español LATAM específicamente.

**Dónde va en el paper:**
- Introducción y Background de ambos papers: es la cita de apertura que establece que el problema es real y medible.

---

## Resumen de uso por sección

| Trabajo | Intro del paper equipo | Background equipo | Paper Nico |
|---|---|---|---|
| M-ALERT | ✅ Motivación central | ✅ Related work | ✅ Evidencia de gap |
| LinguaSafe | — | ✅ Comparación directa | ✅ Diferenciación |
| Spanish Is Not Just One | — | ✅ Justifica variantes | ✅ Evidencia Hipótesis B |
| PolygloToxicityPrompts | — | ✅ Justifica Vertical 1 | — |
| MultiJail / Marx & Dunaiski | ✅ Número clave | ✅ Related work | ✅ Baseline cuantitativo |
