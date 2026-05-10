from fastapi import APIRouter, Depends

from app.agents.maintenance_agent import MaintenanceAgent
from app.api.schemas import ChatRequest, ChatResponse
from app.dependencies import get_agent

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    agent: MaintenanceAgent = Depends(get_agent),
) -> ChatResponse:
    """Run a troubleshooting query through the maintenance agent."""
    if request.image_path:
        result = agent.run_multimodal_query(
            machine_id=request.machine_id,
            plc_type=request.plc_type,
            error_code=request.error_code,
            query=request.message,
            image_path=request.image_path,
        )
    else:
        result = agent.run_text_query(
            machine_id=request.machine_id,
            plc_type=request.plc_type,
            error_code=request.error_code,
            query=request.message,
        )
    return ChatResponse(**result)
