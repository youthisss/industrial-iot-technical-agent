from app.db.models import IncidentLog
from app.db.session import SessionLocal


class IncidentService:
    """Create incident logs in SQL storage."""

    def create_incident(
        self,
        machine_id: str,
        error_code: str,
        issue_summary: str,
        ai_recommendation: str,
        escalation_status: str = "pending",
    ) -> dict:
        """Persist an incident log and return its data."""
        with SessionLocal() as session:
            incident = IncidentLog(
                machine_id=machine_id,
                error_code=error_code,
                issue_summary=issue_summary,
                ai_recommendation=ai_recommendation,
                escalation_status=escalation_status,
            )
            session.add(incident)
            session.commit()
            session.refresh(incident)
            return incident.to_dict()
