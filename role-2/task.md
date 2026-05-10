# Role 2 Task Tracker

Source of truth: `../plan.md` and `../role.md`.

Scope: Role 2 only. Do not add public endpoints, database tables, workflows, UI pages, services, or required environment variables outside the final plan.

## Current Audit Status

Role 2 currently has the required folder skeleton, routes, schema files, UI page files, n8n workflow files, and observability placeholders. It is not yet functionally complete because the API, database, Redis, n8n, telemetry, and monitoring UI layers are mostly placeholder implementations.

## Execution Order

Follow this order strictly:

1. Milestone 3 - API, History, and Cache.
2. Milestone 4 - n8n and WhatsApp Automation.
3. Milestone 5 - Monitoring UI and Telemetry.
4. Role 2 mandatory tests.
5. Milestone 7 - Final demo readiness.

## Milestone 3 - API, History, and Cache

Detailed checklist: `docs/tasks/milestone-3-api-history-cache.md`

- [ ] Implement API gateway configuration from approved environment variables only.
- [ ] Implement request and response contracts for all Role 2 public API endpoints.
- [ ] Implement Role 1 AI service client for `/agent/troubleshoot`.
- [ ] Implement Role 1 AI service client for `/agent/unresolved`.
- [ ] Implement PostgreSQL repository connection and query methods.
- [ ] Implement incident logging into `incident_logs`.
- [ ] Implement agent run logging into `agent_runs`.
- [ ] Implement maintenance history lookup from `maintenance_history`.
- [ ] Implement machine listing and lookup from `machines`.
- [ ] Implement Redis cache with 15-minute TTL.
- [ ] Cache only the four approved cache object types.
- [ ] Return UI-ready JSON responses from all handlers.
- [ ] Replace placeholder handlers in `internal/handlers/routes.go`.

Acceptance target:

```text
The Go API receives troubleshooting requests, calls the AI service, stores results, caches responses, and returns data to the UI.
```

## Milestone 4 - n8n and WhatsApp Automation

Detailed checklist: `docs/tasks/milestone-4-n8n-whatsapp.md`

- [ ] Implement executable `incident_notification` workflow connections.
- [ ] Implement executable `whatsapp_escalation` workflow connections.
- [ ] Keep only the two approved workflows.
- [ ] Validate incident notification payload fields.
- [ ] Validate WhatsApp escalation payload fields.
- [ ] Implement Go n8n webhook client.
- [ ] Trigger incident notification after incident creation where required.
- [ ] Trigger WhatsApp escalation only for high-priority or unresolved incidents.
- [ ] Persist notification delivery status into `notification_logs`.
- [ ] Keep payload examples aligned with handler contracts.

Acceptance target:

```text
High-priority or unresolved incidents trigger n8n and produce a WhatsApp escalation notification.
```

## Milestone 5 - Monitoring UI and Telemetry

Detailed checklist: `docs/tasks/milestone-5-monitoring-ui-telemetry.md`

- [ ] Integrate `/dashboard` with API summary data.
- [ ] Integrate `/incidents` with `GET /api/incidents`.
- [ ] Integrate `/incidents/[id]` with `GET /api/incidents/{incident_id}`.
- [ ] Integrate `/machines` with `GET /api/machines`.
- [ ] Integrate `/telemetry` with `GET /api/telemetry/summary`.
- [ ] Integrate `/agent-runs` with API data exposed through the approved plan surface.
- [ ] Add telemetry instrumentation in Go API.
- [ ] Expose Prometheus-compatible metrics.
- [ ] Fix Prometheus scrape target to use a real HTTP metrics endpoint.
- [ ] Add Grafana dashboard panels for required telemetry metrics.

Acceptance target:

```text
The UI displays incidents, machines, agent runs, and telemetry summaries from the Go API.
```

## Mandatory Role 2 Tests

Detailed checklist: `docs/tasks/testing.md`

- [ ] Go API handler tests.
- [ ] PostgreSQL query tests.
- [ ] Redis cache behavior tests.
- [ ] Python AI service client tests.
- [ ] n8n webhook client tests.
- [ ] Incident logging tests.
- [ ] Telemetry instrumentation tests.
- [ ] Next.js API integration mock tests.

## Milestone 7 - Final Demo Readiness

Detailed checklist: `docs/tasks/milestone-7-final-demo.md`

- [ ] Validate Docker Compose startup for Role 2 services.
- [ ] Validate `GET /health`.
- [ ] Validate PostgreSQL schema and seed data.
- [ ] Validate Redis connectivity and TTL behavior.
- [ ] Validate initial troubleshooting flow for `PACK-LINE-03` and `OB82`.
- [ ] Validate unresolved issue flow.
- [ ] Validate WhatsApp escalation path.
- [ ] Validate incident visibility in monitoring UI.
- [ ] Validate agent run visibility in monitoring UI.
- [ ] Validate telemetry visibility in Prometheus and Grafana.
- [ ] Confirm no out-of-scope Role 2 additions exist.

## Known Blockers From Audit

- [ ] API handlers currently return placeholder responses.
- [ ] AI client has no HTTP methods.
- [ ] n8n client has no HTTP methods.
- [ ] Database repository has no connection or queries.
- [ ] Redis cache has no client implementation.
- [ ] Telemetry service is placeholder-only.
- [ ] Prometheus is scraping a placeholder target.
- [ ] Grafana dashboard has no panels.
- [ ] Monitoring UI pages render static placeholders.
- [ ] API tests are no-op boilerplate.
- [ ] `role-2/legacy/nextjs` is outside the current Role 2 deliverable path and must be removed, archived outside final scope, or explicitly excluded from final delivery.

## Validation Commands

Use a service-local Go cache on this Windows machine if the default Go cache fails:

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
