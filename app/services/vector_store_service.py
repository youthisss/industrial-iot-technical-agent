import json
from pathlib import Path

from app.config import Settings, get_settings
from app.services.embedding_service import EmbeddingService


class VectorStoreService:
    """ChromaDB-ready vector store with a local JSON fallback."""

    def __init__(
        self,
        settings: Settings | None = None,
        storage_path: str | Path = "data/vector_store/chunks.json",
    ) -> None:
        self.settings = settings or get_settings()
        self.storage_path = Path(storage_path)
        self.embedding_service = EmbeddingService()

    def add_documents(self, documents: list[dict]) -> int:
        """Store document chunks in the local fallback store."""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        existing = self._load()
        existing.extend(documents)
        self.storage_path.write_text(json.dumps(existing, indent=2), encoding="utf-8")
        return len(documents)

    def search(self, query: str, limit: int = 3) -> list[dict]:
        """Return simple keyword-ranked document chunks."""
        documents = self._load()
        if not documents:
            return [
                {
                    "source": "mock://plc-troubleshooting",
                    "content": "Check PLC diagnostics, wiring, sensor state, and safety interlocks.",
                    "score": 0.1,
                }
            ]

        query_terms = {term.lower() for term in query.split() if len(term) > 2}
        ranked: list[dict] = []
        for doc in documents:
            content = str(doc.get("content", ""))
            content_terms = content.lower()
            score = sum(1 for term in query_terms if term in content_terms)
            ranked.append(
                {
                    "source": str(doc.get("source", "unknown")),
                    "content": content[:600],
                    "score": float(score),
                }
            )
        ranked.sort(key=lambda item: item["score"], reverse=True)
        return ranked[:limit]

    def _load(self) -> list[dict]:
        if not self.storage_path.exists():
            return []
        return json.loads(self.storage_path.read_text(encoding="utf-8"))
