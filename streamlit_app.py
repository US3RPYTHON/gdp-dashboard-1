import streamlit as st

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to:",
    ["study", "Create"]
)
if page == "study":
    st.title("Choose a question set")

elif page == "Create":
    st.title("Create a new question set")
    if not st.session_state.get("logged_in", False):

        password = st.text_input(
            "Password", 
            type="password"
        )
        if st.button("Log in"):
            if password == st.secrets["passwords"]["owner"]:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Incorrect password.")
else:
    st.write("question creator")
    
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()