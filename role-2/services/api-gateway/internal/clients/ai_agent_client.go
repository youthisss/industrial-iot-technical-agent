package clients

import (
	"bytes"
	"context"
	"encoding/json"
	"fmt"
	"net/http"
	"strings"
	"time"
)

type TroubleShootingRequest struct {
	RequestID string `json:"request_id"`
	MachineID string `json:"machine_id"`
	PLCType   string `json:"plc_type"`
	ErrorCode string `json:"error_code"`
	Message   string `json:"message"`
	ImageURL  string `json:"image_url,omitempty"`
}

type RetrievedSource struct {
	SourceName string `json:"source_name"`
	Page       string `json:"page"`
	Snippet    string `json:"snippet"`
}

type AgentResponse struct {
	RequestID           string            `json:"request_id"`
	RecommendationLevel string            `json:"recommendation_level"`
	Summary             string            `json:"summary"`
	RecommendedAction   string            `json:"recommended_action"`
	SafetyWarning       string            `json:"safety_warning"`
	RetrievedSources    []RetrievedSource `json:"retrieved_sources"`
	ConfidenceScore     float64           `json:"confidence_score"`
}

type AIClient struct {
	baseURL    string
	httpClient *http.Client
}

func NewAIClient(baseURL string) *AIClient {
	return &AIClient{
		baseURL: strings.TrimRight(baseURL, "/"),
		httpClient: &http.Client{
			Timeout: 30 * time.Second,
		},
	}
}

func (c *AIClient) Troubleshoot(ctx context.Context, payload TroubleShootingRequest) (*AgentResponse, int, error) {
	start := time.Now()

	body, err := json.Marshal(payload)
	if err != nil {
		return nil, 0, fmt.Errorf("marshal troubleshoot request: %w", err)
	}

	req, err := http.NewRequestWithContext(
		ctx,
		http.MethodPost,
		c.baseURL+"/agent/troubleshoot",
		bytes.NewReader(body),
	)
	if err != nil {
		return nil, 0, fmt.Errorf("create ai request: %w", err)
	}

	req.Header.Set("content-type", "application/json")

	resp, err := c.httpClient.Do(req)
	if err != nil {
		return nil, int(time.Since(start).Milliseconds()), fmt.Errorf("call ai service: %w", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode < 200 || resp.StatusCode >= 300 {
		return nil, int(time.Since(start).Milliseconds()), fmt.Errorf("ai service returned status: %d", resp.StatusCode)
	}

	var result AgentResponse
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, int(time.Since(start).Milliseconds()), fmt.Errorf("decode ai: %w", err)
	}

	return &result, int(time.Since(start).Milliseconds()), nil

}
