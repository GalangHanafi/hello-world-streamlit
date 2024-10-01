import streamlit as st

st.title("Hello Word ")

name = st.text_input("nama")

if (name):
    st.write("hallo, nama saya : ", name)
else:
    st.warning("please, input your name!!!")

