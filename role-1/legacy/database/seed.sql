INSERT INTO machines (machine_id, machine_name, location, plc_type)
VALUES
    ('PLC-001', 'Filling Line 1', 'Packaging Area', 'Siemens S7-1200'),
    ('PLC-002', 'Conveyor Line A', 'Assembly Area', 'Allen-Bradley CompactLogix')
ON CONFLICT (machine_id) DO NOTHING;

INSERT INTO maintenance_history (
    machine_id,
    error_code,
    root_cause,
    solution_applied,
    success_status,
    downtime_minutes,
    technician_notes
)
VALUES
    (
        'PLC-001',
        'E-STOP',
        'Emergency stop circuit was not fully reset.',
        'Verified E-stop chain and reset safety relay.',
        TRUE,
        18,
        'Check safety relay indicator before restarting.'
    ),
    (
        'PLC-002',
        'OL-101',
        'Motor overload after conveyor jam.',
        'Removed jam and reset overload relay.',
        TRUE,
        42,
        'Inspect conveyor bearings during next preventive maintenance.'
    );
