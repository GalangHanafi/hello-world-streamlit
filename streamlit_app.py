import streamlit as st

st.title("Hello Word ")

name = st.text_input("nama")

if (name):
    st.warning("please, input your name!!!")
else:
    st.write("hallo, nama saya : ", name)

