import json
from pathlib import Path

from app.tools.n8n_tool import N8NTool


def test_n8n_tool_dry_run_when_no_webhook():
    tool = N8NTool(webhook_url="")
    payload = {"machine_id": "PLC-001", "error_code": "E-STOP"}

    result = tool.send_payload(payload)

    assert result["sent"] is False
    assert result["mode"] == "dry_run"


def test_sample_incident_payload_is_valid_json():
    payload_path = Path("n8n/payload_examples/incident_payload.json")
    payload = json.loads(payload_path.read_text(encoding="utf-8"))

    assert payload["machine_id"] == "PLC-001"
    assert "ai_recommendation" in payload
