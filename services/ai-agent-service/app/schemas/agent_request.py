from pydantic import BaseModel


class TroubleshootRequest(BaseModel):
    request_id: str
    machine_id: str
    plc_type: str
    error_code: str
    message: str
    image_url: str | None = None


class MaintenanceHistoryItem(BaseModel):
    root_cause: str | None = None
    solution_applied: str | None = None
    success_status: bool | None = None


class UnresolvedRequest(BaseModel):
    request_id: str
    machine_id: str
    error_code: str
    attempted_solution: str
    maintenance_history: list[MaintenanceHistoryItem] = []
