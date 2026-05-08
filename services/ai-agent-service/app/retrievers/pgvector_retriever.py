class PgvectorRetriever:
    def search(self, query: str, limit: int = 3) -> list[dict[str, object]]:
        return [
            {
                "source_name": "siemens_s7_manual.pdf",
                "page": 42,
                "snippet": "pgvector adapter placeholder for OB82 diagnostic interrupt retrieval.",
            }
        ][:limit]
