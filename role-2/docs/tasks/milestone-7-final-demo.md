# Milestone 7 Task List - Final Demo Readiness

Source of truth: `../../../plan.md`, sections 12 and 13.

## Objective

Validate the final Role 2 contribution in the single approved demo scenario.

## Demo Scenario

```text
Machine: PACK-LINE-03
PLC Type: Siemens S7-1200
Error Code: OB82
Symptom: Machine cannot start after I/O module fault indicator appears.
Image Input: PLC panel or HMI screenshot showing fault condition.
```

No other final portfolio demo scenario should be used.

## Tasks

### 1. Local Startup

- [ ] Create `.env` from `.env.example`.
- [ ] Start services with Docker Compose.
- [ ] Confirm `api-gateway` starts.
- [ ] Confirm `postgres-db` starts.
- [ ] Confirm `redis-cache` starts.
- [ ] Confirm `n8n-workflows` starts.
- [ ] Confirm `monitoring-ui` starts.
- [ ] Confirm telemetry, Prometheus, and Grafana services start.

### 2. API Validation

- [ ] Call `GET /health`.
- [ ] Submit initial troubleshooting request for `PACK-LINE-03` and `OB82`.
- [ ] Confirm Go API calls Role 1.
- [ ] Confirm incident row is created.
- [ ] Confirm agent run row is created.
- [ ] Confirm Redis stores the troubleshooting response with 15-minute TTL.

### 3. Unresolved Flow Validation

- [ ] Mark the issue unresolved.
- [ ] Confirm Go API retrieves maintenance history.
- [ ] Confirm Go API sends history to Role 1 `/agent/unresolved`.
- [ ] Confirm second-level recommendation is persisted.
- [ ] Confirm high-priority or unresolved path triggers n8n WhatsApp escalation.
- [ ] Confirm notification result is written to `notification_logs`.

### 4. UI Validation

- [ ] Open `/dashboard`.
- [ ] Confirm dashboard metrics reflect API data.
- [ ] Open `/incidents`.
- [ ] Confirm the demo incident is listed.
- [ ] Open `/incidents/[id]`.
- [ ] Confirm AI recommendation and maintenance history details are shown.
- [ ] Open `/machines`.
- [ ] Confirm `PACK-LINE-03` is shown.
- [ ] Open `/telemetry`.
- [ ] Confirm telemetry summary is shown.
- [ ] Open `/agent-runs`.
- [ ] Confirm the demo run is shown.

### 5. Observability Validation

- [ ] Confirm Prometheus scrapes metrics.
- [ ] Confirm Grafana dashboard panels load.
- [ ] Confirm API request count is visible.
- [ ] Confirm API latency is visible.
- [ ] Confirm agent latency is visible.
- [ ] Confirm error rate is visible.
- [ ] Confirm n8n workflow success rate is visible.

### 6. Scope Validation

- [ ] Confirm no extra Role 2 public endpoints exist.
- [ ] Confirm no extra database tables exist.
- [ ] Confirm no extra Redis cache objects are used.
- [ ] Confirm no extra n8n workflows exist.
- [ ] Confirm no extra monitoring UI pages exist.
- [ ] Confirm no extra required environment variables exist.
- [ ] Confirm `role-2/legacy/nextjs` is removed, archived outside final scope, or clearly excluded from final delivery.

## Final Acceptance Target

```text
A reviewer can run the project locally, submit the PLC troubleshooting case, receive an AI recommendation, mark the issue unresolved, trigger WhatsApp escalation, and monitor the incident in the Next.js UI.
```
