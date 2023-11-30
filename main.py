import requests
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title = 'Aiden Webpage', page_icon=':tada:', layout='wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding =load_lottieurl("https://lottie.host/0065e8b9-febf-4b70-a032-43e3c8f10208/35qjEZi0bn.json")

with st.container():
    st.subheader("Hi! I am Aiden :wave:")
    st.title('The best Data Analyst')

    st.write(("Yes, I make it"))

    st.write("[Learn more about this: at Aiden directory :tada: ](https://google.com)")

with st.container():
    st.write("-----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('What i do')
        st.write("##")
        st.write("The demonstration below is my work project, very excited with this streamlit from python")

    with right_column:
        st_lottie(lottie_coding,height=300, key="coding")

my_image = Image.open("images/123.jpg")
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(my_image)
    with text_column:
        st.subheader('This is the project relate to Analyze the data with animation')
        st.write("""
        This will manipulate the real time data of the US population base on the US bureal information
        """)