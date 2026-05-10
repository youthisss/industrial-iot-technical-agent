# Milestone 3 Task List - API, History, and Cache

Source of truth: `../../../plan.md`, section 4 and Milestone 3.

## Objective

Make the Go API Gateway functionally receive troubleshooting requests, call Role 1, persist records in PostgreSQL, cache approved data in Redis, and return UI-ready responses.

## Scope Rules

- Use only the public endpoints approved in `plan.md`.
- Use only the five approved database tables.
- Use only the four approved Redis cache objects.
- Do not add authentication, extra APIs, extra tables, or extra service responsibilities.

## Tasks

### 1. Configuration

- [ ] Add API gateway config loader.
- [ ] Read only `API_PORT`, `AI_AGENT_SERVICE_URL`, `DATABASE_URL`, `REDIS_URL`, `N8N_INCIDENT_WEBHOOK_URL`, `N8N_WHATSAPP_WEBHOOK_URL`, and telemetry variables where needed.
- [ ] Apply HTTP client timeout defaults.
- [ ] Return startup errors when required local dependencies are unavailable.

### 2. Request and Response Contracts

- [ ] Define request DTO for `POST /api/troubleshoot`.
- [ ] Define request DTO for `POST /api/troubleshoot/unresolved`.
- [ ] Define request DTO for `POST /api/incidents/escalate`.
- [ ] Define response DTO for incident list.
- [ ] Define response DTO for incident detail.
- [ ] Define response DTO for machine list.
- [ ] Define response DTO for telemetry summary.
- [ ] Validate required fields and return JSON errors.

### 3. Role 1 AI Client

- [ ] Implement `POST /agent/troubleshoot` call.
- [ ] Implement `POST /agent/unresolved` call.
- [ ] Map Role 2 request payloads to Role 1 contract.
- [ ] Map Role 1 response payloads to Role 2 persistence model.
- [ ] Add status-code handling.
- [ ] Add invalid JSON handling.
- [ ] Add timeout handling.

### 4. PostgreSQL Repository

- [ ] Open database connection from `DATABASE_URL`.
- [ ] Add health or ping behavior.
- [ ] Insert incident into `incident_logs`.
- [ ] Update incident status and escalation status.
- [ ] Fetch incident list.
- [ ] Fetch incident detail by ID.
- [ ] Fetch machines.
- [ ] Fetch machine by `machine_id`.
- [ ] Fetch maintenance history by `machine_id` and `error_code`.
- [ ] Insert agent run into `agent_runs`.
- [ ] Insert notification log into `notification_logs`.

### 5. Redis Cache

- [ ] Open Redis client from `REDIS_URL`.
- [ ] Implement troubleshooting response cache by `request_id`.
- [ ] Implement incident summary cache by `incident_id`.
- [ ] Implement machine metadata cache by `machine_id`.
- [ ] Implement maintenance history cache by `machine_id` and `error_code`.
- [ ] Enforce default TTL of 15 minutes.
- [ ] Do not store long-term state in Redis.

### 6. Handlers

- [ ] Replace placeholder `writeAccepted`.
- [ ] Implement `GET /health`.
- [ ] Implement `POST /api/troubleshoot`.
- [ ] Implement `POST /api/troubleshoot/unresolved`.
- [ ] Implement `POST /api/incidents/escalate`.
- [ ] Implement `GET /api/incidents`.
- [ ] Implement `GET /api/incidents/{incident_id}`.
- [ ] Implement `GET /api/machines`.
- [ ] Implement `GET /api/telemetry/summary`.

### 7. Acceptance Checks

- [ ] API compiles.
- [ ] API handler tests pass.
- [ ] Database migration matches `plan.md`.
- [ ] Demo seed data supports `PACK-LINE-03` and `OB82`.
- [ ] Troubleshooting flow creates incident and agent run records.
- [ ] Cache hit returns the expected cached response.
- [ ] Cache miss calls Role 1 and writes cache.

## Files To Change

- `role-2/services/api-gateway/cmd/api/main.go`
- `role-2/services/api-gateway/internal/handlers/routes.go`
- `role-2/services/api-gateway/internal/services/troubleshooting.go`
- `role-2/services/api-gateway/internal/clients/ai_agent_client.go`
- `role-2/services/api-gateway/internal/database/repository.go`
- `role-2/services/api-gateway/internal/cache/redis.go`
- `role-2/services/api-gateway/internal/telemetry/metrics.go`
- `role-2/services/api-gateway/tests/`

## Verification Commands

```powershell
Set-Location role-2/services/api-gateway
New-Item -ItemType Directory -Force -Path .\.gocache | Out-Null
$env:GOCACHE=(Resolve-Path .\.gocache).Path
go test ./...
```
