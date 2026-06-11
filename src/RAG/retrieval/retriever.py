from src.database.config import Supabase
from src.RAG.embeddings.embedder import embedding_manager


def retrieve(query: str, user_id: int, n_results: int = 5):

    query_embedding = embedding_manager.generate_single(query)

    if hasattr(query_embedding, "tolist"):
        query_embedding = query_embedding.tolist()

    response = (
        Supabase.rpc(
            "match_documents",
            {
                "query_embedding": query_embedding,
                "match_count": n_results,
                "p_user_id": user_id
            }
        )
        .execute()
    )

    chunks = []

    for row in response.data:

        chunks.append({
            "content": row["chunk_text"],
            "source": row["file_name"],
            "page": row["page_number"],
            "similarity": row["similarity"],
            "document_id": row["document_id"]
        })

    return chunks