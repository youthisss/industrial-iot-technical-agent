from pathlib import Path


def load_documents(path: str) -> list[str]:
    source = Path(path)
    if not source.exists():
        return []
    return [file.read_text(encoding="utf-8") for file in source.glob("*.md")]
