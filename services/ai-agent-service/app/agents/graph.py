from app.agents.state import AgentState
from app.tools.history_lookup_tool import HistoryLookupTool
from app.tools.rag_tool import RagTool
from app.tools.safety_tool import SafetyTool
from app.tools.vision_tool import VisionTool


class MaintenanceGraph:
    nodes = (
        "input_parser",
        "vision_analyzer",
        "document_retriever",
        "first_recommendation_generator",
        "safety_checker",
        "history_lookup_requester",
        "second_recommendation_generator",
        "response_formatter",
        "evaluation_logger",
    )

    edges = (
        ("input_parser", "vision_analyzer"),
        ("input_parser", "document_retriever"),
        ("vision_analyzer", "document_retriever"),
        ("document_retriever", "first_recommendation_generator"),
        ("first_recommendation_generator", "safety_checker"),
        ("safety_checker", "response_formatter"),
        ("response_formatter", "evaluation_logger"),
        ("history_lookup_requester", "second_recommendation_generator"),
        ("second_recommendation_generator", "safety_checker"),
    )

    def __init__(
        self,
        rag_tool: RagTool,
        vision_tool: VisionTool,
        history_tool: HistoryLookupTool,
        safety_tool: SafetyTool,
    ) -> None:
        self.rag_tool = rag_tool
        self.vision_tool = vision_tool
        self.history_tool = history_tool
        self.safety_tool = safety_tool

    def run_initial(self, state: AgentState) -> AgentState:
        if state.get("image_url"):
            state["image_summary"] = self.vision_tool.analyze(str(state["image_url"]))
        state["retrieved_sources"] = self.rag_tool.retrieve(state)
        state["recommendation_level"] = "initial"
        state["summary"] = "The OB82 error indicates a diagnostic interrupt from an I/O module."
        state["recommended_action"] = (
            "Inspect the diagnostic buffer, I/O module state, and connected sensor wiring."
        )
        return self.safety_tool.apply(state)

    def run_unresolved(self, state: AgentState) -> AgentState:
        self.history_tool.request_history(str(state.get("machine_id", "")), str(state.get("error_code", "")))
        state["recommendation_level"] = "second_level"
        state["summary"] = "Previous similar cases suggest the digital input module may be faulty."
        state["recommended_action"] = (
            "Inspect and test the DI module connected to the affected sensor line."
        )
        return self.safety_tool.apply(state)
