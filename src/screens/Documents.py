from datetime import datetime
import streamlit as st
import time

from src.database.db import fetch_documents,remove_user_document
from src.RAG.pipline.ragpipline import ingest_file


def document_card(id,file_name, upload_date):

    try:
        dt = datetime.fromisoformat(upload_date)
        upload_date = dt.strftime("%d %b %Y, %I:%M %p")
    except:
        pass

    with st.container(border=True):
        st.write(f"📄 **{file_name}**")
        st.caption(upload_date)

        with st.popover("⋮"):
            if st.button("🗑 Delete", key=f"delete_{file_name}"):
                try:
                    remove_user_document(id,st.session_state["User_data"][0].get("user_id"))
                    st.success(f"Deleted {file_name}")
                    time.sleep(3)
                    st.rerun()
                except Exception as e:
                    st.error(f"something went Wrong:{e}")


def document_screen():

    col1, col2 = st.columns([4, 1])

    with col1:
        st.header("All Documents")
        st.write("Manage and organize your uploaded documents")

    with col2:
        if st.button("➕ Add Document"):
            st.session_state["User_tab"] = "Upload"

    _, col2 = st.columns([4, 1])

    with col2:
        if st.button("Convert into Embedding"):
            ingest_file(st.session_state["User_data"][0]["user_id"])
            
            

    documents = fetch_documents(
        st.session_state["User_data"][0]["user_id"]
    )

    cols_per_row = 3

    for i in range(0, len(documents), cols_per_row):

        cols = st.columns(cols_per_row)

        for col, doc in zip(cols, documents[i:i + cols_per_row]):

            with col:
                document_card(
                    id=doc.get("id"),
                    file_name=doc.get("file_name"),
                    upload_date=doc.get("uploaded_at")
                )