from fastapi import APIRouter

from app.api.schemas import HealthResponse
from app.config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Return service health status."""
    settings = get_settings()
    return HealthResponse(
        status="ok",
        service="plc-troubleshooting-agent",
        environment=settings.app_env,
    )
