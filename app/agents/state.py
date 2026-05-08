from dataclasses import dataclass, field


@dataclass
class AgentState:
    """Lightweight state container for a troubleshooting turn."""

    machine_id: str
    plc_type: str
    error_code: str
    query: str
    image_path: str | None = None
    retrieved_sources: list[dict] = field(default_factory=list)
    maintenance_history: list[dict] = field(default_factory=list)
    safety_level: str = "normal"
    answer: str = ""
