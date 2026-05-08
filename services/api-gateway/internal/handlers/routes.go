package handlers

import (
	"encoding/json"
	"net/http"
	"strings"
)

func Router() http.Handler {
	mux := http.NewServeMux()
	mux.HandleFunc("GET /health", writeHealth)
	mux.HandleFunc("POST /api/troubleshoot", writeAccepted)
	mux.HandleFunc("POST /api/troubleshoot/unresolved", writeAccepted)
	mux.HandleFunc("POST /api/incidents/escalate", writeAccepted)
	mux.HandleFunc("GET /api/incidents", writeList)
	mux.HandleFunc("GET /api/incidents/", writeIncident)
	mux.HandleFunc("GET /api/machines", writeList)
	mux.HandleFunc("GET /api/telemetry/summary", writeTelemetry)
	return mux
}

func writeHealth(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, map[string]string{"status": "ok", "service": "api-gateway"})
}

func writeAccepted(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusAccepted, map[string]string{"status": "accepted"})
}

func writeList(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, []map[string]string{})
}

func writeIncident(w http.ResponseWriter, r *http.Request) {
	id := strings.TrimPrefix(r.URL.Path, "/api/incidents/")
	writeJSON(w, http.StatusOK, map[string]string{"incident_id": id, "status": "placeholder"})
}

func writeTelemetry(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, map[string]float64{
		"api_request_count":         0,
		"api_latency":               0,
		"agent_latency":             0,
		"error_rate":                0,
		"n8n_workflow_success_rate": 0,
	})
}

func writeJSON(w http.ResponseWriter, status int, payload any) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	_ = json.NewEncoder(w).Encode(payload)
}
