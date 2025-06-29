# Trabajos practicos de IA

En este repositorio almacenamos los trabajos practicos sugeridos para la materia de Inteligencia Artificial TN-Jueves.

1. Usar el yml de anaconda para crear el env

2. Tener instalado Python 3.8+ y crear un entorno virtual
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt  # (si el archivo existe)

3. Correr las celdas en orden para reproducir el análisis.

## TP1

Este trabajo práctico se centra en aplicar técnicas de análisis exploratorio de datos (EDA) y aprendizaje automático (ML) sobre un conjunto de datos de marketing bancario, con el objetivo de predecir si un cliente aceptará una oferta de producto financiero. El problema se enmarca como una clasificación binaria, siendo la variable objetivo y (con valores "yes" o "no").

El dataset contiene 21 variables que incluyen atributos personales, historial de contacto, indicadores económicos y resultados de campañas previas. Ejemplos:

a. age, job, marital, education: datos demográficos.
b. contact, month, day_of_week, duration: detalles del contacto con el cliente.
c. emp.var.rate, euribor3m: variables económicas externas.
d. y: variable objetivo (si el cliente aceptó o no la oferta).