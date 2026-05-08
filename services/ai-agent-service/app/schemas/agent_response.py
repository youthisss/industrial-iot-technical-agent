from pydantic import BaseModel


class RetrievedSource(BaseModel):
    source_name: str
    page: int | None = None
    snippet: str


class AgentResponse(BaseModel):
    request_id: str
    recommendation_level: str
    summary: str
    recommended_action: str
    safety_warning: str
    retrieved_sources: list[RetrievedSource] = []
    confidence_score: float
