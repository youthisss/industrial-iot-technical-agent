CREATE TABLE IF NOT EXISTS machines (
    id SERIAL PRIMARY KEY,
    machine_id VARCHAR(80) UNIQUE NOT NULL,
    machine_name VARCHAR(160) NOT NULL,
    location VARCHAR(160) NOT NULL,
    plc_type VARCHAR(160) NOT NULL
);

CREATE TABLE IF NOT EXISTS maintenance_history (
    id SERIAL PRIMARY KEY,
    machine_id VARCHAR(80) NOT NULL,
    error_code VARCHAR(80) NOT NULL,
    root_cause TEXT NOT NULL,
    solution_applied TEXT NOT NULL,
    success_status BOOLEAN NOT NULL DEFAULT FALSE,
    downtime_minutes INTEGER NOT NULL DEFAULT 0,
    technician_notes TEXT NOT NULL DEFAULT '',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS incident_logs (
    id SERIAL PRIMARY KEY,
    machine_id VARCHAR(80) NOT NULL,
    error_code VARCHAR(80) NOT NULL,
    issue_summary TEXT NOT NULL,
    ai_recommendation TEXT NOT NULL,
    escalation_status VARCHAR(80) NOT NULL DEFAULT 'pending',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_maintenance_machine_error
    ON maintenance_history (machine_id, error_code);

CREATE INDEX IF NOT EXISTS idx_incident_machine_error
    ON incident_logs (machine_id, error_code);
