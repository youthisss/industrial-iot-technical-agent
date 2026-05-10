# Entity Relationship Diagram

```text
machines
  id PK
  machine_id UNIQUE
  machine_name
  location
  plc_type

maintenance_history
  id PK
  machine_id
  error_code
  root_cause
  solution_applied
  success_status
  downtime_minutes
  technician_notes
  created_at

incident_logs
  id PK
  machine_id
  error_code
  issue_summary
  ai_recommendation
  escalation_status
  created_at
```

Logical relationships:

- `machines.machine_id` identifies a physical PLC-controlled asset.
- `maintenance_history.machine_id` stores historical repair records for a machine.
- `incident_logs.machine_id` stores AI-assisted troubleshooting incidents and escalation status.
