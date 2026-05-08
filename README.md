# PLC Troubleshooting Agent

Enterprise-style boilerplate for PLC troubleshooting with a Python AI agent service, Go API gateway, PostgreSQL history, Redis cache, n8n WhatsApp escalation, a Next.js monitoring UI, and evaluation/telemetry scaffolding.

This repository follows `plan.md` as the final scope. The code is intentionally boilerplate-first: interfaces, contracts, service boundaries, and mock responses are present, but production integrations still need real credentials and implementation work.

## Final Architecture

```text
Next.js Monitoring UI -> Go API Gateway -> Python AI Agent Service
                                  |       -> PostgreSQL
                                  |       -> Redis
                                  |       -> n8n WhatsApp workflows
                                  v
                           Telemetry Service -> Prometheus / Grafana

Python AI Agent Service -> LangGraph-style workflow
                        -> Retriever interface
                        -> Pinecone or pgvector adapter
                        -> LangSmith / Ragas evaluation hooks
```

## Plan-Aligned Areas

- `services/ai-agent-service` contains the Role 1 Python AI service boilerplate.
- `services/api-gateway` contains the Role 2 Go API gateway boilerplate.
- `services/telemetry-service` contains telemetry service boilerplate.
- `apps/monitoring-ui` contains the plan-scoped Next.js monitoring UI pages.
- `automation/n8n` contains exactly the two planned workflow exports and payload examples.
- `infrastructure` contains PostgreSQL, Redis, Prometheus, and Grafana starter assets.
- `data` contains technical docs, sample image notes, and evaluation dataset placeholders.
- `docs` contains architecture, API, AI-agent, database, evaluation, and n8n design notes.

## Local Setup

```powershell
Copy-Item .env.example .env
docker compose up
```

Expected local endpoints:

- AI agent service: `http://localhost:8000/health`
- Go API gateway: `http://localhost:8080/health`
- Monitoring UI: `http://localhost:3000/dashboard`
- n8n: `http://localhost:5678`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3001`

## Final Demo Scenario

Use only this demo case:

- Machine: `PACK-LINE-03`
- PLC type: `Siemens S7-1200`
- Error code: `OB82`
- Symptom: `Machine cannot start after I/O module fault indicator appears.`
- Image input: PLC panel or HMI screenshot showing the fault condition.

## Scope Notes

The final plan excludes authentication, predictive maintenance ML, SCADA integration, mobile apps, extra dashboards, extra notification channels, and any vector database beyond Pinecone and pgvector.

Legacy files from the earlier scaffold may still exist in this workspace because the folder is not currently a Git repository. The plan-aligned boilerplate lives in the directories listed above.
