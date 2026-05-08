from app.services.vector_store_service import VectorStoreService


class RAGTool:
    """Search technical documents from the vector store."""

    def __init__(self, vector_store_service: VectorStoreService) -> None:
        self.vector_store_service = vector_store_service

    def search(self, query: str, limit: int = 3) -> list[dict]:
        """Return relevant document chunks for a query."""
        return self.vector_store_service.search(query=query, limit=limit)
