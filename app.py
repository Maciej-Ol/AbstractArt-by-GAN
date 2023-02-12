#Author: Maciej Ołdakowski
import streamlit as st
import pandas as pd
from keras.models import load_model
import numpy as np
from numpy.random import default_rng
import pathlib

#it is important, that those are the same as in Model_training
NOISE_SIZE=128
IMG_SIZE=64
IMG_CHANNELS=3
PATH_TO_MODELS="models/examples/"
#model_filename = "models//examples//cub_model_v_0.8_e_320.h5"

#get all models from models folder
models_types = pathlib.Path(PATH_TO_MODELS).glob("*.h5")
#get only names of models
model_names = [str(model).split("\\")[-1] for model in models_types]

def gen_image_grid(generator, x=5, y=5):
    latent_points = default_rng().normal(0.0, 1.0, (x*y, NOISE_SIZE))
    X = generator.predict(latent_points)
    array=np.empty(((IMG_SIZE,IMG_SIZE,IMG_CHANNELS)),float)
    count=0
    for i in range(y):
        for j in range(x):
            if j==0:
                array_pom=np.array(X[count].reshape(64,64,3,order='C'))
            else:
                array_pom=np.concatenate((
                    array_pom,np.array(X[count].reshape(
                        64,64,3,order='C'))),axis=1)
            count+=1
        if i==0:
            array=array_pom
        else:
            array=np.concatenate((array,array_pom),axis=0)
    array=(array+1)*255/2
    return array.astype(np.uint8)

def main():
    if 'button' not in st.session_state:
        st.session_state['button'] = False
    overview = st.container()
    images = st.container()
    
    with overview:
        st.title("Generate your grid of abstract paintings")
        st.write("### With a help of GAN")
        model_filename = st.selectbox(
                'Choose a model:',
                model_names)
        x=st.number_input("Insert a x size of an image grid:",
                          min_value=1,max_value=10,value=5)
        y=st.number_input("Insert a y size of an image grid:",
                          min_value=1,max_value=10,value=5)
        if not isinstance(x, int) or not isinstance(y, int):
            st.error("x and y have to be an integer between 1 and 10!",
                     icon="🚨")
        st.session_state['button']=st.button("Generate!")

    with images:
        if st.session_state['button'] == True:
            #upload model
            generator = load_model(PATH_TO_MODELS+model_filename, compile=False)
            image = gen_image_grid(generator,x,y)
            images.image(image, caption='Generated Abstract Art',
                         use_column_width=True)

#run main program
main()