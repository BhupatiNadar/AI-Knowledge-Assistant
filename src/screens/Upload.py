import streamlit as st
import pymupdf
from datetime import datetime

from src.database.db import (
    insert_document,
    insert_document_pages,
    fetch_documents,
    remove_user_document
)


def History_template(file_name, uploaded_at, document_id):

    dt = datetime.fromisoformat(uploaded_at)

    col1, col2, col3 = st.columns([5, 3, 1])

    with col1:
        st.write(f"📄 {file_name}")

    with col2:
        st.write(
            dt.strftime("%d %b %Y, %I:%M %p")
        )

    with col3:

        if st.button(
            "🗑️",
            key=f"delete_{document_id}"
        ):

            remove_user_document(
                document_id=document_id,
                user_id=st.session_state["User_data"][0]["user_id"]
            )

            st.rerun()
        


def extract_pdf_pages(uploaded_file):

    pdf = pymupdf.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    pages = []

    for page_num, page in enumerate(pdf):

        text = page.get_text().strip()

        if text:

            pages.append({
                "page_number": page_num + 1,
                "page_content": text
            })

    pdf.close()

    return pages


def upload_screen():

    st.header("Upload Documents")
    st.write(
        "Upload your documents to start asking questions"
    )

    uploaded_files = st.file_uploader(
        label="",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        if st.button(
            "Upload Documents",
            use_container_width=True
        ):

            user_id = (
                st.session_state["User_data"][0]["user_id"]
            )

            with st.spinner("Uploading..."):

                for file in uploaded_files:

                    pages = extract_pdf_pages(file)

                    document_id = insert_document(
                        user_id=user_id,
                        file_name=file.name
                    )

                    insert_document_pages(
                        document_id=document_id,
                        pages=pages
                    )

            st.success(
                f"{len(uploaded_files)} file(s) uploaded successfully."
            )

            st.rerun()

    st.divider()

    st.header("History")

    user_id = (
        st.session_state["User_data"][0]["user_id"]
    )

    documents = fetch_documents(user_id)

    if not documents:
        st.info("No documents uploaded yet.")
        return

    for document in documents:

        History_template(
            file_name=document["file_name"],
            uploaded_at=document["uploaded_at"],
            document_id=document["document_id"]
        )