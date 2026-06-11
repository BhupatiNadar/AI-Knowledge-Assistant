import streamlit as st
from datetime import datetime

from src.database.db import (
    fetch_conversations,
    delete_conversation,
    get_conversation_title,
    get_history
)


def history_screen():
    

    st.header("⟲ Conversation History")
    st.write("View and resume your past conversations")

    user_id = st.session_state["User_data"][0]["user_id"]
    conversations = fetch_conversations(user_id)

    if not conversations:
        st.info("No conversations yet. Start a new chat to get going!")
        return

    for convo in conversations:
        convo_id = convo["conversation_id"]
        created_at = convo["created_at"]

        title = get_conversation_title(convo_id)

        try:
            dt = datetime.fromisoformat(created_at)
            time_str = dt.strftime("%d %b %Y, %I:%M %p")
        except Exception:
            time_str = created_at

        with st.container(border=True):
            col1, col2, col3 = st.columns([5, 3, 1])

            with col1:
                st.markdown(f"**💬 {title}**")

            with col2:
                st.caption(time_str)

            with col3:
                with st.popover("⋮"):
                    if st.button(
                        "🗑 Delete",
                        key=f"del_convo_{convo_id}"
                    ):
                        delete_conversation(convo_id, user_id)
                        st.success("Conversation deleted.")
                        st.rerun()

            if st.button(
                "Resume →",
                key=f"resume_{convo_id}",
                use_container_width=True
            ):
                history = get_history(convo_id)
                st.session_state["conversation_id"] = convo_id
                st.session_state["chat_messages"] = [
                    {"role": msg["role"], "content": msg["content"]}
                    for msg in history
                ]
                st.session_state["User_tab"] = "Chat"
                st.rerun()