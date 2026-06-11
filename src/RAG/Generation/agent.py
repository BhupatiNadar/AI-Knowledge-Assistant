import streamlit as st

from agno.agent import Agent
from agno.models.groq import Groq
from RAG.Generation.searchtool import create_search_tool

  
def build_agent():

    user_id = st.session_state["User_data"][0]["user_id"]

    return Agent(
        model=Groq(
            id="qwen/qwen3-32b",
            api_key=st.secrets["GROQ_API_KEY"]
        ),
        markdown=True,
        add_datetime_to_context=True,
        tools=[
            create_search_tool(user_id)
        ]
    )