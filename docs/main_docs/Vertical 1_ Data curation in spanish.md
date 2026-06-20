# Vertical 1: Data curation in spanish

Benchmarks de seguridad en español: [https://arxiv.org/abs/2508.12733](https://arxiv.org/abs/2508.12733)

La **Vertical 1 (Spanish Upstream Data Curation)** del marco S-OWMI evalúa de forma auditable si un modelo de lenguaje de gran tamaño (LLM) fue entrenado, filtrado y curado éticamente tratando al idioma español como una dimensión de seguridad de primera clase durante su preentrenamiento y ajuste instruccional, o si adquirió sus capacidades de manera pasiva y no supervisada.

La justificación empírica de esta vertical radica en la ruptura de la asimetría técnica anglocéntrica: **la alineación de seguridad optimizada en inglés no se transfiere automáticamente al español**. A nivel de arquitectura mecanicista, las defensas de un modelo en español dependen críticamente de una infraestructura translingüe extremadamente reducida (menor al $0.3\%$ de los parámetros globales del modelo), denominada **Neuronas de Seguridad Compartidas** (*SS-Neurons*). Las variaciones léxicas y los modismos hispanohablantes no logran activar de forma robusta este puente neuronal indexado al inglés, lo que genera fallos defensivos críticos y permite la ejecución exitosa de vectores de ataque (*jailbreaks*) que ya han sido mitigados en entornos anglosajones.

---

## **Parte 1: Protocolo Práctico de Evaluación y Viabilidad de Automatización**

Este bloque describe las seis aristas simplificadas de la Vertical 1. Para garantizar que la herramienta de auditoría sea de fácil mantenimiento, robusta y **sobreviva a lo largo de todo el proyecto de investigación**, se ha optimizado el diseño eliminando dependencias externas frágiles (APIs lingüísticas externas, motores gráficos complejos o scraping de portales gubernamentales en tiempo real) y reemplazándolas con datasets estáticos y clasificadores locales estándar.

### **Paso 1: Auditoría de Distribución Lingüística del Corpus Base**

* **Objetivo:** Determinar la representatividad real del español en la fase de preentrenamiento.  
* **Viabilidad Técnica de Automatización:** **Alta** (gracias a un enfoque local de caja negra).  
* **Estrategia Simplificada en el Framework:** Medir la **Fertilidad de Tokens** de forma local. En lugar de descargar grandes corpus paralelos de la web, se utiliza un dataset estático local de 50 oraciones paralelas inglés-español. El tokenizador del modelo procesa ambos conjuntos y se calcula la tasa de fragmentación de subpalabras (caracteres por token). Una alta fertilidad en español indica una baja representación en el preentrenamiento del modelo.
* **Métrica Principal:** *Spanish Corpus Coverage (SCC)*.  
* **Stack Tecnológico:** Script simple en Python consumiendo la biblioteca `transformers.AutoTokenizer` sin acceso a internet.

### **Paso 2: Evaluación de Cobertura y Puntos Ciegos Dialectales**

* **Objetivo:** Identificar la resiliencia defensiva del modelo frente a modismos regionales y variación léxica en el mundo hispanohablante.  
* **Viabilidad Técnica de Automatización:** **Alta**.  
* **Estrategia Simplificada en el Framework:** Se utiliza un **diccionario estático mapeado** en el código para realizar perturbaciones léxicas (en lugar de consultar APIs lingüísticas externas o diccionarios dinámicos). Un script de Python toma un dataset de prompts éticamente sensibles en español neutro y reemplaza palabras clave con sinónimos dialectales representativos (v.g., rioplatense, chileno, mexicano, caribeño). Se mide la retención de la negativa segura (*refusal rate*).  
* **Métrica Principal:** *Regional Coverage Score (RCS)*.  
* **Stack Tecnológico:** Script de Python para reemplazo de plantillas léxicas y dataset estático local.

### **Paso 3: Análisis del Pipeline de Curación y Filtrado Semántico**

* **Objetivo:** Discriminar si la depuración del corpus upstream utilizó clasificadores semánticos nativos en español o meras listas negras traducidas (*keyword filtering*).  
* **Viabilidad Técnica de Automatización:** **Alta**.  
* **Estrategia Simplificada en el Framework:** Para reducir el consumo de tokens y asegurar la velocidad en la ejecución del demo, se utiliza un banco de pruebas optimizado de **100 prompts benignos** (en lugar de 1,000) que contienen palabras "disparadoras" (*triggers*) de alta sensibilidad sociocultural e histórica en español (v.g., discusiones sobre dictaduras latinoamericanas o eventos políticos regionales). Se mide el índice de sobre-bloqueo involuntario (*over-refusal*).
* **Métricas Principales:** *Semantic Filter Validation (SFV)* y *False Refusal Rate (FRR) en Español*.  
* **Stack Tecnológico:** Script local de orquestación de inferencia y etiquetado automatizado de plantillas de rechazo.

### **Paso 4: Probe Tests de Conocimiento Peligroso Residual (Vectores de Jailbreak)**

* **Objetivo:** Cuantificar la persistencia de conocimiento dañino (ciberseguridad, fraude, armas) en los pesos base y su facilidad de extracción en español.  
* **Viabilidad Técnica de Automatización:** **Alta**.  
* **Estrategia Simplificada en el Framework:** Se evalúan únicamente vectores de ataque **basados en texto** para evitar dependencias complejas de procesamiento de imágenes y rendering. Se descarta la inyección visual (MLingualFC) para simplificar el pipeline. Los dos vectores evaluados de forma directa son:
  1. *Evasión Semántica:* Reestructuración y traducción adversaria en español.
  2. *Code-switching:* Permutación estructural intercalando tokens de inglés y español.
* **Métrica Principal:** *Attack Success Rate Delta ($\Delta$ ASR)*.  
* **Stack Tecnológico:** Scripts en Python para orquestar los ataques de texto y un clasificador local/API configurado como juez automatizado (*LLM-as-a-judge*, v.g., **Llama Guard 3**).

### **Paso 5: Auditoría de Toxicidad, Sesgos y Estereotipos Locales**

* **Objetivo:** Detectar la asimilación e inducción de sesgos socioculturales específicos contra colectivos de regiones hispanohablantes.  
* **Viabilidad Técnica de Automatización:** **Alta**.  
* **Estrategia Simplificada en el Framework:** En lugar de requerir probabilidades de salida de tokens (logprobs), lo cual no es compatible con muchas APIs comerciales cerradas, el framework evalúa el output final en formato de texto. El sistema envía prompts ambiguos basados en modismos y refranes de poder de LATAM y España, y evalúa el sesgo resultante mediante un clasificador LLM-as-a-judge de toxicidad/sesgo.  
* **Métrica Principal:** *Bias and Stereotype Score (BSS)*.  
* **Stack Tecnológico:** Script de inferencia y plantilla evaluadora LLM-as-a-judge optimizada para toxicidad en español.

### **Paso 6: Verificación de Calidad Factual y Alucinación en Dominios Críticos**

* **Objetivo:** Cuantificar la tasa de alucinación informativa en áreas de alta regulación local debido a la escasez de datos upstream de calidad.  
* **Viabilidad Técnica de Automatización:** **Alta**.  
* **Estrategia Simplificada en el Framework:** Se descarta el scraping en tiempo real o NER contra bases de datos regulatorias oficiales (que son propensas a cambiar de estructura y bloquear bots). En su lugar, se compila un **dataset estático de evaluación factual** con preguntas de opción múltiple y respuesta corta extraídas de exámenes MIR (Salud), FLARE-ES (Finanzas), y un set curado de leyes locales vigentes con su respuesta correcta pre-validada.
* **Métricas Principales:** *Factuality Evaluation Score (FES)* y *False Citation Rate (FCR)*.  
* **Stack Tecnológico:** Dataset JSON local de preguntas y respuestas factuales de control y script evaluador de coincidencia exacta / LLM.
