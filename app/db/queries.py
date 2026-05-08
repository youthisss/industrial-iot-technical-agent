from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import IncidentLog, MaintenanceHistory, Machine


def get_machine_by_machine_id(session: Session, machine_id: str) -> Machine | None:
    """Fetch one machine by business machine id."""
    return session.execute(select(Machine).where(Machine.machine_id == machine_id)).scalar_one_or_none()


def get_maintenance_history(
    session: Session,
    machine_id: str,
    error_code: str,
) -> list[MaintenanceHistory]:
    """Fetch maintenance records by machine and error code."""
    statement = (
        select(MaintenanceHistory)
        .where(MaintenanceHistory.machine_id == machine_id)
        .where(MaintenanceHistory.error_code == error_code)
        .order_by(MaintenanceHistory.created_at.desc())
    )
    return list(session.execute(statement).scalars().all())


def create_incident_log(session: Session, incident: IncidentLog) -> IncidentLog:
    """Persist an incident log."""
    session.add(incident)
    session.commit()
    session.refresh(incident)
    return incident
