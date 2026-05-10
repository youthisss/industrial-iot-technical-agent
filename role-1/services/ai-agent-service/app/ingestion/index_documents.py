from app.ingestion.chunk_documents import chunk_documents
from app.ingestion.embed_documents import embed_documents
from app.ingestion.load_documents import load_documents


def index_documents(path: str) -> dict[str, int]:
    documents = load_documents(path)
    chunks = chunk_documents(documents)
    embedded = embed_documents(chunks)
    return {"documents": len(documents), "chunks": len(embedded)}
