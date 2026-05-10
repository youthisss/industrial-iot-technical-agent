# Milestone 4 Task List - n8n and WhatsApp Automation

Source of truth: `../../../plan.md`, section 4.8 and Milestone 4.

## Objective

Make Role 2 send incident notifications and WhatsApp escalations through the two approved n8n workflows, then persist delivery status in PostgreSQL.

## Scope Rules

- Keep only `incident_notification` and `whatsapp_escalation`.
- Do not add new notification channels.
- Do not add human approval workflow.
- Do not add extra workflow files beyond the approved two workflows and their payload examples.

## Tasks

### 1. incident_notification Workflow

- [ ] Keep workflow name `incident_notification`.
- [ ] Configure webhook trigger.
- [ ] Validate required incident payload fields.
- [ ] Format internal notification message.
- [ ] Send internal notification using a plan-appropriate local or configured n8n node.
- [ ] Return delivery status to Go API.
- [ ] Add executable connections between all workflow nodes.

Required workflow steps:

```text
1. Receive incident payload.
2. Validate required fields.
3. Format notification message.
4. Send internal notification.
5. Return delivery status to Go API.
```

### 2. whatsapp_escalation Workflow

- [ ] Keep workflow name `whatsapp_escalation`.
- [ ] Configure webhook trigger.
- [ ] Validate `machine_id`, `error_code`, `priority`, and `recommendation`.
- [ ] Format WhatsApp escalation message.
- [ ] Send WhatsApp notification to supervisor.
- [ ] Return delivery status to Go API.
- [ ] Add executable connections between all workflow nodes.

Required workflow steps:

```text
1. Receive escalation payload.
2. Validate machine_id, error_code, priority, and recommendation.
3. Format WhatsApp message.
4. Send WhatsApp notification to supervisor.
5. Return delivery status to Go API.
```

### 3. Payload Examples

- [ ] Keep `payload_examples/incident_notification_payload.json` aligned with Go API payload.
- [ ] Keep `payload_examples/whatsapp_escalation_payload.json` aligned with Go API payload.
- [ ] Use final demo machine `PACK-LINE-03`.
- [ ] Use final demo error code `OB82`.

### 4. Go API Integration

- [ ] Implement n8n HTTP webhook client.
- [ ] Read webhook URLs from `N8N_INCIDENT_WEBHOOK_URL` and `N8N_WHATSAPP_WEBHOOK_URL`.
- [ ] Trigger incident notification after incident creation where required.
- [ ] Trigger WhatsApp escalation only for high-priority or unresolved incidents.
- [ ] Persist each delivery result into `notification_logs`.
- [ ] Return useful API errors when webhook delivery fails.

### 5. Acceptance Checks

- [ ] n8n workflows import successfully.
- [ ] Workflow nodes are connected.
- [ ] Incident notification webhook returns delivery status.
- [ ] WhatsApp escalation webhook returns delivery status.
- [ ] Go API logs notification delivery status.
- [ ] No workflow outside the two approved workflows exists.

## Files To Change

- `role-2/automation/n8n/workflows/incident_notification.json`
- `role-2/automation/n8n/workflows/whatsapp_escalation.json`
- `role-2/automation/n8n/payload_examples/incident_notification_payload.json`
- `role-2/automation/n8n/payload_examples/whatsapp_escalation_payload.json`
- `role-2/services/api-gateway/internal/clients/n8n_client.go`
- `role-2/services/api-gateway/internal/handlers/routes.go`
- `role-2/services/api-gateway/internal/database/repository.go`

## Verification Commands

```powershell
Set-Location role-2/services/api-gateway
New-Item -ItemType Directory -Force -Path .\.gocache | Out-Null
$env:GOCACHE=(Resolve-Path .\.gocache).Path
go test ./...
```
