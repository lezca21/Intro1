import streamlit as st
from PIL import Image 


st.title("Hello word")

st.header("En este espacio comienzo a desarrollar mis apps de interfaces multimodales")
st.write("Facilmente puedo hacer backed y fortend")
image = Image.open("imagen.jpg")

st.image(image, caption="Ay mi madre el bicho")

texto = st.text_input("El mejor leon de la historia mundial", "este es unico y divno")
st.write('El leon te ama',texto)

st.subheader("Ahora hay dos columnas")

col1,col2 = st.columns(2)

with col1:
  st.subheader("primera columna")
  st.write("Todo es mejor si programando estoy")
  respecto = st.checkbox("Estoy de acuerdo")
  if respecto:
    st.write("Buenisima")

with col2:
  st.subheader("Segunda columna")
  modo = st.radio("Tu que prefieres backed o fronted",("backend","fronted","ninguna"))
  if modo == "backend":
    st.write("Eres de los mios siuuuuuu")
  if modo == "fronted":
    st.write("Eres una mierda gasss")
  if modo == "ninguna":
    st.write("Que estas haciendo aqui entonces")
