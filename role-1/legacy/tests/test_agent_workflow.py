from app.agents.maintenance_agent import MaintenanceAgent


class FakeRAGTool:
    def search(self, query: str, limit: int = 3) -> list[dict]:
        return [{"source": "manual", "content": "check safety relay", "score": 1.0}]


class FakeSQLHistoryTool:
    def get_history(self, machine_id: str, error_code: str) -> list[dict]:
        return [{"machine_id": machine_id, "error_code": error_code}]


class FakeVisionTool:
    def analyze_image(self, image_path: str, prompt: str) -> str:
        return "image shows PLC panel"


class FakeN8NTool:
    def send_payload(self, payload: dict) -> dict:
        return {"sent": False, "mode": "dry_run"}


class FakeSafetyTool:
    def check_instruction_risk(self, instruction: str) -> str:
        return "normal"


def build_agent() -> MaintenanceAgent:
    return MaintenanceAgent(
        rag_tool=FakeRAGTool(),
        sql_history_tool=FakeSQLHistoryTool(),
        vision_tool=FakeVisionTool(),
        n8n_tool=FakeN8NTool(),
        safety_tool=FakeSafetyTool(),
    )


def test_agent_text_workflow_returns_response():
    response = build_agent().run_text_query(
        machine_id="PLC-001",
        plc_type="Siemens S7-1200",
        error_code="E-STOP",
        query="What should I check?",
    )

    assert response["machine_id"] == "PLC-001"
    assert response["retrieved_sources"]
    assert "Verify safe lockout" in response["answer"]


def test_agent_escalates_incident():
    response = build_agent().escalate_incident(
        machine_id="PLC-001",
        error_code="E-STOP",
        issue_summary="Unresolved stop",
        ai_recommendation="Escalate to lead",
    )

    assert response["status"] == "escalated"
    assert response["payload"]["escalation_status"] == "escalated"


def test_agent_logs_unresolved_issue():
    response = build_agent().handle_unresolved_issue(
        machine_id="PLC-001",
        error_code="E-STOP",
        issue_summary="Unresolved stop",
        ai_recommendation="Escalate to lead",
    )

    assert response["status"] == "unresolved_logged"
    assert response["payload"]["escalation_status"] == "pending"
