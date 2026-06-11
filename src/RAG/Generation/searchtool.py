from src.RAG.retrieval.retriever import retrieve

def create_search_tool(user_id):

    def search_documents(query: str) -> str:
        
        print("TOOL CALLED:", query)
        
        try:
            chunks = retrieve(query, user_id)
        except Exception as e:
            print(f"SEARCH ERROR: {type(e).__name__}: {e}")
            return f"Search error: {type(e).__name__}: {e}"

        print(f"SEARCH RESULTS: {len(chunks)} chunks found")
        
        if not chunks:
            return "No relevant information found in the uploaded documents."

        return "\n\n".join(
            f"[Source: {chunk['source']}, Page: {chunk['page']}]\n{chunk['content']}"
            for chunk in chunks[:5]
        )

    return search_documents