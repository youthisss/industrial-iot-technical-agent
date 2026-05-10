def embed_documents(chunks: list[str]) -> list[dict[str, object]]:
    return [{"text": chunk, "embedding": [0.0, 0.0, 0.0]} for chunk in chunks]
