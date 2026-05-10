from app.agents.state import AgentState


class SafetyTool:
    def apply(self, state: AgentState) -> AgentState:
        state["safety_warning"] = "Follow lockout/tagout and de-energize the panel before inspection."
        return state
