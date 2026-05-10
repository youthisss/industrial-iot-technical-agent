from app.tools.sql_history_tool import SQLHistoryTool


class FakeHistoryService:
    def get_history(self, machine_id: str, error_code: str) -> list[dict]:
        return [{"machine_id": machine_id, "error_code": error_code, "success_status": True}]


def test_sql_history_tool_returns_history():
    tool = SQLHistoryTool(history_service=FakeHistoryService())

    history = tool.get_history(machine_id="PLC-001", error_code="E-STOP")

    assert history[0]["machine_id"] == "PLC-001"
    assert history[0]["success_status"] is True
