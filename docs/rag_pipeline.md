# RAG Pipeline

The starter RAG pipeline is intentionally simple and easy to replace.

## Steps

1. Documents are placed in `data/sample_manuals`.
2. `ingestion/load_docs.py` reads markdown and text files.
3. `ingestion/chunk_documents.py` creates overlapping chunks.
4. `ingestion/ingest_documents.py` stores chunks through `VectorStoreService`.
5. `RAGTool` searches chunks for relevant troubleshooting context.

## Run

```bash
python ingestion/ingest_documents.py
```

## Future Improvements

- Add PDF parsing.
- Use OpenAI embeddings.
- Store embeddings in ChromaDB collections.
- Track source title, page number, section, and revision metadata.
- Add retrieval evaluation tests.
