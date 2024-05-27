# Introducción
Este proyecto utiliza Flask para la construcción de una API que permita la clasificación de las tres clases de la base de datos IRIS, utilizando una muy sencilla interfaz que permite ingresar tres variables, la longitud y ancho de sépalo y la longitud del pétalo.

# Estructura del proyecto
En este proyecto se tiene la siguiente distribución de carpetas y archivos:

>model
>>model_building.ipynb 
>>training_model.pkl


>>img
>>>banner_bioudea.png
>>>iris_flower.png

>static
>>prediction.html

>app.py

>requirements.txt

>README.md

>.gitignore


* `model/model_building.ipynb` - Notebook para entrenar y guardar el modelo en un archivo con extensión 'pkl'
* `model/training_model.pkl` - Archivo que contiene el modelo entrenado
* `static/prediction.html` - Archivo HTML que se utiliza para mostrar la predicción
* `app.py` - Archivo que contiene la lógica de la API
* `requirements.txt` - Archivo que contiene las dependencias necesarias para el proyecto

# Construir el modelo
Para este ejercicio usamos el problema de clasificación de las especies de la flor Iris de la base de datos [IRIS](https://www.kaggle.com/code/joeportilla/analisis-exploratorio-de-datos-dataset-iris). Se entrena un Árbol de Decisión. El análisis de la base de datos, la contrucción del modelo en *Scikit-learn* y el entrenamiento de este se hace dentro del archivo `model_building.ipynb`.

# Ejecución del proyecto
### 1. Creación del ambiente vitual.
Primero debemos crear un ambiente virtual para instalar las dependencias necesarias para el proyecto.
#### Para sistema operativo Windows
- python -m venv `mi_entorno`
- `mi_entorno`\Scripts\activate
#### Para sistema operativo Linux o Mac
- python3 -m venv `mi_entorno`
- source `mi_entorno`/Scripts/activate

### 2. Instalación de las dependecias de la API
- pip install -r requirements.txt

### 3. Ejecución de la API
- python app.py

### 4. Prueba en el navegador
- Abrimos un navegador y accedemos a la dirección http://localhost:5000/
- En el formulario que aparece, debe ingresar la información de las tres variables.
- Se muestra la predicción de la clase de la flor Iris.
