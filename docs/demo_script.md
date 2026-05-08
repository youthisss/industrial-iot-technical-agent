# Demo Script

## Scenario

A technician is working on `Filling Line 1` with machine ID `PLC-001`. The line stopped after an emergency stop event and the HMI still reports `E-STOP`.

## Setup

1. Start backend:

```bash
uvicorn app.main:app --reload --port 8000
```

2. Ingest documents:

```bash
python ingestion/ingest_documents.py
```

3. Start Streamlit:

```bash
streamlit run frontend/streamlit_app.py
```

## Walkthrough

1. Enter machine ID `PLC-001`.
2. Enter PLC type `Siemens S7-1200`.
3. Enter error code `E-STOP`.
4. Ask: `What should I check after an emergency stop reset?`
5. Show the agent recommendation.
6. Expand retrieved sources to show the manual evidence.
7. Show maintenance history for a similar previous event.
8. Click `Issue Not Resolved`.
9. Click `Escalate` and explain the n8n webhook handoff.

## Talk Track

The agent gives technicians a structured first response: safety check, relevant manual context, historical fixes, and escalation workflow readiness.
