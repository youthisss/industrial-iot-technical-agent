class HistoryLookupTool:
    def request_history(self, machine_id: str, error_code: str) -> dict[str, str]:
        return {
            "machine_id": machine_id,
            "error_code": error_code,
            "source": "go-api-gateway",
            "status": "history_requested",
        }
