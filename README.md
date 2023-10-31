# Proyecto de Recomendación de Videojuegos para Steam

## Descripción del Problema

**Contexto:** Como Data Scientist en Steam, una plataforma multinacional de videojuegos, enfrentamos el desafío de crear un sistema de recomendación de videojuegos para usuarios. Aunque nuestro modelo de recomendación ha arrojado métricas prometedoras, ahora debemos llevarlo al mundo real y enfrentar problemas de madurez en los datos y la falta de automatización en los procesos.

**Rol a Desarrollar:** Como Data Scientist en Steam, nuestra misión es diseñar un sistema de recomendación de videojuegos que satisfaga las necesidades de los usuarios y la empresa. El proyecto abarca desde el tratamiento y recolección de datos hasta el entrenamiento y mantenimiento del modelo de Machine Learning.

## Propuesta de Trabajo

### ETL (Extract, Transform, Load)

- **Transformaciones:** En este MVP, priorizamos la lectura del dataset con el formato correcto y la eliminación de columnas innecesarias para optimizar la API y el entrenamiento del modelo.

- **Feature Engineering:** Creamos la columna 'sentiment_analysis' aplicando análisis de sentimiento con NLP a las reseñas de los usuarios. Los valores son 0 (malo), 1 (neutral) o 2 (positivo). Si no es posible realizar el análisis, se asigna 1.

### Desarrollo de la API (FastAPI)

Proponemos exponer los datos a través de una API utilizando el framework FastAPI. Las consultas que implementamos incluyen:

- `developer(desarrollador: str)`: Devuelve la cantidad de items y el porcentaje de contenido gratuito por año según la empresa desarrolladora.

- `userdata(User_id: str)`: Proporciona información sobre el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items.

- `UserForGenre(genero: str)`: Encuentra al usuario con más horas jugadas para un género dado y muestra una lista de las horas jugadas por año de lanzamiento.

- `best_developer_year(año: int)`: Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado.

- `developer_reviews_analysis(desarrolladora: str)`: Ofrece estadísticas de reseñas de usuarios categorizadas como positivas o negativas para una empresa desarrolladora.

### Deployment

El despliegue se realiza en Render, lo que permite que la API sea accesible desde cualquier dispositivo con conexión a Internet.

### Análisis Exploratorio de Datos (EDA)

El EDA se enfoca en investigar relaciones entre variables, detectar outliers y explorar patrones interesantes en el dataset. El análisis incluye la generación de nubes de palabras para comprender las palabras más frecuentes en los títulos de los juegos.

### Modelo de Aprendizaje Automático

El modelo de Machine Learning es capaz de recomendar juegos a los usuarios:

- **Sistema de Recomendación Usuario-Ítem:** Recibe un usuario y devuelve una lista de juegos recomendados para ese usuario.

## Proyecto

- **Repositorio:** Se verificó que el repositorio contuviera nombres de archivo adecuados y una estructura organizada. El `README.md` proporciona una guía clara del proyecto.

- **Cumplimiento de Requerimientos:** Se comprobó si se cumplieron los requerimientos de aprobación mencionados en la propuesta de trabajo.

## Video de Presentación

Un video con una duración máxima de 7 minutos es esencial para demostrar el funcionamiento de la API y explicar el modelo de Machine Learning utilizado.


El MVP aprobatorio está listo para ser consumido a través de RENDER y cumple con todos los criterios mencionados. Este proyecto me permitio mostrar mis habilidades en ETL, FastAPI, EDA y Machine Learning.