from __future__ import annotations

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path
from uuid import uuid4


OUTPUT_DIR = Path("data/generated")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


PLC_TYPES = [
    "Siemens S7-1200",
    "Siemens S7-1500",
    "Omron CJ2M",
    "Allen-Bradley CompactLogix",
    "Mitsubishi FX5U",
]

MACHINE_TYPES = [
    "Packaging Line",
    "Filling Machine",
    "Conveyor System",
    "Labeling Machine",
    "Palletizer",
    "Mixer",
    "Compressor",
    "Sorting Machine",
]

LOCATIONS = [
    "Plant A - Line 1",
    "Plant A - Line 2",
    "Plant B - Packaging Area",
    "Plant B - Utility Area",
    "Warehouse Automation Zone",
]

ERROR_CODES = [
    {
        "code": "OB82",
        "category": "Diagnostic Interrupt",
        "root_causes": [
            "Faulty digital input module",
            "Sensor wiring loose",
            "I/O module diagnostic fault",
            "24V supply instability",
        ],
        "solutions": [
            "Inspect digital input module",
            "Check field sensor wiring",
            "Verify 24V power supply",
            "Replace faulty I/O module",
        ],
    },
    {
        "code": "OB86",
        "category": "Rack Failure",
        "root_causes": [
            "Remote I/O rack disconnected",
            "PROFINET communication failure",
            "ET200SP power module fault",
        ],
        "solutions": [
            "Check remote rack communication",
            "Inspect PROFINET cable",
            "Restart remote I/O rack",
            "Replace power module",
        ],
    },
    {
        "code": "F001",
        "category": "Drive Fault",
        "root_causes": [
            "Motor overload",
            "Inverter overcurrent",
            "Cooling fan failure",
            "Mechanical jam",
        ],
        "solutions": [
            "Reset overload relay",
            "Inspect motor current",
            "Check inverter cooling fan",
            "Inspect mechanical load",
        ],
    },
    {
        "code": "E101",
        "category": "Sensor Fault",
        "root_causes": [
            "Dirty proximity sensor",
            "Broken sensor cable",
            "Sensor misalignment",
            "Incorrect input mapping",
        ],
        "solutions": [
            "Clean proximity sensor",
            "Replace sensor cable",
            "Realign sensor position",
            "Validate PLC input mapping",
        ],
    },
    {
        "code": "P204",
        "category": "Pressure Alarm",
        "root_causes": [
            "Low pneumatic pressure",
            "Air leak in actuator line",
            "Faulty pressure switch",
        ],
        "solutions": [
            "Check compressor pressure",
            "Inspect pneumatic hose",
            "Replace pressure switch",
            "Reset pressure alarm",
        ],
    },
]


def random_date_within(days: int = 365) -> str:
    date = datetime.now() - timedelta(
        days=random.randint(0, days),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
    )
    return date.strftime("%Y-%m-%d %H:%M:%S")


def write_csv(file_path: Path, rows: list[dict]) -> None:
    if not rows:
        return

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def generate_machines(count: int = 50) -> list[dict]:
    machines = []

    for index in range(1, count + 1):
        machine_type = random.choice(MACHINE_TYPES)
        machine_id = f"{machine_type.upper().replace(' ', '-')}-{index:03d}"

        machines.append(
            {
                "id": index,
                "machine_id": machine_id,
                "machine_name": f"{machine_type} {index}",
                "location": random.choice(LOCATIONS),
                "plc_type": random.choice(PLC_TYPES),
                "status": random.choice(["running", "idle", "maintenance", "fault"]),
                "created_at": random_date_within(900),
            }
        )

    return machines


def generate_maintenance_history(
    machines: list[dict],
    count: int = 2000,
) -> list[dict]:
    rows = []

    for index in range(1, count + 1):
        machine = random.choice(machines)
        error = random.choice(ERROR_CODES)

        root_cause = random.choice(error["root_causes"])
        solution = random.choice(error["solutions"])
        success_status = random.choices([True, False], weights=[0.78, 0.22])[0]

        downtime = random.randint(10, 240)
        if not success_status:
            downtime += random.randint(30, 180)

        rows.append(
            {
                "id": index,
                "machine_id": machine["machine_id"],
                "plc_type": machine["plc_type"],
                "error_code": error["code"],
                "error_category": error["category"],
                "root_cause": root_cause,
                "solution_applied": solution,
                "success_status": success_status,
                "downtime_minutes": downtime,
                "technician_notes": generate_technician_note(
                    error_code=error["code"],
                    root_cause=root_cause,
                    solution=solution,
                    success=success_status,
                ),
                "created_at": random_date_within(730),
            }
        )

    return rows


def generate_technician_note(
    error_code: str,
    root_cause: str,
    solution: str,
    success: bool,
) -> str:
    if success:
        templates = [
            f"Error {error_code} resolved after {solution.lower()}. Root cause: {root_cause.lower()}.",
            f"Technician confirmed normal operation after applying: {solution}.",
            f"Machine restarted successfully. Root cause identified as {root_cause.lower()}.",
        ]
    else:
        templates = [
            f"Initial action {solution.lower()} did not resolve error {error_code}. Further inspection required.",
            f"Temporary recovery only. Suspected root cause: {root_cause.lower()}.",
            f"Issue returned after restart. Escalation recommended.",
        ]

    return random.choice(templates)


def generate_incident_logs(
    machines: list[dict],
    count: int = 1000,
) -> list[dict]:
    rows = []

    for index in range(1, count + 1):
        machine = random.choice(machines)
        error = random.choice(ERROR_CODES)

        priority = random.choices(
            ["low", "medium", "high", "critical"],
            weights=[0.2, 0.45, 0.25, 0.1],
        )[0]

        escalation_status = random.choices(
            ["not_escalated", "escalated", "resolved", "pending_review"],
            weights=[0.35, 0.25, 0.3, 0.1],
        )[0]

        recommendation = random.choice(error["solutions"])

        rows.append(
            {
                "id": index,
                "incident_id": f"INC-{datetime.now().year}-{index:05d}",
                "machine_id": machine["machine_id"],
                "plc_type": machine["plc_type"],
                "error_code": error["code"],
                "priority": priority,
                "issue_summary": f"{error['category']} detected on {machine['machine_name']}.",
                "ai_recommendation": recommendation,
                "escalation_status": escalation_status,
                "notification_channel": random.choice(["whatsapp", "email", "slack", "none"]),
                "created_at": random_date_within(365),
            }
        )

    return rows


def generate_telemetry_events(
    machines: list[dict],
    count: int = 10000,
) -> list[dict]:
    rows = []

    for index in range(1, count + 1):
        machine = random.choice(machines)

        motor_temp = round(random.normalvariate(65, 12), 2)
        vibration = round(abs(random.normalvariate(2.5, 1.2)), 2)
        current_amp = round(random.normalvariate(12, 4), 2)
        pressure_bar = round(random.normalvariate(6, 1.5), 2)

        risk_score = calculate_risk_score(
            motor_temp=motor_temp,
            vibration=vibration,
            current_amp=current_amp,
            pressure_bar=pressure_bar,
        )

        rows.append(
            {
                "id": index,
                "event_id": str(uuid4()),
                "machine_id": machine["machine_id"],
                "motor_temperature_c": motor_temp,
                "vibration_mm_s": vibration,
                "current_amp": current_amp,
                "pressure_bar": pressure_bar,
                "cycle_count": random.randint(1000, 500000),
                "risk_score": risk_score,
                "machine_status": classify_machine_status(risk_score),
                "timestamp": random_date_within(90),
            }
        )

    return rows


def calculate_risk_score(
    motor_temp: float,
    vibration: float,
    current_amp: float,
    pressure_bar: float,
) -> float:
    score = 0.0

    if motor_temp > 80:
        score += 0.3
    if vibration > 4.5:
        score += 0.3
    if current_amp > 18:
        score += 0.2
    if pressure_bar < 4:
        score += 0.2

    score += random.uniform(0, 0.15)

    return round(min(score, 1.0), 2)


def classify_machine_status(risk_score: float) -> str:
    if risk_score >= 0.75:
        return "critical"
    if risk_score >= 0.5:
        return "warning"
    if risk_score >= 0.25:
        return "attention"
    return "normal"


def generate_hmi_alarm_events(
    machines: list[dict],
    count: int = 1500,
) -> list[dict]:
    rows = []

    for index in range(1, count + 1):
        machine = random.choice(machines)
        error = random.choice(ERROR_CODES)

        rows.append(
            {
                "id": index,
                "alarm_id": f"ALM-{index:05d}",
                "machine_id": machine["machine_id"],
                "plc_type": machine["plc_type"],
                "error_code": error["code"],
                "alarm_message": f"{error['category']} detected. Check {random.choice(error['root_causes']).lower()}.",
                "severity": random.choice(["info", "warning", "major", "critical"]),
                "acknowledged": random.choice([True, False]),
                "operator_action": random.choice(
                    [
                        "Reset alarm",
                        "Checked sensor",
                        "Called maintenance",
                        "Stopped machine",
                        "Restarted PLC module",
                    ]
                ),
                "timestamp": random_date_within(180),
            }
        )

    return rows


def main() -> None:
    random.seed(42)

    machines = generate_machines(count=50)
    maintenance_history = generate_maintenance_history(machines, count=2000)
    incident_logs = generate_incident_logs(machines, count=1000)
    telemetry_events = generate_telemetry_events(machines, count=10000)
    hmi_alarm_events = generate_hmi_alarm_events(machines, count=1500)

    write_csv(OUTPUT_DIR / "machines.csv", machines)
    write_csv(OUTPUT_DIR / "maintenance_history.csv", maintenance_history)
    write_csv(OUTPUT_DIR / "incident_logs.csv", incident_logs)
    write_csv(OUTPUT_DIR / "telemetry_events.csv", telemetry_events)
    write_csv(OUTPUT_DIR / "hmi_alarm_events.csv", hmi_alarm_events)

    print("Dummy datasets generated successfully.")
    print(f"Output directory: {OUTPUT_DIR.resolve()}")
    print(f"machines.csv: {len(machines)} rows")
    print(f"maintenance_history.csv: {len(maintenance_history)} rows")
    print(f"incident_logs.csv: {len(incident_logs)} rows")
    print(f"telemetry_events.csv: {len(telemetry_events)} rows")
    print(f"hmi_alarm_events.csv: {len(hmi_alarm_events)} rows")


if __name__ == "__main__":
    main()