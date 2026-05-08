CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS machines (
    id UUID PRIMARY KEY,
    machine_id VARCHAR(100) UNIQUE NOT NULL,
    machine_name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    plc_type VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS maintenance_history (
    id UUID PRIMARY KEY,
    machine_id VARCHAR(100) NOT NULL,
    error_code VARCHAR(100) NOT NULL,
    root_cause TEXT,
    solution_applied TEXT,
    success_status BOOLEAN,
    downtime_minutes INTEGER,
    technician_notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS incident_logs (
    id UUID PRIMARY KEY,
    machine_id VARCHAR(100) NOT NULL,
    plc_type VARCHAR(255),
    error_code VARCHAR(100),
    issue_summary TEXT,
    ai_recommendation TEXT,
    priority VARCHAR(50) NOT NULL DEFAULT 'medium',
    status VARCHAR(50) NOT NULL DEFAULT 'open',
    escalation_status VARCHAR(50) NOT NULL DEFAULT 'not_escalated',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS agent_runs (
    id UUID PRIMARY KEY,
    request_id VARCHAR(100) UNIQUE NOT NULL,
    incident_id UUID,
    machine_id VARCHAR(100),
    error_code VARCHAR(100),
    recommendation_level VARCHAR(50),
    confidence_score NUMERIC(5, 4),
    latency_ms INTEGER,
    tool_call_success BOOLEAN,
    safety_passed BOOLEAN,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS notification_logs (
    id UUID PRIMARY KEY,
    incident_id UUID NOT NULL,
    channel VARCHAR(50) NOT NULL,
    recipient VARCHAR(255),
    message_summary TEXT,
    delivery_status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
