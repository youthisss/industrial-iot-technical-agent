from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class Machine(Base):
    """Machine inventory table."""

    __tablename__ = "machines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    machine_id: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    machine_name: Mapped[str] = mapped_column(String(160))
    location: Mapped[str] = mapped_column(String(160))
    plc_type: Mapped[str] = mapped_column(String(160))

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "machine_id": self.machine_id,
            "machine_name": self.machine_name,
            "location": self.location,
            "plc_type": self.plc_type,
        }


class MaintenanceHistory(Base):
    """Past maintenance records."""

    __tablename__ = "maintenance_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    machine_id: Mapped[str] = mapped_column(String(80), index=True)
    error_code: Mapped[str] = mapped_column(String(80), index=True)
    root_cause: Mapped[str] = mapped_column(Text)
    solution_applied: Mapped[str] = mapped_column(Text)
    success_status: Mapped[bool] = mapped_column(Boolean, default=False)
    downtime_minutes: Mapped[int] = mapped_column(Integer, default=0)
    technician_notes: Mapped[str] = mapped_column(Text, default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "machine_id": self.machine_id,
            "error_code": self.error_code,
            "root_cause": self.root_cause,
            "solution_applied": self.solution_applied,
            "success_status": self.success_status,
            "downtime_minutes": self.downtime_minutes,
            "technician_notes": self.technician_notes,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class IncidentLog(Base):
    """Incident logs created by the agent."""

    __tablename__ = "incident_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    machine_id: Mapped[str] = mapped_column(String(80), index=True)
    error_code: Mapped[str] = mapped_column(String(80), index=True)
    issue_summary: Mapped[str] = mapped_column(Text)
    ai_recommendation: Mapped[str] = mapped_column(Text)
    escalation_status: Mapped[str] = mapped_column(String(80), default="pending")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "machine_id": self.machine_id,
            "error_code": self.error_code,
            "issue_summary": self.issue_summary,
            "ai_recommendation": self.ai_recommendation,
            "escalation_status": self.escalation_status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
