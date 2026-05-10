# Role 2 Mandatory Test Task List

Source of truth: `../../../plan.md`, section 10.

## Objective

Replace placeholder tests with meaningful coverage for the Role 2 API, database, cache, clients, telemetry, and UI integration behavior.

## Test Tasks

### 1. Go API Handler Tests

- [ ] Test `GET /health`.
- [ ] Test `POST /api/troubleshoot` success path.
- [ ] Test `POST /api/troubleshoot` validation failure.
- [ ] Test `POST /api/troubleshoot/unresolved` success path.
- [ ] Test `POST /api/incidents/escalate` success path.
- [ ] Test `GET /api/incidents`.
- [ ] Test `GET /api/incidents/{incident_id}`.
- [ ] Test `GET /api/machines`.
- [ ] Test `GET /api/telemetry/summary`.

### 2. PostgreSQL Query Tests

- [ ] Test machine insert or seed lookup.
- [ ] Test maintenance history lookup by `machine_id` and `error_code`.
- [ ] Test incident creation.
- [ ] Test incident status update.
- [ ] Test agent run creation.
- [ ] Test notification log creation.
- [ ] Test incident list query.
- [ ] Test incident detail query.

### 3. Redis Cache Behavior Tests

- [ ] Test troubleshooting response cache by `request_id`.
- [ ] Test incident summary cache by `incident_id`.
- [ ] Test machine metadata cache by `machine_id`.
- [ ] Test maintenance history cache by `machine_id` and `error_code`.
- [ ] Test 15-minute TTL is applied.
- [ ] Test cache miss behavior.

### 4. Python AI Service Client Tests

- [ ] Test `/agent/troubleshoot` request mapping.
- [ ] Test `/agent/troubleshoot` response parsing.
- [ ] Test `/agent/unresolved` request mapping.
- [ ] Test `/agent/unresolved` response parsing.
- [ ] Test non-2xx status handling.
- [ ] Test invalid JSON handling.
- [ ] Test timeout handling.

### 5. n8n Webhook Client Tests

- [ ] Test incident notification payload mapping.
- [ ] Test WhatsApp escalation payload mapping.
- [ ] Test webhook success response parsing.
- [ ] Test webhook failure handling.
- [ ] Test missing webhook URL handling.

### 6. Incident Logging Tests

- [ ] Test initial troubleshooting creates incident log.
- [ ] Test unresolved flow updates incident status.
- [ ] Test escalation flow updates escalation status.
- [ ] Test notification result is persisted.

### 7. Telemetry Instrumentation Tests

- [ ] Test request count increments.
- [ ] Test API latency records.
- [ ] Test agent latency records.
- [ ] Test error rate records.
- [ ] Test n8n success rate records.
- [ ] Test metrics endpoint returns Prometheus-compatible data.

### 8. Next.js API Integration Mock Tests

- [ ] Test dashboard data fetch.
- [ ] Test incident list data fetch.
- [ ] Test incident detail data fetch.
- [ ] Test machines data fetch.
- [ ] Test telemetry data fetch.
- [ ] Test agent runs data fetch.
- [ ] Test failed API response handling.

## Verification Commands

```powershell
Set-Location role-2/services/api-gateway
New-Item -ItemType Directory -Force -Path .\.gocache | Out-Null
$env:GOCACHE=(Resolve-Path .\.gocache).Path
go test ./...
```

```powershell
Set-Location role-2/services/telemetry-service
New-Item -ItemType Directory -Force -Path .\.gocache | Out-Null
$env:GOCACHE=(Resolve-Path .\.gocache).Path
go test ./...
```

```powershell
Set-Location role-2/apps/monitoring-ui
cmd /c npm install
cmd /c npm run typecheck
```
