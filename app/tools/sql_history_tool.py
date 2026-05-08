from app.services.maintenance_history_service import MaintenanceHistoryService


class SQLHistoryTool:
    """Retrieve machine maintenance history from SQL storage."""

    def __init__(self, history_service: MaintenanceHistoryService) -> None:
        self.history_service = history_service

    def get_history(self, machine_id: str, error_code: str) -> list[dict]:
        """Return maintenance records for the machine and error code."""
        return self.history_service.get_history(machine_id=machine_id, error_code=error_code)
