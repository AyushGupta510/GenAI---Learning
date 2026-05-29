import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name")

age = st.slider("select your age:",0,100,25)

st.write(f"your age is {age} . ")

options = ["Python","Java","C++","javaScript"]
choice = st.selectbox("Choose your Fav Language",options)
st.write(f"You selected {choice}.")



if name:
    st.write(f"hello , {name}")

data = {
    "Name" : ["aarav","sam","aman","Jason"],
    "Age" : [22,26,22,20],
    "City" : ["Lucknow","Kanpur","Pune","Noida"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file",type = "csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)