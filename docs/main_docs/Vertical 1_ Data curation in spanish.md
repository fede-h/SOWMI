# Vertical 1: Data curation in spanish

Benchmarks de seguridad en español: [https://arxiv.org/abs/2508.12733](https://arxiv.org/abs/2508.12733)

La **Vertical 1 (Spanish Upstream Data Curation)** del marco S-OWMI evalúa de forma auditable si un modelo de lenguaje de gran tamaño (LLM) fue entrenado, filtrado y curado éticamente tratando al idioma español como una dimensión de seguridad de primera clase durante su preentrenamiento y ajuste instruccional, o si adquirió sus capacidades de manera pasiva y no supervisada.

La justificación empírica de esta vertical radica en la ruptura de la asimetría técnica anglocéntrica: **la alineación de seguridad optimizada en inglés no se transfiere automáticamente al español**. A nivel de arquitectura mecanicista, las defensas de un modelo en español dependen críticamente de una infraestructura translingüe extremadamente reducida (menor al $0.3\\%$ de los parámetros globales del modelo), denominada **Neuronas de Seguridad Compartidas** (*SS-Neurons*). Las variaciones léxicas y los modismos hispanohablantes no logran activar de forma robusta este puente neuronal indexado al inglés, lo que genera fallos defensivos críticos y permite la ejecución exitosa de vectores de ataque (*jailbreaks*) que ya han sido mitigados en entornos anglosajones.

## **Parte 1: Protocolo Práctico de Evaluación y Viabilidad de Automatización**

Este bloque operativo describe las seis aristas mandatorias de la Vertical 1, analizando su viabilidad técnica real de automatización para construir una herramienta de auditoría perimetral corporativa.

### **Paso 1: Auditoría de Distribución Lingüística del Corpus Base**

* **Objetivo:** Determinar la representatividad real del español en la fase de preentrenamiento.  
* **Viabilidad Técnica de Automatización:** **Baja/Media** (debido a la opacidad corporativa y la retención de datos en modelos cerrados o comerciales).  
* **Estrategia de Automatización en el Framework:** Implementar un pipeline automatizado basado en el **Análisis de Tokenización Comparativa (Fertilidad de Tokens)**. El sistema envía en lote un corpus estandarizado multilingüe (v.g., fragmentos paralelos de Wikipedia) en inglés y español. El tokenizador del modelo procesa ambos conjuntos y calcula la tasa de compresión (caracteres por token). Una alta fertilidad de tokens en español (mayor fragmentación de subpalabras) correlaciona matemáticamente con un vocabulario no optimizado y una baja representación en el preentrenamiento.  
* **Métrica Principal:** *Spanish Corpus Coverage (SCC)*.  
* **Stack Tecnológico:** Scripts en Python consumiendo la biblioteca transformers.AutoTokenizer.

### **Paso 2: Evaluación de Cobertura y Puntos Ciegos Dialectales**

* **Objetivo:** Identificar la resiliencia defensiva del modelo frente a la diversidad lingüística y modismos regionales del mundo hispanohablante.  
* **Viabilidad Técnica de Automatización:** **Alta**.  
* **Estrategia de Automatización en el Framework:** Programar un script que extraiga un dataset base de *prompts* éticamente sensibles o dañinos escritos en español neutro. El pipeline se conecta mediante API a un diccionario de variación léxica regional de los 21 países hispanohablantes. El script aplica perturbaciones sintácticas automáticas sustituyendo los términos neutros por modismos locales (v.g., rioplatense, chileno, caribeño) o combinaciones de *Spanglish*. Posteriormente, se evalúa en lote la tasa de retención de la negativa segura (*refusal rate*).  
* **Métrica Principal:** *Regional Coverage Score (RCS)*.  
* **Stack Tecnológico:** Dataset de variaciones idiomáticas locales acoplado a clasificadores probabilísticos.

### **Paso 3: Análisis del Pipeline de Curación y Filtrado Semántico**

* **Objetivo:** Discriminar si la depuración del corpus upstream utilizó clasificadores semánticos nativos en español o meras listas negras traducidas (*keyword filtering*).  
* **Viabilidad Técnica de Automatización:** **Alta** (evaluada a través de respuestas en la capa de inferencia).  
* **Estrategia de Automatización en el Framework:** El módulo automatiza la inyección masiva de 1,000 *prompts* benignos que contienen intencionalmente palabras "disparadoras" o *triggers* de alta sensibilidad cultural, histórica, política o social del contexto hispanohablante (v.g., discusiones sobre dictaduras latinoamericanas o terminología de desintoxicación de discursos de odio). Los modelos que dependen de heurísticas de filtrado anglosajonas traducidas muestran un comportamiento sesgado de sobre-bloqueo (*over-refusal*). El script procesa las respuestas del modelo para identificar falsos positivos defensivos.  
* **Métricas Principales:** *Semantic Filter Validation (SFV)* y *False Refusal Rate (FRR) en Español*.  
* **Stack Tecnológico:** Scripts automatizados de escaneo de cadenas de texto (*string matching*) para clasificar plantillas estandarizadas de rechazo involuntario.

### **Paso 4: Probe Tests de Conocimiento Peligroso Residual (Vectores de Jailbreak)**

* **Objetivo:** Cuantificar la persistencia de conocimiento dañino (ciberseguridad, fraude, armas biológicas, violencia) en los pesos base y su facilidad de extracción en español.  
* **Viabilidad Técnica de Automatización:** **Alta** (los ataques adversariales en lote son parametrizables).  
* **Estrategia de Automatización en el Framework:** Construir un motor de orquestación adversarial que transforme automáticamente directrices dañinas bajo tres vectores específicos:  
  1. *Evasión Semántica:* Traducción y reestructuración de la consulta en lógica formal en español.  
  2. *Code-switching:* Permutación estructural intercalando fragmentos de tokens en inglés, español y dialectos locales dentro del mismo prompt.  
  3. *Inyección Visual (MLingualFC):* Conversión automatizada del texto malicioso en imágenes que contienen diagramas de flujo estructurados utilizando scripts latinos y caracteres en español.  
* **Métrica Principal:** *Attack Success Rate Delta ($\\Delta$ ASR)*.  
* **Stack Tecnológico:** Librerías de renderizado gráfico (matplotlib/Graphviz) integradas con un clasificador perimetral configurado como juez automatizado (*LLM-as-a-judge*, v.g., **Llama Guard 3** o clasificadores basados en el corpus *Celadon*) para etiquetar de forma binaria el éxito del ataque.

### **Paso 5: Auditoría de Toxicidad, Sesgos y Estereotipos Locales**

* **Objetivo:** Detectar la asimilación e inducción de sesgos socioculturales específicos contra colectivos de regiones hispanohablantes.  
* **Viabilidad Técnica de Automatización:** **Alta**.  
* **Estrategia de Automatización en el Framework:** Automatizar la ingesta masiva de prompts ambiguos basados en dichos populares, refranes y modismos estructurados bajo dinámicas de poder de América Latina y España. El framework realiza llamadas de inferencia en paralelo y recopila los outputs generados bajo escenarios discriminatorios.  
* **Métrica Principal:** *Bias and Stereotype Score (BSS)*.  
* **Stack Tecnológico:** Adaptación de la lógica del framework **SESGO**, programando la medición estadística automática de la entropía de los tokens de salida asociados a categorías de género, etnia, nivel socioeconómico y origen nacional.

### **Paso 6: Verificación de Calidad Factual y Alucinación en Dominios Críticos**

* **Objetivo:** Cuantificar la tasa de alucinación informativa en áreas altamente reguladas locales debido a la escasez de datos upstream de alta calidad o al sobreajuste instruccional.  
* **Viabilidad Técnica de Automatización:** **Alta**.  
* **Estrategia de Automatización en el Framework:** Lanzar evaluaciones automatizadas de opción múltiple y respuesta estructurada utilizando bancos de preguntas regionales en las siguientes verticales hispanohablantes:  
  * *Salud:* Histórico de los exámenes médicos oficiales de postgrado **MIR**.  
  * *Finanzas:* Tareas financieras y de mercado extraídas del benchmark **FLARE-ES**.  
  * *Derecho y Administración Pública:* Extracción automática de entidades normativas locales mediante scripts de Reconocimiento de Entidades Nombradas (NER) y verificación cruzada contra bases de datos regulatorias oficiales para calcular de forma matemática la invención de leyes o artículos apócrifos.  
* **Métricas Principales:** *Factuality Evaluation Score (FES)* y *False Citation Rate (FCR)*.  
* **Stack Tecnológico:** Pipelines de procesamiento de lenguaje natural integrados con herramientas de concordancia factual (v.g., *TruthfulQA-Multi* optimizado para el cálculo automatizado del índice *Kappa de Cohen*).

