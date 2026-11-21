import streamlit as st
st.title("My Super Awesome Website")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to:",
    ["study", "Create"]
)
if page == "study":
    st.title("Choose a question set")

elif page == "Create":
    st.title("Create a new question set")