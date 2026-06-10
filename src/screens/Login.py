import streamlit as st 
import os

from src.UI.base_layout import Signup_screens_layout
from src.database.db import check_user




def Check_Login_User(email, password):
    if not email:
        st.warning("Please enter your email")
    elif not password:
        st.warning("Please enter your password")
    else:
        try:
            login,user_data=check_user(email, password)
            if login:
                st.session_state["User_login"] = True
                st.session_state["User_data"]=user_data
                st.rerun()
            else:
                st.warning("Password or email doesn't match")
        except Exception as e:
            st.warning(f"Something Went Wrong: {e}")
        
    









def LoginScreen():
    
    Signup_screens_layout()
    
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    Signup_right_panel_img = os.path.join(base_path, "src", "assets", "Signup_right_panel_img.jpg")
    
    col1, col2 = st.columns([1, 1.2], gap="small")
    
    with col1:
        st.markdown("""
                 <div class="left-panel">
                  <div class="logo">🤖 <b>AI Knowledge</b><span class="purple">Assistant</span></div>
                  
                  <div class="heading">Your Documnets.  Smart Answers.</div>
                  
                  <div class="subtext">Upload your documents and get instant answers  with sources you can trust</div>
                  
                    <div class="feature">
                        <div class="feature-icon">🔍</div>
                        <div>
                            <div class="feature-title">Smart Search</div>
                            <div class="feature-desc">Find accurate information from your documnets  in secounds</div>
                        </div>
                    </div>
                    
                    <div class="feature">
                        <div class="feature-icon">🔐</div>
                        <div>
                            <div class="feature-title">Source Citations</div>
                            <div class="feature-desc">Every answer is backed by real sources  with page references</div>
                        </div>
                    </div>
                    
                    <div class="feature">
                        <div class="feature-icon">🔒</div>
                        <div>
                            <div class="feature-title">Secure & Private</div>
                            <div class="feature-desc">Your documents and conversations are  always secure and private/div>
                        </div>
                    </div>
                    
                 </div>
                    """,unsafe_allow_html=True)
        
        st.image(Signup_right_panel_img)
    
    with col2:

        top_left, top_right = st.columns([4, 1], gap="small")
        with top_left:
            st.markdown('<div class="signin">Don\'t have an account? </div>', unsafe_allow_html=True)
        with top_right:
            if st.button("Signup", key="signup_btn",width='stretch'):
                st.session_state["login_type"] = "Signup"
                st.rerun()

        st.markdown('<div class="form-title">Welcome back 👋</div><div class="form-sub">Sign in to continue to your Ai Knowledge Assistant</div>', unsafe_allow_html=True)
        st.markdown('<div style="display:flex;gap:10px;"></div>', unsafe_allow_html=True)

        email = st.text_input("Email address", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        
        st.divider()

        
        if st.button("Login",use_container_width=True):
            Check_Login_User(email,password)

        st.markdown(
"""<div class="footer">🔒 Your data is safe and encrypted</div>""",
            unsafe_allow_html=True
        )

    