from dataclasses import dataclass
from functools import lru_cache
import os


@dataclass(frozen=True)
class Settings:
    service_name: str = "ai-agent-service"
    app_env: str = os.getenv("APP_ENV", "local")
    langsmith_project: str = os.getenv("LANGSMITH_PROJECT", "plc-troubleshooting-agent")
    pinecone_index_name: str = os.getenv("PINECONE_INDEX_NAME", "plc-technical-docs")
    vector_store_provider: str = os.getenv("VECTOR_STORE_PROVIDER", "pgvector")


@lru_cache
def get_settings() -> Settings:
    return Settings()
