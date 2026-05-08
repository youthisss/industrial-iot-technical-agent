from fastapi import FastAPI

from app.agents.maintenance_agent import MaintenanceAgent
from app.config import get_settings
from app.schemas.agent_request import TroubleshootRequest, UnresolvedRequest
from app.schemas.agent_response import AgentResponse

settings = get_settings()
agent = MaintenanceAgent()

app = FastAPI(title="AI Agent Service", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": settings.service_name}


@app.post("/agent/troubleshoot", response_model=AgentResponse)
def troubleshoot(request: TroubleshootRequest) -> AgentResponse:
    return agent.run_initial(request)


@app.post("/agent/unresolved", response_model=AgentResponse)
def unresolved(request: UnresolvedRequest) -> AgentResponse:
    return agent.run_unresolved(request)
