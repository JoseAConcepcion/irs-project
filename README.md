# Proyecto Final de Sistemas de Recuperación de Información

## Integrantes
- Alejandro García González C-311 [Github](https://github.com/ajper256)
- Ernesto Alejandro Bárcena Trujillo C-311 [Github](https://github.com/Barccena05)
- José Antonio Concepción Álvarez C-311 [Github](https://github.com/JoseAConcepcion)

---

## Informe sobre el repositorio: JoseAConcepcion/irs-project

### Descripción general
Este repositorio corresponde al proyecto final de la asignatura Sistemas de Recuperación de Información (IRS) y está desarrollado principalmente en Python. El proyecto implementa una aplicación de escritorio que permite analizar y rankear reseñas de productos de manera inteligente y personalizada.

### Propósito del proyecto según el código
El proyecto consiste en una aplicación de escritorio que permite cargar intereses de usuario y reseñas de productos, analizar dichas reseñas y rankearlas según diferentes criterios seleccionables por el usuario. Utiliza la biblioteca Tkinter para la interfaz gráfica. Los criterios de análisis incluyen votos de utilidad, complejidad sintáctica del texto, diversidad léxica y longitud del comentario.

El sistema también extrae características relevantes de los productos mencionados en las reseñas usando modelos generativos (Gemini API), y permite identificar cuáles características pueden ser de mayor interés para el usuario según sus preferencias.

### Funciones principales

#### 1. Carga de datos
- **Cargar datos del usuario e intereses**: Permite importar archivos de texto (.txt) con los intereses del usuario
- **Cargar reseñas de productos**: Soporta archivos en formato JSONL con reseñas que incluyen rating, texto, votos de utilidad, ASIN del producto, etc.

#### 2. Análisis y ranking de reseñas
- **Análisis por votos de utilidad**: Ranking basado en la cantidad de votos útiles que ha recibido cada reseña
- **Análisis de estructura textual**: Evaluación de la complejidad sintáctica y diversidad léxica del texto usando técnicas de procesamiento de lenguaje natural con SpaCy
- **Análisis por longitud**: Consideración de la extensión del comentario como factor de ranking
- **Ranking combinado**: Posibilidad de combinar múltiples criterios de análisis

#### 3. Interfaz gráfica intuitiva
- **Vista 1 (Carga de datos)**: Interfaz para cargar datos de usuario y reseñas
- **Vista 2 (Análisis y resultados)**: Visualización de resultados con opciones de filtrado y ordenamiento
- **Búsqueda con autocompletado**: Sistema de búsqueda con sugerencias automáticas usando estructura de datos Trie
- **Selección de criterios**: Checkboxes para seleccionar qué criterios incluir en el análisis

#### 4. Extracción de características con IA
- **Integración con Gemini API**: Utiliza modelos generativos de Google para extraer características relevantes de productos
- **Análisis de características personalizadas**: Identifica qué características de productos son más relevantes según los intereses del usuario

### Arquitectura técnica

#### Estructura del proyecto
```
src/
├── main.py                     # Aplicación principal con Tkinter
├── vistas/
│   ├── vista1.py              # Interfaz de carga de datos
│   └── vista2.py              # Interfaz de análisis y resultados
├── data_processing/
│   ├── load.py               # Carga y procesamiento de archivos JSONL
│   ├── quantify.py           # Algoritmos de ranking y puntuación
│   ├── analyze.py            # Análisis textual (complejidad sintáctica, diversidad léxica)
│   └── feature_extraction.py # Extracción de características con Gemini API
└── data_structure/
    └── trie.py               # Estructura de datos para autocompletado
```

#### Algoritmos de análisis implementados

1. **Complejidad sintáctica**: Análisis basado en:
   - Número de cláusulas principales (peso: 3)
   - Número de cláusulas secundarias (peso: 2)
   - Modificadores adjetivales (peso: 1)
   - Frases preposicionales (peso: 1.5)

2. **Diversidad léxica**: Calculada usando entropía de Shannon sobre los lemas del texto, excluyendo palabras vacías

3. **Ranking compuesto**: Combina múltiples métricas normalizadas para generar una puntuación final

### Dependencias y tecnologías

#### Dependencias principales
- **tkinter**: Interfaz gráfica de usuario (GUI)
- **pandas**: Manipulación y análisis de datos
- **spacy**: Procesamiento de lenguaje natural y análisis textual
- **google-generativeai**: Integración con API de Gemini para extracción de características
- **demoji**: Procesamiento de emojis en texto
- **protobuf**: Serialización de datos para APIs de Google

#### Modelos requeridos
- **en_core_web_sm**: Modelo de SpaCy para análisis de texto en inglés

### Flujo de uso

1. **Inicio**: El usuario lanza la aplicación que muestra la vista de carga de datos
2. **Carga de intereses**: Importa un archivo .txt con sus intereses personales
3. **Carga de reseñas**: Selecciona un archivo .jsonl con reseñas de productos
4. **Configuración de análisis**: Selecciona qué criterios incluir en el ranking (votos útiles, análisis textual, longitud)
5. **Visualización de resultados**: Revisa las reseñas ordenadas según los criterios seleccionados
6. **Búsqueda y filtrado**: Utiliza la búsqueda con autocompletado para encontrar reseñas específicas
7. **Análisis de características**: Opcionalmente analiza las características más relevantes de productos específicos

### En resumen
El proyecto ayuda al usuario a analizar reseñas de productos y destacar las más relevantes, personalizando el análisis según sus intereses y diferentes criterios de evaluación. Combina técnicas tradicionales de procesamiento de texto con inteligencia artificial generativa para proporcionar insights valiosos sobre productos y reseñas.
