# Proyecto Final de Sistemas de Recuperación de Información

## Integrantes
- Alejandro García González C-311 [Github](https://github.com/ajper256)
- Ernesto Alejandro Bárcena Trujillo C-311 [Github](https://github.com/Barccena05)
- José Antonio Concepción Álvarez C-311 [Github](https://github.com/JoseAConcepcion)

---

## Informe corto sobre el proyecto

Este proyecto implementa una aplicación de análisis y ranking de reseñas de productos utilizando una interfaz gráfica en Tkinter y procesamiento inteligente de texto. Permite la carga de datos de reseñas y de intereses de usuario, y utiliza modelos de inteligencia artificial (Gemini API) para extraer características relevantes de los productos mencionados en los comentarios.

Las funcionalidades principales incluyen:

- **Carga y visualización de reseñas:** El usuario puede seleccionar archivos con reseñas y ver los datos cargados.
- **Ranking de reseñas:** Se pueden ordenar las reseñas por utilidad, estructura de texto, longitud y otros criterios.
- **Extracción de features:** El sistema analiza los comentarios y extrae las características principales de los productos utilizando IA generativa.
- **Personalización por intereses:** Relaciona los intereses del usuario con las features extraídas para recomendar productos o identificar elementos de mayor relevancia.
- **Interfaz amigable:** El flujo de la aplicación permite pasar entre diferentes vistas y actualizar los rankings en tiempo real.

El código emplea clases como `Quantify` para calcular los rankings y realizar análisis de texto, y utiliza la clase `feature_extractor` para obtener las características relevantes desde los comentarios. Además, integra un sistema de autocompletado y sugerencias basado en estructura Trie.

En resumen, el proyecto está orientado a mejorar la recuperación y recomendación de información sobre productos a partir del análisis inteligente de reseñas y preferencias de los usuarios.