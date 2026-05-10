package handlers

import (
	"encoding/json"
	"net/http"
	"strings"

	"plc-troubleshooting-agent/services/api-gateway/internal/clients"
	"plc-troubleshooting-agent/services/api-gateway/internal/repository"
)

type Dependencies struct {
	MachineRepo  *repository.MachineRepository
	IncidentRepo *repository.IncidentRepository
	AgentRunRepo *repository.AgentRunRepository
	AIClient     *clients.AIClient
}

func Router(deps Dependencies) http.Handler {
	mux := http.NewServeMux()

	mux.HandleFunc("GET /health", writeHealth)
	mux.HandleFunc("POST /api/troubleshoot", writeAccepted)
	mux.HandleFunc("POST /api/troubleshoot/unresolved", writeAccepted)
	mux.HandleFunc("POST /api/incidents/escalate", writeAccepted)
	mux.HandleFunc("GET /api/incidents", writeList)
	mux.HandleFunc("GET /api/incidents/", writeIncident)
	mux.HandleFunc("GET /api/machines", writeList)
	mux.HandleFunc("GET /api/telemetry/summary", writeTelemetry)
	mux.HandleFunc("GET /api/machines", listMachines(deps))
	mux.HandleFunc("GET /api/incidents", listIncident(deps))
	mux.HandleFunc("POST /api/troubleshoot", troubleshoot(deps))

	return mux
}

func writeHealth(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, map[string]string{
		"status":  "ok",
		"service": "api-gateway",
	})
}

func writeAccepted(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusAccepted, map[string]string{
		"status": "accepted",
	})
}

func writeList(w http.ResponseWriter, r *http.Request) {
	writeJSON(w, http.StatusOK, []map[string]string{})
}

func writeIncident(w http.ResponseWriter, r *http.Request) {
	id := strings.TrimPrefix(r.URL.Path, "/api/incidents/")
	id = strings.TrimSpace(id)

	if id == "" {
		writeError(w, http.StatusBadRequest, "incident_id is required")
		return
	}

	writeJSON(w, http.StatusOK, map[string]string{
		"incident_id": id,
		"status":      "placeholder",
	})
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

	if err := json.NewEncoder(w).Encode(payload); err != nil {
		http.Error(w, `{"error":"failed to encode response"}`, http.StatusInternalServerError)
	}
}

func writeError(w http.ResponseWriter, status int, message string) {
	writeJSON(w, status, map[string]string{
		"error": message,
	})
}

func listMachines(deps Dependencies) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		machines, err := deps.MachineRepo.List(r.Context())
		if err != nil {
			writeError(w, http.StatusInternalServerError, "failed to list machines")
			return
		}

		writeJSON(w, http.StatusOK, machines)
	}
}

func listIncident(deps Dependencies) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		incidents, err := deps.IncidentRepo.List(r.Context())
		if err != nil {
			writeError(w, http.StatusInternalServerError, "failed to list incidents")
			return
		}

		writeJSON(w, http.StatusOK, incidents)
	}
}

func getIncident(deps Dependencies) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		id := strings.TrimPrefix(r.URL.Path, "/api/incidents/")
		id = strings.TrimSpace(id)

		if id == "" {
			writeError(w, http.StatusBadRequest, "incident_id is required")
			return
		}

		incident, err := deps.IncidentRepo.GetByID(r.Context(), id)
		if err != nil {
			writeError(w, http.StatusNotFound, "incident not found")
			return
		}

		writeJSON(w, http.StatusOK, incident)
	}
}

func troubleshoot(deps Dependencies) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		var req clients.TroubleShootingRequest

		if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
			writeError(w, http.StatusBadRequest, "invalid request body")
			return
		}

		if req.RequestID == "" || req.MachineID == "" || req.PLCType == "" || req.ErrorCode == "" || req.Message == "" {
			writeError(w, http.StatusBadRequest, "request_id, machine_id, plc_type, error_code, and message are required")
			return
		}

		agentResp, latencyMS, err := deps.AIClient.Troubleshoot(r.Context(), req)
		if err != nil {
			writeError(w, http.StatusBadGateway, "failed to call ai agent service")
			return
		}

		incident, err := deps.IncidentRepo.Create(r.Context(), repository.CreateIncidentParams{
			MachineID:        req.MachineID,
			PLCType:          req.PLCType,
			ErrorCode:        req.ErrorCode,
			IssueSummary:     agentResp.Summary,
			AIRecommendation: agentResp.RecommendedAction,
			Priority:         "medium",
			Status:           "open",
			EscalationStatus: "not_escalated",
		})
		if err != nil {
			writeError(w, http.StatusInternalServerError, "failed to create incident")
			return
		}

		if err := deps.AgentRunRepo.Create(r.Context(), repository.CreateAgentRunParams{
			RequestID:           req.RequestID,
			IncidentID:          incident.ID,
			MachineID:           req.MachineID,
			ErrorCode:           req.ErrorCode,
			RecommendationLevel: agentResp.RecommendationLevel,
			ConfidenceScore:     agentResp.ConfidenceScore,
			LatencyMS:           latencyMS,
			ToolCallSuccess:     true,
			SafetyPassed:        agentResp.SafetyWarning != "",
		}); err != nil {
			writeError(w, http.StatusInternalServerError, "failed to create agent run")
			return
		}

		writeJSON(w, http.StatusOK, map[string]any{
			"request_id":           req.RequestID,
			"incident_id":          incident.ID,
			"machine_id":           req.MachineID,
			"plc_type":             req.PLCType,
			"error_code":           req.ErrorCode,
			"priority":             incident.Priority,
			"status":               incident.Status,
			"escalation_status":    incident.EscalationStatus,
			"recommendation_level": agentResp.RecommendationLevel,
			"summary":              agentResp.Summary,
			"recommended_action":   agentResp.RecommendedAction,
			"safety_warning":       agentResp.SafetyWarning,
			"retrieved_sources":    agentResp.RetrievedSources,
			"confidence_score":     agentResp.ConfidenceScore,
			"agent_latency_ms":     latencyMS,
			"cached":               false,
		})
	}
}
