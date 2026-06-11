import streamlit as st

def setting_screen():
    if st.button("Logout"):
        st.session_state["User_data"] = None
        st.session_state["User_login"] = None
        st.session_state["login_type"] = None
        st.session_state["User_tab"] = None
        st.session_state["User_tab"]="Chat"
        st.rerun()