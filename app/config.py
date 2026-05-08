from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    database_url: str = Field(
        default="sqlite:///./plc_agent_dev.db",
        alias="DATABASE_URL",
    )
    chroma_host: str = Field(default="localhost", alias="CHROMA_HOST")
    chroma_port: int = Field(default=8001, alias="CHROMA_PORT")
    n8n_webhook_url: str = Field(default="", alias="N8N_WEBHOOK_URL")
    app_env: str = Field(default="development", alias="APP_ENV")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache
def get_settings() -> Settings:
    """Return cached settings."""
    return Settings()
