from typing import TypedDict


class AgentState(TypedDict, total=False):
    request_id: str
    machine_id: str
    plc_type: str
    error_code: str
    message: str
    image_url: str | None
    image_summary: str
    retrieved_sources: list[dict[str, object]]
    recommendation_level: str
    summary: str
    recommended_action: str
    safety_warning: str
    confidence_score: float
