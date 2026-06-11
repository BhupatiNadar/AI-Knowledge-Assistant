import streamlit as st

from src.database.db import create_conversation, get_history
from src.RAG.Generation.generation_pipline import generation_pipeline


def _init_chat_state():
    if "conversation_id" not in st.session_state:
        st.session_state["conversation_id"] = None

    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = []


def _start_new_chat():
    user_id = st.session_state["User_data"][0]["user_id"]
    conversation_id = create_conversation(user_id)
    st.session_state["conversation_id"] = conversation_id
    st.session_state["chat_messages"] = []


def _load_conversation(conversation_id):
    st.session_state["conversation_id"] = conversation_id
    history = get_history(conversation_id)
    st.session_state["chat_messages"] = [
        {"role": msg["role"], "content": msg["content"]}
        for msg in history
    ]


def _send_message(user_query):
    conversation_id = st.session_state["conversation_id"]

    st.session_state["chat_messages"].append({
        "role": "user",
        "content": user_query
    })

    response = generation_pipeline(user_query, conversation_id)

    st.session_state["chat_messages"].append({
        "role": "assistant",
        "content": response
    })


def chat_screen():
    _init_chat_state()

    user_name = st.session_state["User_data"][0].get("user_name")

    col1, col2 = st.columns([4, 1])

    with col1:
        st.header(f"👋 Hello, {user_name}!")
        st.write("Ask me anything about your documents. I'll answer with sources.")

    with col2:
        if st.button("✨ New Chat", use_container_width=True):
            _start_new_chat()
            st.rerun()

    if st.session_state["conversation_id"] is None:

        st.markdown("---")
        st.subheader("💡 Try asking")

        suggestions = [
            "What is the leave policy?",
            "How is performance evaluated?",
            "What are the employee benefits?",
            "Summarize the main document"
        ]

        cols = st.columns(len(suggestions))

        for col, text in zip(cols, suggestions):
            with col:
                if st.button(text, use_container_width=True):
                    _start_new_chat()
                    _send_message(text)
                    st.rerun()

        return

    for msg in st.session_state["chat_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input(placeholder="Ask any question about your documents...")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                _send_message(user_input)
                st.markdown(st.session_state["chat_messages"][-1]["content"])

        st.rerun()