package repository

import (
	"context"
	"fmt"
	"time"

	"github.com/jackc/pgx/v5/pgxpool"
)

type Machine struct {
	ID          string    `json:"id"`
	MachineID   string    `json:"machine_id"`
	MachineName string    `json:"machine_name"`
	Location    string    `json:"location"`
	PLCType     string    `json:"plc_type"`
	CreatedAt   time.Time `json:"created_at"`
}

type MachineRepository struct {
	db *pgxpool.Pool
}

func NewMachineRepository(db *pgxpool.Pool) *MachineRepository {
	return &MachineRepository{db: db}
}

func (r *MachineRepository) List(ctx context.Context) ([]Machine, error) {
	rows, err := r.db.Query(ctx, `
	SELECT id, machine_id, machine_name, location, plc_type, created_at
	FROM machines
	ORDER BY machine_id
	`)

	if err != nil {
		return nil, fmt.Errorf("query machine: %w", err)
	}
	defer rows.Close()

	machines := make([]Machine, 0)

	for rows.Next() {
		var machine Machine

		if err := rows.Scan(
			&machine.ID,
			&machine.MachineID,
			&machine.MachineName,
			&machine.PLCType,
			&machine.Location,
			&machine.CreatedAt,
		); err != nil {
			return nil, fmt.Errorf("scan machine: %w", err)
		}

		machines = append(machines, machine)
	}

	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("iterate machines: %w", err)
	}

	return machines, nil
}
