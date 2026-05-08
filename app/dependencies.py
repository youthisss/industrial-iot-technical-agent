from app.agents.maintenance_agent import MaintenanceAgent
from app.config import Settings, get_settings
from app.services.maintenance_history_service import MaintenanceHistoryService
from app.services.vector_store_service import VectorStoreService
from app.services.vision_service import VisionService
from app.tools.n8n_tool import N8NTool
from app.tools.rag_tool import RAGTool
from app.tools.safety_tool import SafetyTool
from app.tools.sql_history_tool import SQLHistoryTool
from app.tools.vision_tool import VisionTool


def get_agent() -> MaintenanceAgent:
    """Build the current agent with mock-friendly production interfaces."""
    settings: Settings = get_settings()
    vector_store = VectorStoreService(settings=settings)
    history_service = MaintenanceHistoryService()
    vision_service = VisionService(settings=settings)

    return MaintenanceAgent(
        rag_tool=RAGTool(vector_store_service=vector_store),
        sql_history_tool=SQLHistoryTool(history_service=history_service),
        vision_tool=VisionTool(vision_service=vision_service),
        n8n_tool=N8NTool(webhook_url=settings.n8n_webhook_url),
        safety_tool=SafetyTool(),
    )
