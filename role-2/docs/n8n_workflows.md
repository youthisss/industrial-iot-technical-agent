# n8n Workflows

The final scope allows only two workflows under `role-2/automation/n8n/workflows`.

## incident_notification

Steps:

1. Receive incident payload.
2. Validate required fields.
3. Format notification message.
4. Send internal notification.
5. Return delivery status to Go API.

## whatsapp_escalation

Steps:

1. Receive escalation payload.
2. Validate `machine_id`, `error_code`, `priority`, and `recommendation`.
3. Format WhatsApp message.
4. Send WhatsApp notification to supervisor.
5. Return delivery status to Go API.
