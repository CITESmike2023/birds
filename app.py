import pandas as pd
import streamlit as st
from helper import get_info_bird ,heatmap_bird,map_3d,scientific_n,get_image
from streamlit_lottie import st_lottie
import json

st.set_page_config(layout='wide')
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
#st.markdown(hide_default_format, unsafe_allow_html=True)
from streamlit_folium import st_folium


df = pd.read_csv('train_metadata.csv')


#df.describe(include ='all')
#df.isnull().sum()
df.dropna(inplace=True)
#C:\work\birds\birdsCLEF\train_audio\asbfly\XC49755.ogg
BASE_PATH = 'C:\work\birds\birdsCLEF\train_audio\ '
df['filepath'] = BASE_PATH +   df.primary_label + " \ " +  df.filename.map(lambda x: x.split('/')[-1])
import os
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
title= "<p style='font-family:Comic Sans MS ;font-size:38px;'>Feathers and Frequencies</p>"
subh = "<p style='font-family:Comic Sans MS ;font-size:18px;'>A Technological Approach to Birdwatching</p>"
lottie_coding = load_lottiefile("Animation.json")
st.sidebar.write(title,unsafe_allow_html=True)
st.sidebar.write(subh,unsafe_allow_html=True)
with st.sidebar:
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",height=220
    )




birds_common =df['common_name'].value_counts()[df['common_name'].value_counts() > 100]

#birds_common.index
#df[df['common_name']=='Asian Brown Flycatcher']

#st.title('hi')
bird = st.sidebar.selectbox("enter bird name ",options= birds_common.index)

#st.sidebar.image(get_image(bird))
#st.write(bird)
#about = '<p style=font-size:22px;><b> Description </p>'
st.write(f"<p style=font-size:30px; font-family:Comic Sans MS ;'><b>{bird} </p>",unsafe_allow_html=True)
col1, col2 = st.columns([1.8, 1.2])
with col1:
    st.write(f"<p style='font-family:Comic Sans MS ;font-size:19px;'> <b>Description:-</b> {get_info_bird(bird)}</p>",unsafe_allow_html=True)
    s_n= scientific_n(bird,df)
    st.write(f"<p style='font-family:Comic Sans MS ;font-size:19px;'> <b>Scientific Name:-</b> {s_n}</p>",unsafe_allow_html=True)
with col2:
    st.image(get_image(bird))
st.write("<p style='font-family:Comic Sans MS ;font-size:19px;text-align: center;'>Heatmap</p>",unsafe_allow_html=True)
heatmap_bird(bird,df)
st.write("<p style='font-family:Comic Sans MS ;font-size:19px;text-align: center;'>3D Scatterplot</p>",unsafe_allow_html=True)
st.pydeck_chart(map_3d(bird,df))
#print(heatmap_bird('Asian Brown Flycatcher',df))
#st_map = st_folium(heatmap_bird('Asian Brown Flycatcher',df), width=725)
#st.write(st_map)
