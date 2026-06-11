from src.RAG.ingestion.text_cleaner import TextCleaner
from src.database.db import fetch_document_pages,insert_document_chunks
from src.RAG.ingestion.chunker import split_docs 
from src.RAG.embeddings.embedder import embedding_manager
import streamlit as st

_cleaner = TextCleaner()


def ingest_file(user_id):
    """
    Full ingestion pipeline for a single PDF file.
    1. Load pages from PDF
    2. Clean text
    3. Split into chunks
    4. Generate embeddings
    5. Store in ChromaDB
    """
    
    pages = fetch_document_pages(user_id)
    if not pages:
        print(f"No Pages found")
        return
    
    print(len(pages))

    # 2. Clean
    for page in pages:
        page["content"] = _cleaner.clean(page["page_content"])

    # Remove empty pages after cleaning
    pages = [p for p in pages if p["content"].strip()]
    
    # st.write(pages[0])

    # 3. Chunk
    chunks = split_docs(pages, chunk_size=500, chunk_overlap=50)
    print(f"[Pipeline] {len(pages)} pages → {len(chunks)} chunks")

    # 4. Embed
    texts = [c["content"] for c in chunks]
    embeddings = embedding_manager.generate_embeddings(texts)

    # 5. Store
    rows = []
    
    # st.write(type(embeddings[0]))

    for chunk, embedding in zip(chunks, embeddings):

        rows.append({
            "document_id": chunk["metadata"]["document_id"],
            "page_number": chunk["metadata"]["page"],
            "chunk_text": chunk["content"],
            "embedding": embedding.tolist()
            })
        
    insert_document_chunks(rows)

    st.success(f"[Pipeline] Stored {len(rows)} chunks in Supabase")
