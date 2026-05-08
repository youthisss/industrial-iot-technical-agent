from app.agents.state import AgentState


def build_initial_state(
    machine_id: str,
    plc_type: str,
    error_code: str,
    query: str,
    image_path: str | None = None,
) -> AgentState:
    """Create the initial workflow state for future LangChain or LangGraph integration."""
    return AgentState(
        machine_id=machine_id,
        plc_type=plc_type,
        error_code=error_code,
        query=query,
        image_path=image_path,
    )
