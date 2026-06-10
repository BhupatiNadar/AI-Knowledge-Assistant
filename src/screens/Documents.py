import streamlit as st

def document_screen():
    
    col1,col2=st.columns([4,1])
    
    with col1:
        st.header("All Documents")
        st.write("Manage and organize your uploaded documents")
        
    with col2:
        if st.button("➕ Add Document"):
            st.session_state["User_tab"]="Upload"