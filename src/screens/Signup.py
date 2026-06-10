import streamlit as st
import os
import bcrypt

from src.UI.base_layout import Login_screens_layout
from src.database.db import create_new_user




def User_login(name,email,password,confirm_password):
    if not name:
        st.warning("Please enter your Full name")
                
    elif not email:
        st.warning("Please enter your email")
                
    elif not password:
        st.warning("please enter a password")
                
    elif password != confirm_password:
        st.warning("Password and Confirm Password Did not match")
                
    else:
        password_bytes = password.encode("utf-8")
                
        hashed_password = bcrypt.hashpw(
                password_bytes,
                bcrypt.gensalt()
                ).decode("utf-8")
        try:       
            create_new_user(name,email,hashed_password)
            st.success("Account created successfully")
            st.session_state["login_type"] = "Login"
        
        except:
            st.warning("Something went Wrong")
    





def SignupScreen():
    Login_screens_layout()
    
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    right_panel_img = os.path.join(base_path, "src", "assets", "right_panel_img.png")
    
    col1, col2 = st.columns([1, 1.2], gap="small")

    with col1:
        st.markdown(
f"""<div class="left-panel">
        <div class="logo">🤖 <b>AI Knowledge</b><br><span class="purple">Assistant</span></div>
        <div class="heading">Create your account<br><span class="purple">and unlock insights<br>from your documents.</span></div>
        <div class="subtext">Join thousands of users who trust our AI to find answers, faster.</div>
        <div class="feature"><div class="feature-icon">📄</div>
        <div>
            <div class="feature-title">Smart Document Search</div>
            <div class="feature-desc">Ask anything and get accurate answers from your documents.</div>
            </div>
            </div>
            <div class="feature">
                <div class="feature-icon">🛡️</div>
                <div>
                    <div class="feature-title">Secure & Private</div>
                    <div class="feature-desc">Your data is encrypted and your documents stay private.</div>
                </div>
            </div>
                <div class="feature">
                    <div class="feature-icon">👥</div>
                    <div>
                    <div class="feature-title">AI-Powered Assistance</div>
                    <div class="feature-desc">Advanced AI models with source citations you can trust.</div>
                    </div>
                    </div>
                    """,
            unsafe_allow_html=True
        )
        
        st.image(right_panel_img, width="stretch")
        

    with col2:
        
        top_left, top_right = st.columns([4, 1], gap="small")
        with top_left:
            st.markdown('<div class="signin">Already have an account? </div>', unsafe_allow_html=True)
        with top_right:
            if st.button("Login", key="signup_btn",width='stretch'):
                st.session_state["login_type"] = "Login"
                st.rerun()

        st.markdown('<div class="form-title">Create your account 👋</div><div class="form-sub">Start your journey to smarter document insights.</div>', unsafe_allow_html=True)
        st.markdown('<div style="display:flex;gap:10px;"></div>', unsafe_allow_html=True)

        name = st.text_input("Full name", key="login_name")
        email = st.text_input("Email address", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="login_confirm_password")
        
        st.divider()

        
        if st.button("Create Account",use_container_width=True):
            User_login(name,email,password,confirm_password)

        st.markdown(
"""<div class="footer">🔒 Your data is safe and encrypted</div>""",
            unsafe_allow_html=True
        )
