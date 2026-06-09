import streamlit as st


from src.screens.Login import LoginScreen
from src.screens.Signup import SignupScreen
from src.UI.base_layout import style_base_layout

def main():
    style_base_layout()

    st.set_page_config(
        page_title="AI Knowledge Assistant",
        layout="wide"
    )

    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    match st.session_state["login_type"]:

        case "Login":
            LoginScreen()

        case "Signup":
            SignupScreen()
            

        case None:
            LoginScreen()

if __name__ == "__main__":
    main()