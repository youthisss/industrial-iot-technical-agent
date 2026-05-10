from app.agents.state import AgentState
from app.config import get_settings
from app.retrievers.pgvector_retriever import PgvectorRetriever
from app.retrievers.pinecone_retriever import PineconeRetriever


class RagTool:
    def __init__(self) -> None:
        settings = get_settings()
        self.retriever = (
            PineconeRetriever()
            if settings.vector_store_provider == "pinecone"
            else PgvectorRetriever()
        )

    def retrieve(self, state: AgentState) -> list[dict[str, object]]:
        query = " ".join(
            str(state.get(key, ""))
            for key in ("machine_id", "plc_type", "error_code", "message", "image_summary")
        )
        return self.retriever.search(query=query, limit=3)
