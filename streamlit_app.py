import streamlit as st
st.title("My Super Awesome Website")
st.write("Welcome!")
name = st.text_input("What is your name?")
if st.button("submit"):
    st.write("Hello, ", name)