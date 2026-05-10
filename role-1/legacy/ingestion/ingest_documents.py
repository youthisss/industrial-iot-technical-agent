from pathlib import Path

from app.services.vector_store_service import VectorStoreService
from ingestion.chunk_documents import chunk_text
from ingestion.load_docs import load_docs


def ingest_documents(source_dir: str | Path = "data/sample_manuals") -> int:
    """Read manual documents, chunk them, and store them in the vector store."""
    documents = load_docs(source_dir)
    chunks: list[dict] = []
    for document in documents:
        for index, chunk in enumerate(chunk_text(document["content"])):
            chunks.append(
                {
                    "source": f"{document['source']}#chunk-{index}",
                    "content": chunk,
                }
            )

    vector_store = VectorStoreService()
    return vector_store.add_documents(chunks)


if __name__ == "__main__":
    count = ingest_documents()
    print(f"Ingested {count} document chunks.")
