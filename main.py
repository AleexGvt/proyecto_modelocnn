from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
import base64
import tensorflow as tf
import numpy as np

app = FastAPI()

model = tf.keras.models.load_model('./xnet_model.h5')

# Función de preprocesamiento de la imagen
def preprocess_image(image):
    # Redimensionar la imagen a las dimensiones requeridas por el modelo
    image = image.resize((224, 224))
    
    # Convertir la imagen a un arreglo de numpy y normalizar los valores de píxeles
    image_array = np.array(image) / 255.0
    
    # Expandir las dimensiones del arreglo para que coincida con el formato de entrada del modelo
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array

@app.get("/")
async def root():
    # df = pd.read_csv('/home/lubmorsis-01/Documents/Proyects/bootcamp/m7/titanic.csv')
    # df['Survived'] = df['Survived'].astype(str)
    return {"message": "Hello World"}

@app.post("/pneumonia/predict")
async def upload_image(file: UploadFile = File(...)):
    # Procesar la imagen
    if( file.filename.endswith(".jpg") or file.filename.endswith(".jpeg") ):

        image = Image.open(file.file)
    
        preprocessed_image = preprocess_image(image)
    
        # Obtener la predicción del modelo
        prediction = model.predict(preprocessed_image)
        return {"status": "ok", "prediccion": prediction}
    else:
        return {"status": "error", "message": "invalid file format"}