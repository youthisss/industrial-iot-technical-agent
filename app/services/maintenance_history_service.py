from sqlalchemy import select

from app.db.models import MaintenanceHistory
from app.db.session import SessionLocal


class MaintenanceHistoryService:
    """Query maintenance history from the database."""

    def get_history(self, machine_id: str, error_code: str) -> list[dict]:
        """Return matching maintenance history or a demo fallback record."""
        try:
            with SessionLocal() as session:
                statement = (
                    select(MaintenanceHistory)
                    .where(MaintenanceHistory.machine_id == machine_id)
                    .where(MaintenanceHistory.error_code == error_code)
                    .order_by(MaintenanceHistory.created_at.desc())
                )
                records = session.execute(statement).scalars().all()
                return [record.to_dict() for record in records]
        except Exception:
            if machine_id == "PLC-001":
                return [
                    {
                        "machine_id": machine_id,
                        "error_code": error_code,
                        "root_cause": "Emergency stop circuit was not fully reset.",
                        "solution_applied": "Verified E-stop chain and reset safety relay.",
                        "success_status": True,
                        "downtime_minutes": 18,
                        "technician_notes": "Check safety relay indicator before restarting.",
                    }
                ]
            return []
