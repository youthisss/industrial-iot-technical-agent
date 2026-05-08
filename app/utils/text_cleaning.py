import re


def normalize_whitespace(text: str) -> str:
    """Collapse repeated whitespace into single spaces."""
    return re.sub(r"\s+", " ", text).strip()
