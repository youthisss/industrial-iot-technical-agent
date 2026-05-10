package cache

const DefaultTTLMinutes = 15

var AllowedKeys = []string{
	"troubleshooting_response_by_request_id",
	"incident_summary_by_incident_id",
	"machine_metadata_by_machine_id",
	"maintenance_history_by_machine_id_error_code",
}
