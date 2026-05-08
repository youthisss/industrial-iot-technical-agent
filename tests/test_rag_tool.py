from app.services.vector_store_service import VectorStoreService
from app.tools.rag_tool import RAGTool


def test_rag_tool_returns_documents(tmp_path):
    store = VectorStoreService(storage_path=tmp_path / "chunks.json")
    store.add_documents(
        [
            {
                "source": "manual.md#chunk-0",
                "content": "Emergency stop reset requires safety relay inspection.",
            }
        ]
    )
    tool = RAGTool(vector_store_service=store)

    results = tool.search("emergency stop")

    assert results
    assert results[0]["source"] == "manual.md#chunk-0"
