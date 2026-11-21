import streamlit as st
st.title("My Super Awesome Website")
st.write("Welcome!")
name = st.text_input("What is your name?")
if st.button("submit"):
    st.write("Hello, ", name)

Ques1 = st.text_input("How many layers are there in the OSI model?")
if st.button("check"):
    if Ques1.lower().strip() in ("seven", "7"):
        st.write(Ques1, "is correct")
    else:
        st.write("Sorry, that's incorrect")