from app.agents.workflow import build_initial_state
from app.tools.n8n_tool import N8NTool
from app.tools.rag_tool import RAGTool
from app.tools.safety_tool import SafetyTool
from app.tools.sql_history_tool import SQLHistoryTool
from app.tools.vision_tool import VisionTool


class MaintenanceAgent:
    """Main PLC troubleshooting agent.

    The class currently uses simple deterministic logic but keeps the interfaces
    ready for LangChain tools, chains, or a graph-based agent workflow.
    """

    def __init__(
        self,
        rag_tool: RAGTool,
        sql_history_tool: SQLHistoryTool,
        vision_tool: VisionTool,
        n8n_tool: N8NTool,
        safety_tool: SafetyTool,
    ) -> None:
        self.rag_tool = rag_tool
        self.sql_history_tool = sql_history_tool
        self.vision_tool = vision_tool
        self.n8n_tool = n8n_tool
        self.safety_tool = safety_tool

    def run_text_query(
        self,
        machine_id: str,
        plc_type: str,
        error_code: str,
        query: str,
    ) -> dict:
        """Run a text troubleshooting query."""
        state = build_initial_state(
            machine_id=machine_id,
            plc_type=plc_type,
            error_code=error_code,
            query=query,
        )
        state.safety_level = self.safety_tool.check_instruction_risk(query)
        state.retrieved_sources = self.rag_tool.search(query=query)
        state.maintenance_history = self.sql_history_tool.get_history(
            machine_id=machine_id,
            error_code=error_code,
        )

        source_hint = "No manual source was found."
        if state.retrieved_sources:
            source_hint = f"Most relevant source: {state.retrieved_sources[0]['source']}."

        history_hint = "No prior maintenance history was found."
        if state.maintenance_history:
            history_hint = (
                f"Found {len(state.maintenance_history)} prior maintenance record(s) "
                f"for {machine_id} and {error_code}."
            )

        if state.safety_level == "high":
            recommendation = "Stop and escalate before attempting high-risk electrical work."
        else:
            recommendation = (
                "Verify safe lockout status, inspect the PLC diagnostic code, "
                "check wiring and sensor state, then compare against the cited manual section."
            )

        state.answer = f"{recommendation} {source_hint} {history_hint}"
        return self._state_to_response(state)

    def run_multimodal_query(
        self,
        machine_id: str,
        plc_type: str,
        error_code: str,
        query: str,
        image_path: str,
    ) -> dict:
        """Run troubleshooting with text and image context."""
        result = self.run_text_query(
            machine_id=machine_id,
            plc_type=plc_type,
            error_code=error_code,
            query=query,
        )
        vision_summary = self.vision_tool.analyze_image(
            image_path=image_path,
            prompt=f"Analyze PLC panel evidence for {plc_type} error {error_code}.",
        )
        result["answer"] = f"{result['answer']} Visual inspection summary: {vision_summary}"
        return result

    def handle_unresolved_issue(
        self,
        machine_id: str,
        error_code: str,
        issue_summary: str,
        ai_recommendation: str,
    ) -> dict:
        """Create a local incident-style response when the issue remains unresolved."""
        payload = {
            "machine_id": machine_id,
            "error_code": error_code,
            "issue_summary": issue_summary,
            "ai_recommendation": ai_recommendation,
            "escalation_status": "pending",
        }
        n8n_result = self.n8n_tool.send_payload(payload=payload)
        return {"status": "unresolved_logged", "automation": n8n_result, "payload": payload}

    def escalate_incident(
        self,
        machine_id: str,
        error_code: str,
        issue_summary: str,
        ai_recommendation: str,
    ) -> dict:
        """Escalate an incident through the configured n8n webhook."""
        payload = {
            "machine_id": machine_id,
            "error_code": error_code,
            "issue_summary": issue_summary,
            "ai_recommendation": ai_recommendation,
            "escalation_status": "escalated",
            "notify": ["maintenance_lead", "operations_manager"],
        }
        n8n_result = self.n8n_tool.send_payload(payload=payload)
        return {"status": "escalated", "automation": n8n_result, "payload": payload}

    @staticmethod
    def _state_to_response(state: object) -> dict:
        """Convert agent state to API response shape."""
        return {
            "answer": state.answer,
            "machine_id": state.machine_id,
            "error_code": state.error_code,
            "safety_level": state.safety_level,
            "retrieved_sources": state.retrieved_sources,
            "maintenance_history": state.maintenance_history,
            "incident_id": None,
        }
