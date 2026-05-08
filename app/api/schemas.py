from pydantic import BaseModel, Field


class SourceDocument(BaseModel):
    """Document source returned by RAG."""

    source: str
    content: str
    score: float = 0.0


class ChatRequest(BaseModel):
    """Request body for text-based troubleshooting."""

    machine_id: str = Field(..., examples=["PLC-001"])
    plc_type: str = Field(..., examples=["Siemens S7-1200"])
    error_code: str = Field(..., examples=["E-STOP"])
    message: str = Field(..., examples=["Machine stopped after emergency stop reset."])
    image_path: str | None = None


class ChatResponse(BaseModel):
    """Agent response for troubleshooting requests."""

    answer: str
    machine_id: str
    error_code: str
    safety_level: str = "normal"
    retrieved_sources: list[SourceDocument] = Field(default_factory=list)
    maintenance_history: list[dict] = Field(default_factory=list)
    incident_id: str | None = None


class IncidentActionRequest(BaseModel):
    """Request body for unresolved and escalation incident actions."""

    machine_id: str = Field(..., examples=["PLC-001"])
    error_code: str = Field(..., examples=["E-STOP"])
    issue_summary: str = Field(..., examples=["Emergency stop remains active after reset."])
    ai_recommendation: str = Field(
        ...,
        examples=["Verify lockout status, inspect the safety relay, then escalate if unresolved."],
    )


class IncidentActionResponse(BaseModel):
    """Incident action response returned by the agent automation layer."""

    status: str
    automation: dict
    payload: dict


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    service: str
    environment: str


class UploadImageResponse(BaseModel):
    """Image upload response."""

    filename: str
    saved_path: str
    content_type: str | None = None
