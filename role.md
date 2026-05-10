# Role 2 Execution Guide

This file is your execution guide as **Role 2** for this project.
Source of truth: `plan.md` (version date `2026-05-08`).

## 1. Role 2 Mission

Build and own the platform and operations layer:

- Go API gateway
- Telemetry service
- PostgreSQL maintenance history and incident persistence
- Redis cache
- n8n notification and WhatsApp escalation workflows
- Main Next.js monitoring UI
- Service-to-service integration and observability

## 2. Ownership Boundaries

### You own

1. `role-2/services/api-gateway`
2. `role-2/services/telemetry-service`
3. `role-2/apps/monitoring-ui`
4. `role-2/automation/n8n`
5. PostgreSQL schema and queries
6. Redis caching behavior
7. Incident logging and notification logging
8. Integration with Role 1 API

### You do not own

1. Agent reasoning logic
2. Prompt design
3. RAG implementation internals
4. Vector embedding pipeline
5. Model evaluation scoring logic

## 3. Fixed Scope Constraints

Do not add beyond plan scope:

- No extra public API endpoints outside the defined list
- No extra database tables beyond the required 5 tables
- No extra n8n workflows beyond 2 workflows
- No extra monitoring UI pages beyond 6 pages
- No new top-level project directories
- No authentication, billing, mobile app, or extra notification channels

## 4. Services and Paths You Must Deliver

- `role-2/services/api-gateway`
- `role-2/services/telemetry-service`
- `role-2/apps/monitoring-ui`
- `role-2/automation/n8n/workflows/incident_notification.json`
- `role-2/automation/n8n/workflows/whatsapp_escalation.json`
- `role-2/automation/n8n/payload_examples/incident_notification_payload.json`
- `role-2/automation/n8n/payload_examples/whatsapp_escalation_payload.json`

## 5. Required Public API Endpoints

Expose only:

1. `GET /health`
2. `POST /api/troubleshoot`
3. `POST /api/troubleshoot/unresolved`
4. `POST /api/incidents/escalate`
5. `GET /api/incidents`
6. `GET /api/incidents/{incident_id}`
7. `GET /api/machines`
8. `GET /api/telemetry/summary`

## 6. Required Database Tables

Create and use only:

1. `machines`
2. `maintenance_history`
3. `incident_logs`
4. `agent_runs`
5. `notification_logs`

## 7. Required Redis Cache Objects

Cache only these (TTL 15 minutes):

1. Troubleshooting response by `request_id`
2. Incident summary by `incident_id`
3. Machine metadata by `machine_id`
4. Maintenance history by `machine_id + error_code`

## 8. Required n8n Workflows

1. `incident_notification`
   - Triggered by Go API webhook
   - Validate payload
   - Format message
   - Send internal notification
   - Return delivery status

2. `whatsapp_escalation`
   - Triggered by Go API for high-priority or unresolved issue
   - Validate `machine_id`, `error_code`, `priority`, `recommendation`
   - Format WhatsApp message
   - Send supervisor notification
   - Return delivery status

## 9. Required Monitoring UI Pages

1. `/dashboard`
2. `/incidents`
3. `/incidents/[id]`
4. `/machines`
5. `/telemetry`
6. `/agent-runs`

## 10. Role 2 Implementation Order

### Milestone 3 - API, History, Cache

- [ ] Implement Go handlers for all required endpoints
- [ ] Implement Role 1 AI client integration (`/agent/troubleshoot`, `/agent/unresolved`)
- [ ] Persist incidents and agent run records in PostgreSQL
- [ ] Implement Redis caching with 15-minute TTL
- [ ] Return UI-ready response contracts

Acceptance target:

`Go API receives troubleshooting request, calls AI service, stores results, caches response, and returns data to UI.`

### Milestone 4 - n8n and WhatsApp

- [ ] Build `incident_notification` workflow JSON
- [ ] Build `whatsapp_escalation` workflow JSON
- [ ] Add payload example JSON files
- [ ] Add n8n webhook client in Go API
- [ ] Persist delivery status into `notification_logs`

Acceptance target:

`High-priority or unresolved incidents trigger n8n and send WhatsApp escalation.`

### Milestone 5 - Monitoring UI and Telemetry

- [ ] Build all 6 required pages in `role-2/apps/monitoring-ui`
- [ ] Integrate UI with Go API endpoints
- [ ] Add telemetry instrumentation in Go services
- [ ] Expose Prometheus-compatible metrics
- [ ] Ensure Grafana dashboards can visualize key metrics

Acceptance target:

`UI displays incidents, machines, telemetry summaries, and agent runs from Go API.`

### Milestone 7 - Final Demo Readiness (Shared)

- [ ] Validate end-to-end demo flow using `PACK-LINE-03` / `OB82`
- [ ] Confirm unresolved path triggers WhatsApp escalation
- [ ] Confirm incident and agent run visibility in UI
- [ ] Ensure README supports local setup and demo flow

## 11. Test Tasks (Role 2 Mandatory)

- [ ] Go API handler tests
- [ ] PostgreSQL query tests
- [ ] Redis cache behavior tests
- [ ] Python AI service client tests
- [ ] n8n webhook client tests
- [ ] Incident logging tests
- [ ] Telemetry instrumentation tests
- [ ] Next.js API integration mock tests

## 12. Environment Variables You Must Use

Use these values from `.env` (from `.env.example`):

- `API_PORT`
- `AI_AGENT_SERVICE_URL`
- `DATABASE_URL`
- `REDIS_URL`
- `N8N_INCIDENT_WEBHOOK_URL`
- `N8N_WHATSAPP_WEBHOOK_URL`
- `NEXT_PUBLIC_API_BASE_URL`
- `OTEL_EXPORTER_OTLP_ENDPOINT`
- `PROMETHEUS_PORT`
- `GRAFANA_PORT`

No extra required env vars should be introduced.

## 13. Role 2 Done Checklist

Mark Role 2 complete only if all are true:

- [ ] Docker Compose starts all Role 2 services
- [ ] Go API health endpoint works
- [ ] PostgreSQL schema is created and queried successfully
- [ ] Redis is connected and caching with 15-minute TTL
- [ ] Troubleshoot and unresolved flows work through Go API to Role 1
- [ ] n8n escalation flow works and notification logs are persisted
- [ ] Monitoring UI loads and shows incidents/machines/agent-runs/telemetry
- [ ] Telemetry metrics are visible in Prometheus/Grafana
- [ ] No out-of-scope additions were implemented

## 14. Working Rule

When in doubt, choose strict compliance with `plan.md` over adding new ideas.
