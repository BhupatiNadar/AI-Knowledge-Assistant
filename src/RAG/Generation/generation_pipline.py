from agno.models.message import Message

from src.database.db import get_history, save_message
from src.RAG.Generation.agent import build_agent
from src.RAG.retrieval.retriever import retrieve
import streamlit as st


MAX_CONTEXT_MESSAGES = 20


def _build_context_from_docs(user_query: str, user_id: int) -> str:
    try:
        chunks = retrieve(user_query, user_id)
    except Exception as e:
        print(f"[Pipeline] Retrieval error: {e}")
        return ""

    if not chunks:
        return ""

    context_parts = []
    for chunk in chunks[:5]:
        context_parts.append(
            f"[Source: {chunk['source']}, Page: {chunk['page']}]\n{chunk['content']}"
        )

    return "\n\n---\n\n".join(context_parts)


def generation_pipeline(user_query: str, conversation_id: int) -> str:

    user_id = st.session_state["User_data"][0]["user_id"]

    history = get_history(conversation_id)

    doc_context = _build_context_from_docs(user_query, user_id)

    messages = []

    recent_history = history[-MAX_CONTEXT_MESSAGES:] if len(history) > MAX_CONTEXT_MESSAGES else history

    for msg in recent_history:
        messages.append(
            Message(role=msg["role"], content=msg["content"])
        )

    if doc_context:
        enriched_query = (
            f"User Question: {user_query}\n\n"
            f"--- RELEVANT DOCUMENT EXCERPTS ---\n\n"
            f"{doc_context}\n\n"
            f"--- END OF EXCERPTS ---\n\n"
            f"Answer the question using ONLY the document excerpts above. "
            f"Cite the source file name and page number for each piece of information."
        )
    else:
        enriched_query = (
            f"{user_query}\n\n"
            f"[No relevant documents were found for this query. "
            f"Inform the user that no matching content was found in their uploaded documents.]"
        )

    messages.append(
        Message(role="user", content=enriched_query)
    )

    agent = build_agent()
    response = agent.run(input=messages)

    assistant_response = response.content

    save_message(conversation_id, "user", user_query)
    save_message(conversation_id, "assistant", assistant_response)

    return assistant_response
