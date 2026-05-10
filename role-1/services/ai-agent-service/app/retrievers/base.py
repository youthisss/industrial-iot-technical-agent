from typing import Protocol


class Retriever(Protocol):
    def search(self, query: str, limit: int = 3) -> list[dict[str, object]]:
        ...
