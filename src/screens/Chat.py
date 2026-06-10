import streamlit as st

def chat_screen():
    
    st.header(f"👋 Hello, {st.session_state["User_data"][0].get("user_name")} !")
    
    st.write("Ask me anything about your documnts. i will answer with scources")
    
    st.write("Reference")
    
    list_content=["What is the leaving policy?","how is the performance evalution ?","What are the benefits?","show leave policy"]
    
    col1,col2,col3,col4=st.columns(4,gap='small')
    
    for col, text in zip(st.columns(4), list_content):
        with col:
            st.write(text)
            
    if "user_messages" not in st.session_state:
        st.session_state.user_messages = []
        
    if st.session_state.user_messages:
        st.write(st.session_state.user_messages)
        
    
    chat=st.chat_input(placeholder="Ask any question about your document")
    
    if chat:
        st.session_state.user_messages.append(chat)
        st.rerun()
    
    