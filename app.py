import streamlit as st
from tensorflow import keras
from keras.preprocessing import image
import os
from PIL import Image
import numpy

def get_model():
    model_path = os.getcwd()
    model_path = os.path.join(model_path, "CNN_Model")
    model = keras.models.load_model(model_path)

    return model

def get_res(model,img):
    img = numpy.asarray(img).reshape(1,150,150,3)
    img = img/255
    predict = model.predict(img)
    if predict >= 0.5:
        text = "Healthy tooth"
    elif 0.25 <= predict <= 0.45:
        text = "Mild Cavity"
    else:
        text = "Cavity infected tooth"
    
    return text

st.header("Cavity Detection - A TARP project by Shilpan Pawan Singh")
model = get_model()
uploaded_file = st.file_uploader("Choose a JPG file")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = image.resize((150,150))
    st.image(image,width=300) 
    st.subheader(get_res(model,image))