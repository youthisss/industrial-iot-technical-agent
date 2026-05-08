from app.agents.graph import MaintenanceGraph
from app.schemas.agent_request import TroubleshootRequest, UnresolvedRequest
from app.schemas.agent_response import AgentResponse, RetrievedSource
from app.tools.history_lookup_tool import HistoryLookupTool
from app.tools.rag_tool import RagTool
from app.tools.safety_tool import SafetyTool
from app.tools.vision_tool import VisionTool


class MaintenanceAgent:
    def __init__(self) -> None:
        self.graph = MaintenanceGraph(
            rag_tool=RagTool(),
            vision_tool=VisionTool(),
            history_tool=HistoryLookupTool(),
            safety_tool=SafetyTool(),
        )

    def run_initial(self, request: TroubleshootRequest) -> AgentResponse:
        state = self.graph.run_initial(request.model_dump())
        return AgentResponse(
            request_id=request.request_id,
            recommendation_level="initial",
            summary=state["summary"],
            recommended_action=state["recommended_action"],
            safety_warning=state["safety_warning"],
            retrieved_sources=[RetrievedSource(**source) for source in state["retrieved_sources"]],
            confidence_score=0.82,
        )

    def run_unresolved(self, request: UnresolvedRequest) -> AgentResponse:
        state = self.graph.run_unresolved(request.model_dump())
        return AgentResponse(
            request_id=request.request_id,
            recommendation_level="second_level",
            summary=state["summary"],
            recommended_action=state["recommended_action"],
            safety_warning=state["safety_warning"],
            retrieved_sources=[],
            confidence_score=0.87,
        )
