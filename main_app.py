import  streamlit as st
from PIL import Image

st.title('Webアプリの練習')
st.caption('テストアプリ')

image = Image.open('../images.png')
st.image(image,width=250)

