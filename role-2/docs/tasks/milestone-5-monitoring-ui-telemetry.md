# Milestone 5 Task List - Monitoring UI and Telemetry

Source of truth: `../../../plan.md`, section 4.9 and Milestone 5.

## Objective

Replace placeholder monitoring UI and telemetry with functional Role 2 views backed by the Go API and Prometheus-compatible metrics.

## Scope Rules

- Keep only these UI pages: `/dashboard`, `/incidents`, `/incidents/[id]`, `/machines`, `/telemetry`, `/agent-runs`.
- Do not add extra dashboards beyond the main monitoring UI and Grafana telemetry dashboard.
- Do not add authentication or user management.

## UI Tasks

### 1. API Client

- [ ] Expand `apps/monitoring-ui/lib/api.ts`.
- [ ] Read `NEXT_PUBLIC_API_BASE_URL`.
- [ ] Add typed fetch helpers.
- [ ] Add error handling for failed API calls.
- [ ] Keep response types aligned with Go API contracts.

### 2. Dashboard Page

- [ ] Display open incidents.
- [ ] Display high-priority incidents.
- [ ] Display average agent confidence score.
- [ ] Display average troubleshooting latency.
- [ ] Display notification success rate.
- [ ] Replace static zero values.

### 3. Incidents Page

- [ ] Fetch `GET /api/incidents`.
- [ ] Display incident list.
- [ ] Display machine ID.
- [ ] Display error code.
- [ ] Display priority.
- [ ] Display status.
- [ ] Display escalation status.
- [ ] Display created time.

### 4. Incident Detail Page

- [ ] Fetch `GET /api/incidents/{incident_id}`.
- [ ] Display incident summary.
- [ ] Display AI recommendation.
- [ ] Display retrieved source summary.
- [ ] Display agent confidence score.
- [ ] Display notification status.
- [ ] Display maintenance history used.

### 5. Machines Page

- [ ] Fetch `GET /api/machines`.
- [ ] Display machine list.
- [ ] Display location.
- [ ] Display PLC type.
- [ ] Display recent incident count.

### 6. Telemetry Page

- [ ] Fetch `GET /api/telemetry/summary`.
- [ ] Display API request count.
- [ ] Display API latency.
- [ ] Display agent latency.
- [ ] Display error rate.
- [ ] Display n8n workflow success rate.

### 7. Agent Runs Page

- [ ] Display request ID.
- [ ] Display machine ID.
- [ ] Display error code.
- [ ] Display recommendation level.
- [ ] Display confidence score.
- [ ] Display safety status.
- [ ] Display tool-call status.
- [ ] Display latency.
- [ ] Use only API data available through the approved Role 2 surface.

## Telemetry Tasks

- [ ] Add request count instrumentation.
- [ ] Add API latency instrumentation.
- [ ] Add agent latency instrumentation.
- [ ] Add API error rate instrumentation.
- [ ] Add n8n workflow success rate instrumentation.
- [ ] Expose Prometheus-compatible metrics over HTTP.
- [ ] Fix `prometheus.yml` to scrape a real metrics endpoint.
- [ ] Add Grafana panels for required metrics.
- [ ] Keep OTLP endpoint usage aligned with `OTEL_EXPORTER_OTLP_ENDPOINT`.

## Acceptance Checks

- [ ] Monitoring UI builds.
- [ ] Monitoring UI typecheck passes.
- [ ] All six allowed pages load.
- [ ] UI data comes from Go API, not static placeholders.
- [ ] Prometheus can scrape Role 2 metrics.
- [ ] Grafana dashboard has useful panels.

## Files To Change

- `role-2/apps/monitoring-ui/lib/api.ts`
- `role-2/apps/monitoring-ui/types/index.ts`
- `role-2/apps/monitoring-ui/app/dashboard/page.tsx`
- `role-2/apps/monitoring-ui/app/incidents/page.tsx`
- `role-2/apps/monitoring-ui/app/incidents/[id]/page.tsx`
- `role-2/apps/monitoring-ui/app/machines/page.tsx`
- `role-2/apps/monitoring-ui/app/telemetry/page.tsx`
- `role-2/apps/monitoring-ui/app/agent-runs/page.tsx`
- `role-2/services/api-gateway/internal/telemetry/metrics.go`
- `role-2/services/telemetry-service/`
- `role-2/infrastructure/prometheus/prometheus.yml`
- `role-2/infrastructure/grafana/dashboards/plc-agent-dashboard.json`

## Verification Commands

```powershell
Set-Location role-2/apps/monitoring-ui
cmd /c npm install
cmd /c npm run typecheck
cmd /c npm run build
```

```powershell
Set-Location role-2/services/api-gateway
New-Item -ItemType Directory -Force -Path .\.gocache | Out-Null
$env:GOCACHE=(Resolve-Path .\.gocache).Path
go test ./...
```
