from fastapi import APIRouter, Depends

from app.agents.maintenance_agent import MaintenanceAgent
from app.api.schemas import IncidentActionRequest, IncidentActionResponse
from app.dependencies import get_agent

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.post("/unresolved", response_model=IncidentActionResponse)
def mark_unresolved(
    request: IncidentActionRequest,
    agent: MaintenanceAgent = Depends(get_agent),
) -> IncidentActionResponse:
    """Log an unresolved troubleshooting issue through the agent automation layer."""
    result = agent.handle_unresolved_issue(
        machine_id=request.machine_id,
        error_code=request.error_code,
        issue_summary=request.issue_summary,
        ai_recommendation=request.ai_recommendation,
    )
    return IncidentActionResponse(**result)


@router.post("/escalate", response_model=IncidentActionResponse)
def escalate_incident(
    request: IncidentActionRequest,
    agent: MaintenanceAgent = Depends(get_agent),
) -> IncidentActionResponse:
    """Escalate an unresolved troubleshooting issue through n8n-ready automation."""
    result = agent.escalate_incident(
        machine_id=request.machine_id,
        error_code=request.error_code,
        issue_summary=request.issue_summary,
        ai_recommendation=request.ai_recommendation,
    )
    return IncidentActionResponse(**result)
