from sentence_transformers import SentenceTransformer

class EmbeddingManager:
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        print(f"Loading embedding model: {self.model_name}")
        self.model = SentenceTransformer(self.model_name)
        print(f"Embedding dimensions: {self.model.get_sentence_embedding_dimension()}")

    def generate_embeddings(self, texts: list[str]):
        embeddings = self.model.encode(texts, show_progress_bar=True)
        return embeddings  

    def generate_single(self, text: str):
        return self.model.encode([text])[0]

embedding_manager = EmbeddingManager()
