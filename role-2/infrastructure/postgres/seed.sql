INSERT INTO machines (id, machine_id, machine_name, location, plc_type)
VALUES ('00000000-0000-0000-0000-000000000001', 'PACK-LINE-03', 'Packaging Line 03', 'Line A', 'Siemens S7-1200')
ON CONFLICT (machine_id) DO NOTHING;

INSERT INTO maintenance_history (
    id,
    machine_id,
    error_code,
    root_cause,
    solution_applied,
    success_status,
    downtime_minutes,
    technician_notes
)
VALUES (
    '00000000-0000-0000-0000-000000000101',
    'PACK-LINE-03',
    'OB82',
    'Faulty digital input module',
    'Replaced DI module',
    true,
    45,
    'Use as final demo history case only.'
);
