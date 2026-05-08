from pathlib import Path

from app.services.document_service import DocumentService


def load_docs(directory: str | Path) -> list[dict]:
    """Load markdown and text documents from a directory."""
    return DocumentService().load_documents(directory=directory)
