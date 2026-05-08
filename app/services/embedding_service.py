import hashlib


class EmbeddingService:
    """Create deterministic placeholder embeddings for local demos."""

    def embed_text(self, text: str) -> list[float]:
        """Return a small deterministic vector for text.

        Replace this with OpenAI embeddings in production.
        """
        digest = hashlib.sha256(text.encode("utf-8")).digest()
        return [byte / 255 for byte in digest[:16]]
