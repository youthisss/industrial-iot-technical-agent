package repository

import (
	"context"
	"fmt"
	"time"

	"github.com/google/uuid"
	"github.com/jackc/pgx/v5/pgxpool"
)

type Incident struct {
	ID               string    `json:"id"`
	MachineID        string    `json:"machine_id"`
	PLCType          string    `json:"plc_type"`
	ErrorCode        string    `json:"error_code"`
	IssueSummary     string    `json:"issue_summary"`
	AIRecommendation string    `json:"ai_recommendation"`
	Priority         string    `json:"priority"`
	Status           string    `json:"status"`
	EscalationStatus string    `json:"escalation_status"`
	CreatedAt        time.Time `json:"created_at"`
	UpdatedAt        time.Time `json:"updated_at"`
}

type CreateIncidentParams struct {
	MachineID        string
	PLCType          string
	ErrorCode        string
	IssueSummary     string
	AIRecommendation string
	Priority         string
	Status           string
	EscalationStatus string
}

type IncidentRepository struct {
	db *pgxpool.Pool
}

func NewIncidentRepository(db *pgxpool.Pool) *IncidentRepository {
	return &IncidentRepository{db: db}
}

func (r *IncidentRepository) List(ctx context.Context) ([]Incident, error) {
	rows, err := r.db.Query(ctx, `
		SELECT
			id,
			machine_id,
			COALESCE(plc_type, ''),
			COALESCE(error_code, ''),
			COALESCE(issue_summary, ''),
			COALESCE(ai_recommendation, ''),
			priority,
			status,
			escalation_status,
			created_at,
			updated_at
		FROM incident_logs
		ORDER BY created_at DESC
	`)
	if err != nil {
		return nil, fmt.Errorf("query incidents: %w", err)
	}
	defer rows.Close()

	incidents := make([]Incident, 0)

	for rows.Next() {
		var incident Incident

		if err := rows.Scan(
			&incident.ID,
			&incident.MachineID,
			&incident.PLCType,
			&incident.ErrorCode,
			&incident.IssueSummary,
			&incident.AIRecommendation,
			&incident.Priority,
			&incident.Status,
			&incident.EscalationStatus,
			&incident.CreatedAt,
			&incident.UpdatedAt,
		); err != nil {
			return nil, fmt.Errorf("scan incident: %w", err)
		}

		incidents = append(incidents, incident)
	}

	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("iterate incidents: %w", err)
	}

	return incidents, nil
}

func (r *IncidentRepository) GetByID(ctx context.Context, id string) (*Incident, error) {
	var incident Incident

	err := r.db.QueryRow(ctx, `
		SELECT
			id,
			machine_id,
			COALESCE(plc_type, ''),
			COALESCE(error_code, ''),
			COALESCE(issue_summary, ''),
			COALESCE(ai_recommendation, ''),
			priority,
			status,
			escalation_status,
			created_at,
			updated_at
		FROM incident_logs
		WHERE id = $1
	`, id).Scan(
		&incident.ID,
		&incident.MachineID,
		&incident.PLCType,
		&incident.ErrorCode,
		&incident.IssueSummary,
		&incident.AIRecommendation,
		&incident.Priority,
		&incident.Status,
		&incident.EscalationStatus,
		&incident.CreatedAt,
		&incident.UpdatedAt,
	)
	if err != nil {
		return nil, fmt.Errorf("get incident by id: %w", err)
	}

	return &incident, nil
}

func (r *IncidentRepository) Create(ctx context.Context, params CreateIncidentParams) (*Incident, error) {
	id := uuid.New().String()

	_, err := r.db.Exec(ctx, `
		INSERT INTO incident_logs (
			id,
			machine_id,
			plc_type,
			error_code,
			issue_summary,
			ai_recommendation,
			priority,
			status,
			escalation_status
		)
		VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
	`, id,
		params.MachineID,
		params.PLCType,
		params.ErrorCode,
		params.IssueSummary,
		params.AIRecommendation,
		params.Priority,
		params.Status,
		params.EscalationStatus,
	)
	if err != nil {
		return nil, fmt.Errorf("insert incident; %w", err)
	}

	return r.GetByID(ctx, id)
}
