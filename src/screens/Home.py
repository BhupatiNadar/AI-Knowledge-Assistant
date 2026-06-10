import streamlit as st
import os

from src.screens.Chat import chat_screen
from src.screens.Documents import document_screen
from src.screens.Upload import upload_screen
from src.screens.History import history_screen

def HomeScreen():
    
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    user_logo = os.path.join(base_path, "src", "assets", "user_logo_img.png")
    
    col1,col2=st.columns([0.8,4])
    
    with col1:
        st.markdown("""
                    <div class="left-panel">
                        <div class="logo">🤖 <b><b>AI Knowledge</b><span class="purple">Assistant</span></b></div>
                    </div>
                    
                    """,unsafe_allow_html=True)
        
        
        if st.button("💬 Chat",width='stretch'):
           st.session_state["User_tab"]="Chat"
        
        if st.button("📃 Documents",width='stretch'):
            st.session_state["User_tab"]="Documents"
        
        if st.button("📄 Upload",width='stretch'):
            st.session_state["User_tab"]="Upload"
        
        if st.button("⟲ History",width='stretch'):
           st.session_state["User_tab"]="History"
        
        if st.button("📑 Bookmark",width='stretch'):
            st.session_state["User_tab"]="Bookmark"
        
        if st.button("📑 Tools",width='stretch'):
            st.session_state["User_tab"]="Tools"
        
        if st.button("⚙️ Settings",width='stretch'):
            st.session_state["User_tab"]="Settings"
        
        st.markdown(f"""
                   <div class="User_detail">
                    """,unsafe_allow_html=True)
        
        st.image(user_logo, width=50)
        
        st.markdown(f"""
                    <div>
                    {st.session_state["User_data"][0].get("user_name")}
                    </div>
                </div>""",unsafe_allow_html=True)
        
        
        
    with col2:
        match (st.session_state["User_tab"]):
            case "Chat":
                chat_screen()
                
            case "Documents":
                document_screen()
            
            case "Upload":
                upload_screen()
            
            case "History":
                pass
            
            case None:
                chat_screen()