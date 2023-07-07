# proyecto_modelocnn
Proyecto del módulo 7 del Bootcamp Ciencia de Datos e Inteligencia Artificial

# Entorno colab notebook
Regístrate o inicia sesión en https://www.kaggle.com/ con tu cuenta. Haz clic en "Mi cuenta". Desplázate hacia abajo hasta la sección de API. Haz clic en "Expirar token de API". Luego, haz clic en "Crear nuevo token de API". Este paso es necesario para generar un token de acceso que te permitirá conectarte a tu cuenta de Kaggle a través de la API de Kaggle.
Descarga el archivo .json a tu directorio local.
Descarga el archivo chest_x_ray_pneumonia_classification.ipynb de este repositorio a tu directorio local.
Abre Google Colab y carga el archivo chest_x_ray_pneumonia_classification.ipynb en el cuaderno de Colab.
Ejecuta todo el script y, cuando se te solicite, carga el archivo .json descargado anteriormente en tu entorno de Colab. Esto es necesario para vincular la API de Kaggle con el entorno de Colab y poder descargar conjuntos de datos directamente en Colab.
No dudes en descargar el conjunto de datos desde https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia para familiarizarte con los datos y ver las imágenes en los subdirectorios de entrenamiento, prueba y validación.

# FastAPI predicción de imágenes

Este repositorio contiene un sencillo endpoint de FastAPI que acepta una imagen y realiza una predicción utilizando un modelo pre-entrenado. Puede ser utilizado para clasificar imágenes basándose en el modelo entrenado.

# Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias requeridas usando pip install -r requirements.txt.

# Uso

1. Ejecuta el servidor FastAPI usando el comando uvicorn main:app --reload.
2. Abre tu navegador y ve a http://localhost:8000/docs para acceder a la interfaz de Swagger.
3. Utiliza el endpoint /predict para subir una imagen y obtener el resultado de la predicción.

# Endpoint de la API
/pneumonia/predict [POST]

Este endpoint acepta una carga de archivo con la imagen a clasificar. Retorna el resultado de la predicción en formato JSON.

curl -X POST -F "file=@imagen.jpg" http://localhost:8000/predict

Ejemplo de respuesta:

{
    "clase": "gato",
    "probabilidad": 0.95
}


