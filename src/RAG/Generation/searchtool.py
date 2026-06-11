from RAG.retrieval.retriever import retrieve

def create_search_tool(user_id):

    def search_documents(query: str) -> str:
        chunks = retrieve(query, user_id)

        if not chunks:
            return "No relevant information found."

        return "\n\n".join(
            chunk["content"]
            for chunk in chunks[:5]
        )

    return search_documents