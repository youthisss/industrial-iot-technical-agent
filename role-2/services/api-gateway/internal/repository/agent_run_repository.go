package repository

import (
	"context"
	"fmt"

	"github.com/google/uuid"
	"github.com/jackc/pgx/v5/pgxpool"
)

type CreateAgentRunParams struct {
	RequestID           string
	IncidentID          string
	MachineID           string
	ErrorCode           string
	RecommendationLevel string
	ConfidenceScore     float64
	LatencyMS           int
	ToolCallSuccess     bool
	SafetyPassed        bool
}

type AgentRunRepository struct {
	db *pgxpool.Pool
}

func NewAgentRunRepository(db *pgxpool.Pool) *AgentRunRepository {
	return &AgentRunRepository{db: db}
}

func (r *AgentRunRepository) Create(ctx context.Context, params CreateAgentRunParams) error {
	_, err := r.db.Exec(ctx, `
		INSERT INTO agent_runs (
			id,
			request_id,
			incident_id,
			machine_id,
			error_code,
			recommendation_level,
			confidence_score,
			latency_ms,
			tool_call_success,
			safety_passed
		)
		VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
	`, uuid.New().String(),
		params.RequestID,
		params.IncidentID,
		params.MachineID,
		params.ErrorCode,
		params.RecommendationLevel,
		params.ConfidenceScore,
		params.LatencyMS,
		params.ToolCallSuccess,
		params.SafetyPassed,
	)

	if err != nil {
		return fmt.Errorf("insert agent run: %w", err)
	}

	return nil
}
