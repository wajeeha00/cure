import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ammad Ali")
    content = """Passionate Computer Engineer specializing 
    in ML/AI, computer vision, signal processing, and 
    embedded systems. Strong programming and data analysis 
    skills with a drive to contribute to innovative 
    projects in computer engineering.
"""
    st.info(content)

first_para = """Below you can find some of the apps I have
built in Python. Feel free to contact me!"""

st.write(first_para)

col3, _, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv", sep=';')


with col3:
    for index, row in df.iterrows():
        if index%2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{index+1}.png")
            link = row["url"]
            st.write(f"[Source Code]({link})")
        else:
            continue

with col4:
    for index, row in df.iterrows():
        if index%2 != 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{index+1}.png")
            link = row["url"]
            st.write(f"[Source Code]({link})")
        else:
            continue