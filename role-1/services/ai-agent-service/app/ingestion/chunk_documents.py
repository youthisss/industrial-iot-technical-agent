def chunk_documents(documents: list[str], chunk_size: int = 800) -> list[str]:
    chunks: list[str] = []
    for document in documents:
        for index in range(0, len(document), chunk_size):
            chunks.append(document[index : index + chunk_size])
    return chunks
