from pathlib import Path


class DocumentService:
    """Load local technical documents."""

    SUPPORTED_EXTENSIONS = {".md", ".txt"}

    def load_documents(self, directory: str | Path) -> list[dict]:
        """Read supported files from a directory."""
        base_path = Path(directory)
        documents: list[dict] = []
        if not base_path.exists():
            return documents

        for path in sorted(base_path.rglob("*")):
            if path.is_file() and path.suffix.lower() in self.SUPPORTED_EXTENSIONS:
                documents.append({"source": str(path), "content": path.read_text(encoding="utf-8")})
        return documents
