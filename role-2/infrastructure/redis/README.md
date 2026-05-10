# Redis Cache

Redis is used only for:

- Recent troubleshooting response by `request_id`.
- Recent incident summary by `incident_id`.
- Machine metadata by `machine_id`.
- Maintenance history lookup by `machine_id` and `error_code`.

Default TTL: 15 minutes.
