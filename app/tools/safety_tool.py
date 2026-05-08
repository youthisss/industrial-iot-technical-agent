class SafetyTool:
    """Classify troubleshooting instructions by risk."""

    HIGH_RISK_TERMS = {
        "bypass interlock",
        "disable guard",
        "live wire",
        "remove lockout",
        "override safety",
        "short circuit",
    }

    def check_instruction_risk(self, instruction: str) -> str:
        """Return high when the instruction includes risky electrical or safety actions."""
        normalized = instruction.lower()
        if any(term in normalized for term in self.HIGH_RISK_TERMS):
            return "high"
        return "normal"
