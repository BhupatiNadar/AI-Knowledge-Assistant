def split_docs(documents, chunk_size=500, chunk_overlap=50):
    """
    Split a list of page dicts into smaller chunks.
    Each input doc: { "content": str, "metadata": dict }
    Returns a list of dicts with same structure.
    """
    chunks = []
    for doc in documents:
        text = doc["content"]
        metadata ={
            "page": doc["page_number"],
            "document_id": doc["documents"]["document_id"]
        }

        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]
            chunks.append({
                "content": chunk_text,
                "metadata": {**metadata, "chunk_start": start}
            })
            start += chunk_size - chunk_overlap  # slide with overlap

    return chunks
