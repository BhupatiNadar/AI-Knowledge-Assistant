import streamlit as st

from agno.agent import Agent
from agno.models.groq import Groq

  
def build_agent():

    return Agent(
        model=Groq(
            id="qwen/qwen3-32b",
            api_key=st.secrets["GROQ_API_KEY"]
        ),
        markdown=True,
        add_datetime_to_context=True,
        instructions=[
        "You are an AI Knowledge Assistant that answers ONLY based on the provided document excerpts.",
        "Document excerpts are included in the user's message between '--- RELEVANT DOCUMENT EXCERPTS ---' markers.",
        "ONLY use information from those excerpts. Do NOT use your own general knowledge.",
        "ALWAYS cite the source file name and page number for every piece of information: (Source: filename.pdf, Page: X)",
        "If no document excerpts are provided, tell the user no matching content was found.",
        "NEVER make up or fabricate document content.",
        "Use previous conversation messages for context to maintain continuity.",
        ]
    )