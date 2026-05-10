from fastapi import FastAPI

from app.api.routes_chat import router as chat_router
from app.api.routes_health import router as health_router
from app.api.routes_incidents import router as incidents_router
from app.api.routes_upload import router as upload_router
from app.config import get_settings
from app.db.session import init_db


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    api = FastAPI(
        title="PLC Troubleshooting Agent",
        description="AI agent API for PLC troubleshooting with RAG, SQL memory, vision, and n8n.",
        version="0.1.0",
        debug=settings.app_env == "development",
    )
    api.include_router(health_router)
    api.include_router(chat_router)
    api.include_router(upload_router)
    api.include_router(incidents_router)

    @api.on_event("startup")
    def on_startup() -> None:
        if settings.app_env != "test":
            init_db()

    return api


app = create_app()
