# API Contract

## AI Agent Service

Internal endpoints:

- `POST /agent/troubleshoot`
- `POST /agent/unresolved`

## Go API Gateway

Public endpoints:

- `GET /health`
- `POST /api/troubleshoot`
- `POST /api/troubleshoot/unresolved`
- `POST /api/incidents/escalate`
- `GET /api/incidents`
- `GET /api/incidents/{incident_id}`
- `GET /api/machines`
- `GET /api/telemetry/summary`
