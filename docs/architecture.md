# Architecture

```text
Field Technician
    |
    v
Next.js Monitoring UI
    |
    v
Go API Gateway
    |----------------------------|
    |                            |
    v                            v
Python AI Agent Service       PostgreSQL
    |                            |
    v                            v
LangGraph Reasoning          Maintenance History
    |
    v
LangChain Tools
    |----------------------------|
    |                            |
    v                            v
Pinecone / pgvector          GPT Vision
    |
    v
Technical Documents

Go API Gateway -> Redis Cache
Go API Gateway -> n8n Workflows -> WhatsApp Notification
All Services -> Telemetry Service -> Prometheus / Grafana
Python AI Agent Service -> LangSmith / Ragas Evaluation Dashboard
```

The monorepo is divided by `plan.md` role ownership. Role 1 owns AI reasoning, retrieval, vision, and evaluation. Role 2 owns API, telemetry, database, cache, n8n, WhatsApp integration, and the monitoring UI.
