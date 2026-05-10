package telemetry

type Summary struct {
	APIRequestCount        int     `json:"api_request_count"`
	APILatency             float64 `json:"api_latency"`
	AgentLatency           float64 `json:"agent_latency"`
	ErrorRate              float64 `json:"error_rate"`
	N8NWorkflowSuccessRate float64 `json:"n8n_workflow_success_rate"`
}
