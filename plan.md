# PLC Troubleshooting Agent - Project Plan

**Project Name:** PLC Troubleshooting Agent with RAG, SQL Memory, GPT Vision, LangGraph Reasoning, Telemetry, n8n Automation, WhatsApp Notification, and Monitoring UI

**Plan Status:** Final scope

**Version Date:** 2026-05-08

**Scope Rule:** This plan is the final implementation scope. No additional product features, extra modules, or new user-facing functions should be added after this document. Any future work must be treated as a separate project, not an extension of this portfolio build.

---

## 1. Project Goal

Build an enterprise-style AI maintenance platform for PLC troubleshooting.

The system helps field technicians diagnose PLC errors by combining:

1. Agentic AI reasoning using Python, LangChain, and LangGraph.
2. Technical document retrieval using a vector database layer.
3. Historical troubleshooting lookup from PostgreSQL.
4. Real-time telemetry and API services using Go.
5. Redis caching for fast repeated access.
6. n8n automation for notifications and WhatsApp escalation.
7. Next.js monitoring UI for supervisors and operators.
8. A model evaluation dashboard for measuring AI quality and reliability.

---

## 2. Final Scope Boundary

### Included

The project includes only the following capabilities:

1. Text-based PLC troubleshooting query.
2. Image-assisted troubleshooting using GPT Vision.
3. Technical document retrieval using RAG.
4. Multi-step reasoning using LangGraph.
5. Historical maintenance lookup from PostgreSQL.
6. Redis caching for repeated queries and recent incidents.
7. Go-based telemetry and API gateway.
8. n8n-based notification workflow.
9. WhatsApp notification through n8n integration.
10. Next.js monitoring dashboard.
11. Model evaluation dashboard.
12. Structured logging, tracing, and metrics.
13. Role-based service ownership between Role 1 and Role 2.

### Excluded

The project must not include the following in this version:

1. Predictive maintenance ML model.
2. Real-time PLC hardware integration.
3. SCADA integration.
4. User authentication system.
5. Multi-tenant organization management.
6. Payment, subscription, or billing module.
7. Mobile application.
8. Voice assistant.
9. Fine-tuning pipeline.
10. Human approval workflow beyond notification and escalation.
11. Additional notification channels beyond WhatsApp.
12. Additional dashboards beyond the main monitoring UI and model evaluation dashboard.
13. Additional vector databases beyond Pinecone and pgvector.

---

## 3. Role Separation

The project is divided into two implementation roles.

---

# Role 1 - AI Agent, RAG, Reasoning, and Evaluation

## 3.1 Role 1 Ownership

Role 1 owns the AI intelligence layer.

Role 1 is responsible for:

1. Python AI service.
2. LangChain tool integration.
3. LangGraph reasoning workflow.
4. RAG pipeline.
5. Pinecone and pgvector vector retrieval layer.
6. GPT Vision integration.
7. Prompt engineering.
8. Model evaluation dashboard.
9. Agent response quality metrics.
10. Agent test datasets.

Role 1 does not own:

1. Main API gateway.
2. Telemetry API.
3. Main monitoring UI.
4. WhatsApp notification workflow.
5. PostgreSQL history schema ownership.
6. Redis infrastructure ownership.

---

## 3.2 Role 1 Tech Stack

Use the latest stable version available at implementation time.

Baseline versions verified for this plan:

| Technology | Purpose | Baseline Version Policy |
|---|---|---|
| Python | AI service runtime | Use latest stable Python 3.x. Baseline: Python 3.14.4 |
| LangChain | Agent tools and LLM orchestration | Use latest stable `langchain` and `langchain-core` packages |
| LangGraph | Deterministic multi-step reasoning | Use latest stable LangGraph release, not alpha unless explicitly required |
| OpenAI Python SDK | GPT and Vision model access | Use latest stable `openai` Python package |
| Pinecone | Production vector database target | Use latest stable `pinecone` Python SDK |
| pgvector | Local/dev vector database target | Use latest stable pgvector extension |
| LangSmith | Model tracing and evaluation dashboard | Use latest stable LangSmith SDK and platform |
| Ragas | Offline RAG evaluation metrics | Use latest stable Ragas package |
| Pytest | Python testing | Use latest stable Pytest |

---

## 3.3 Vector Store Decision

The vector layer must support two targets:

1. **Pinecone** for production-like vector search.
2. **pgvector** for local development and CI testing.

The code must expose a single vector-store interface so the agent does not depend directly on either Pinecone or pgvector.

Final rule:

```text
Agent -> Retriever Interface -> Vector Store Adapter -> Pinecone or pgvector
```

No third vector database is allowed in this project.

---

## 3.4 Role 1 Service Name

Role 1 service name:

```text
ai-agent-service
```

Primary responsibility:

```text
Receive troubleshooting context, perform retrieval and reasoning, return structured troubleshooting recommendations.
```

---

## 3.5 Role 1 Repository Area

Role 1 owns these directories:

```text
services/ai-agent-service/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── agents/
│   │   ├── maintenance_agent.py
│   │   ├── graph.py
│   │   ├── state.py
│   │   └── prompts.py
│   ├── tools/
│   │   ├── rag_tool.py
│   │   ├── vision_tool.py
│   │   ├── history_lookup_tool.py
│   │   └── safety_tool.py
│   ├── retrievers/
│   │   ├── base.py
│   │   ├── pinecone_retriever.py
│   │   └── pgvector_retriever.py
│   ├── ingestion/
│   │   ├── load_documents.py
│   │   ├── chunk_documents.py
│   │   ├── embed_documents.py
│   │   └── index_documents.py
│   ├── evaluation/
│   │   ├── datasets/
│   │   ├── evaluators.py
│   │   ├── run_eval.py
│   │   └── metrics.py
│   └── schemas/
│       ├── agent_request.py
│       └── agent_response.py
├── tests/
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## 3.6 Role 1 Agent Flow

The agent must follow this fixed reasoning flow:

```text
1. Receive troubleshooting request from Go API.
2. Detect whether the request contains image input.
3. If image exists, analyze image using GPT Vision.
4. Extract machine_id, plc_type, error_code, and symptoms.
5. Retrieve relevant technical documents from vector database.
6. Generate first troubleshooting recommendation.
7. Run safety check on the recommendation.
8. Return structured response to Go API.
9. If issue is unresolved, query maintenance history through Go API.
10. Generate second recommendation using historical maintenance data.
11. Return final structured response.
12. Send traces and evaluation data to the model evaluation dashboard.
```

No additional reasoning steps are allowed.

---

## 3.7 LangGraph Nodes

The LangGraph workflow must contain only these nodes:

```text
1. input_parser
2. vision_analyzer
3. document_retriever
4. first_recommendation_generator
5. safety_checker
6. history_lookup_requester
7. second_recommendation_generator
8. response_formatter
9. evaluation_logger
```

Allowed edges:

```text
input_parser -> vision_analyzer
input_parser -> document_retriever
vision_analyzer -> document_retriever
document_retriever -> first_recommendation_generator
first_recommendation_generator -> safety_checker
safety_checker -> response_formatter
response_formatter -> evaluation_logger
history_lookup_requester -> second_recommendation_generator
second_recommendation_generator -> safety_checker
```

No extra LangGraph nodes should be added.

---

## 3.8 Role 1 API Contract

Role 1 exposes internal endpoints only. These endpoints are consumed by Role 2's Go API.

### POST `/agent/troubleshoot`

Purpose:

```text
Run initial troubleshooting using text, image summary, and technical document retrieval.
```

Request:

```json
{
  "request_id": "req_001",
  "machine_id": "PACK-LINE-03",
  "plc_type": "Siemens S7-1200",
  "error_code": "OB82",
  "message": "PLC shows OB82 error and the machine cannot start.",
  "image_url": "https://example.com/image.jpg"
}
```

Response:

```json
{
  "request_id": "req_001",
  "recommendation_level": "initial",
  "summary": "The error indicates a diagnostic interrupt from an I/O module.",
  "recommended_action": "Inspect the I/O module, diagnostic buffer, and connected sensor wiring.",
  "safety_warning": "Follow lockout/tagout before opening the electrical panel.",
  "retrieved_sources": [
    {
      "source_name": "siemens_s7_manual.pdf",
      "page": 42,
      "snippet": "OB82 is triggered by diagnostic interrupt..."
    }
  ],
  "confidence_score": 0.82
}
```

### POST `/agent/unresolved`

Purpose:

```text
Generate second-level recommendation after the first solution fails.
```

Request:

```json
{
  "request_id": "req_001",
  "machine_id": "PACK-LINE-03",
  "error_code": "OB82",
  "attempted_solution": "Restarted I/O module and checked diagnostic buffer.",
  "maintenance_history": [
    {
      "root_cause": "Faulty digital input module",
      "solution_applied": "Replaced DI module",
      "success_status": true
    }
  ]
}
```

Response:

```json
{
  "request_id": "req_001",
  "recommendation_level": "second_level",
  "summary": "Previous similar cases suggest the digital input module may be faulty.",
  "recommended_action": "Inspect and test the DI module connected to the affected sensor line.",
  "safety_warning": "De-energize the panel before hardware inspection.",
  "confidence_score": 0.87
}
```

---

## 3.9 Role 1 Evaluation Dashboard

The model evaluation dashboard must track only these metrics:

1. Retrieval precision.
2. Retrieval relevance score.
3. Answer groundedness.
4. Answer correctness.
5. Safety compliance.
6. Tool-call success rate.
7. Hallucination flag rate.
8. Average agent latency.
9. First recommendation success rate.
10. Second recommendation success rate.

The dashboard source of truth is LangSmith.

Ragas is used only for offline RAG evaluation.

No additional evaluation metrics should be added.

---

# Role 2 - API, Telemetry, Database, Cache, Automation, and UI

## 4.1 Role 2 Ownership

Role 2 owns the platform and operations layer.

Role 2 is responsible for:

1. Go API gateway.
2. Telemetry service.
3. PostgreSQL maintenance history database.
4. Redis cache.
5. n8n notification workflow.
6. WhatsApp notification integration.
7. Main Next.js monitoring UI.
8. Incident logging.
9. Service-to-service communication.
10. Observability pipeline.

Role 2 does not own:

1. Agent reasoning logic.
2. Prompt design.
3. RAG implementation.
4. Vector embedding pipeline.
5. Model evaluation scoring logic.

---

## 4.2 Role 2 Tech Stack

Use the latest stable version available at implementation time.

Baseline versions verified for this plan:

| Technology | Purpose | Baseline Version Policy |
|---|---|---|
| Go | API gateway and telemetry service | Use latest stable Go. Baseline: Go 1.26.3 |
| PostgreSQL | Maintenance history and incident logs | Use latest stable major version. Baseline: PostgreSQL 18.x |
| Redis | Cache layer | Use latest stable Redis 8.x |
| n8n | Notification and WhatsApp workflow automation | Use latest stable n8n release |
| Next.js | Main monitoring UI | Use latest stable Next.js. Baseline: Next.js 16.x |
| OpenTelemetry Go | Tracing and metrics instrumentation | Use latest stable OpenTelemetry Go SDK |
| Grafana | Telemetry visualization | Use latest stable Grafana |
| Prometheus | Metrics storage | Use latest stable Prometheus |
| Docker Compose | Local orchestration | Use latest stable Docker Compose |

---

## 4.3 Role 2 Service Names

Role 2 owns these services:

```text
api-gateway
telemetry-service
monitoring-ui
n8n-workflows
postgres-db
redis-cache
```

---

## 4.4 Role 2 Repository Area

Role 2 owns these directories:

```text
services/api-gateway/
├── cmd/
│   └── api/
│       └── main.go
├── internal/
│   ├── handlers/
│   ├── services/
│   ├── clients/
│   ├── middleware/
│   ├── telemetry/
│   ├── cache/
│   └── database/
├── migrations/
├── tests/
├── go.mod
└── README.md

services/telemetry-service/
├── cmd/
│   └── telemetry/
│       └── main.go
├── internal/
│   ├── collectors/
│   ├── metrics/
│   ├── traces/
│   └── exporters/
├── go.mod
└── README.md

apps/monitoring-ui/
├── app/
├── components/
├── lib/
├── hooks/
├── types/
├── package.json
└── README.md

automation/n8n/
├── workflows/
│   ├── incident_notification.json
│   └── whatsapp_escalation.json
└── payload_examples/
    ├── incident_notification_payload.json
    └── whatsapp_escalation_payload.json
```

---

## 4.5 Go API Gateway Responsibilities

The Go API gateway must expose only these public endpoints:

```text
GET    /health
POST   /api/troubleshoot
POST   /api/troubleshoot/unresolved
POST   /api/incidents/escalate
GET    /api/incidents
GET    /api/incidents/{incident_id}
GET    /api/machines
GET    /api/telemetry/summary
```

No additional public endpoints are allowed.

---

## 4.6 PostgreSQL Schema Ownership

Role 2 owns the database schema.

Required tables:

```text
machines
maintenance_history
incident_logs
agent_runs
notification_logs
```

No additional tables are allowed in this final version.

### machines

```sql
CREATE TABLE machines (
    id UUID PRIMARY KEY,
    machine_id VARCHAR(100) UNIQUE NOT NULL,
    machine_name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    plc_type VARCHAR(255),
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### maintenance_history

```sql
CREATE TABLE maintenance_history (
    id UUID PRIMARY KEY,
    machine_id VARCHAR(100) NOT NULL,
    error_code VARCHAR(100) NOT NULL,
    root_cause TEXT,
    solution_applied TEXT,
    success_status BOOLEAN,
    downtime_minutes INTEGER,
    technician_notes TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### incident_logs

```sql
CREATE TABLE incident_logs (
    id UUID PRIMARY KEY,
    machine_id VARCHAR(100) NOT NULL,
    plc_type VARCHAR(255),
    error_code VARCHAR(100),
    issue_summary TEXT,
    ai_recommendation TEXT,
    priority VARCHAR(50) NOT NULL DEFAULT 'medium',
    status VARCHAR(50) NOT NULL DEFAULT 'open',
    escalation_status VARCHAR(50) NOT NULL DEFAULT 'not_escalated',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### agent_runs

```sql
CREATE TABLE agent_runs (
    id UUID PRIMARY KEY,
    request_id VARCHAR(100) UNIQUE NOT NULL,
    incident_id UUID,
    machine_id VARCHAR(100),
    error_code VARCHAR(100),
    recommendation_level VARCHAR(50),
    confidence_score NUMERIC(5, 4),
    latency_ms INTEGER,
    tool_call_success BOOLEAN,
    safety_passed BOOLEAN,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

### notification_logs

```sql
CREATE TABLE notification_logs (
    id UUID PRIMARY KEY,
    incident_id UUID NOT NULL,
    channel VARCHAR(50) NOT NULL,
    recipient VARCHAR(255),
    message_summary TEXT,
    delivery_status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);
```

---

## 4.7 Redis Cache Responsibilities

Redis must cache only these objects:

1. Recent troubleshooting response by request_id.
2. Recent incident summary by incident_id.
3. Machine metadata by machine_id.
4. Maintenance history lookup by machine_id and error_code.

Default TTL:

```text
15 minutes
```

No long-term data should be stored in Redis.

---

## 4.8 n8n Workflow Responsibilities

n8n must contain only two workflows:

```text
1. incident_notification
2. whatsapp_escalation
```

### Workflow 1: incident_notification

Trigger:

```text
Webhook from Go API Gateway
```

Steps:

```text
1. Receive incident payload.
2. Validate required fields.
3. Format notification message.
4. Send internal notification.
5. Return delivery status to Go API.
```

### Workflow 2: whatsapp_escalation

Trigger:

```text
Webhook from Go API Gateway when priority is high or issue is unresolved.
```

Steps:

```text
1. Receive escalation payload.
2. Validate machine_id, error_code, priority, and recommendation.
3. Format WhatsApp message.
4. Send WhatsApp notification to supervisor.
5. Return delivery status to Go API.
```

No additional n8n workflows are allowed.

---

## 4.9 Next.js Monitoring UI

The main monitoring UI must include only these pages:

```text
1. /dashboard
2. /incidents
3. /incidents/[id]
4. /machines
5. /telemetry
6. /agent-runs
```

No additional pages are allowed.

### Dashboard Page

Displays:

1. Open incidents.
2. High-priority incidents.
3. Average agent confidence score.
4. Average troubleshooting latency.
5. Notification success rate.

### Incidents Page

Displays:

1. Incident list.
2. Machine ID.
3. Error code.
4. Priority.
5. Status.
6. Escalation status.
7. Created time.

### Incident Detail Page

Displays:

1. Incident summary.
2. AI recommendation.
3. Retrieved source summary.
4. Agent confidence score.
5. Notification status.
6. Maintenance history used.

### Machines Page

Displays:

1. Machine list.
2. Location.
3. PLC type.
4. Recent incident count.

### Telemetry Page

Displays:

1. API request count.
2. API latency.
3. Agent latency.
4. Error rate.
5. n8n workflow success rate.

### Agent Runs Page

Displays:

1. Request ID.
2. Machine ID.
3. Error code.
4. Recommendation level.
5. Confidence score.
6. Safety status.
7. Tool-call status.
8. Latency.

---

## 5. System Architecture

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

Go API Gateway
    |
    v
Redis Cache

Go API Gateway
    |
    v
n8n Workflows
    |
    v
WhatsApp Notification

All Services
    |
    v
Telemetry Service
    |
    v
Prometheus / Grafana

Python AI Agent Service
    |
    v
LangSmith / Ragas Evaluation Dashboard
```

---

## 6. End-to-End Request Flow

### Initial Troubleshooting Flow

```text
1. Technician submits PLC issue from Next.js UI.
2. Next.js sends request to Go API Gateway.
3. Go API checks Redis cache.
4. If cache miss, Go API forwards request to Python AI Agent Service.
5. Python service runs LangGraph workflow.
6. Agent retrieves technical documents from Pinecone or pgvector.
7. Agent analyzes image if image input is present.
8. Agent returns recommendation to Go API.
9. Go API stores incident and agent run in PostgreSQL.
10. Go API caches response in Redis.
11. Go API returns response to Next.js UI.
12. Telemetry is recorded.
13. Evaluation traces are logged to LangSmith.
```

### Unresolved Issue Flow

```text
1. Technician marks issue as unresolved.
2. Next.js sends unresolved request to Go API Gateway.
3. Go API queries PostgreSQL maintenance history.
4. Go API sends maintenance history to Python AI Agent Service.
5. LangGraph generates second-level recommendation.
6. Go API stores updated incident and agent run.
7. If priority is high, Go API triggers n8n WhatsApp escalation.
8. n8n sends WhatsApp message to supervisor.
9. Go API records notification status.
10. Next.js UI displays updated incident status.
```

---

## 7. Cross-Role API Contract

Role 1 and Role 2 must communicate using HTTP JSON APIs only.

Role 2 calls Role 1.

Role 1 must not directly write to PostgreSQL, Redis, n8n, or Next.js.

Role 1 returns AI output.

Role 2 persists, caches, displays, and triggers notifications.

---

## 8. Final Monorepo Architecture

```text
plc-troubleshooting-agent/
├── README.md
├── plan.md
├── docker-compose.yml
├── .env.example
├── docs/
│   ├── architecture.md
│   ├── api_contract.md
│   ├── ai_agent_design.md
│   ├── database_schema.md
│   ├── evaluation_plan.md
│   └── n8n_workflows.md
│
├── services/
│   ├── ai-agent-service/
│   │   ├── app/
│   │   ├── tests/
│   │   ├── pyproject.toml
│   │   ├── requirements.txt
│   │   └── README.md
│   │
│   ├── api-gateway/
│   │   ├── cmd/
│   │   ├── internal/
│   │   ├── migrations/
│   │   ├── tests/
│   │   ├── go.mod
│   │   └── README.md
│   │
│   └── telemetry-service/
│       ├── cmd/
│       ├── internal/
│       ├── go.mod
│       └── README.md
│
├── apps/
│   └── monitoring-ui/
│       ├── app/
│       ├── components/
│       ├── lib/
│       ├── hooks/
│       ├── types/
│       ├── package.json
│       └── README.md
│
├── automation/
│   └── n8n/
│       ├── workflows/
│       │   ├── incident_notification.json
│       │   └── whatsapp_escalation.json
│       └── payload_examples/
│           ├── incident_notification_payload.json
│           └── whatsapp_escalation_payload.json
│
├── infrastructure/
│   ├── postgres/
│   │   ├── schema.sql
│   │   └── seed.sql
│   ├── redis/
│   ├── prometheus/
│   │   └── prometheus.yml
│   └── grafana/
│       └── dashboards/
│
├── data/
│   ├── technical_docs/
│   ├── sample_images/
│   └── eval_datasets/
│
└── scripts/
    ├── bootstrap.sh
    ├── run_local.sh
    └── run_tests.sh
```

No additional top-level directories are allowed.

---

## 9. Development Milestones

## Milestone 1 - Foundation

Owner: Role 1 and Role 2

Deliverables:

1. Monorepo structure.
2. Docker Compose.
3. Environment files.
4. PostgreSQL schema.
5. Redis service.
6. Basic Go API health endpoint.
7. Basic Python AI service health endpoint.
8. Basic Next.js dashboard shell.

Acceptance criteria:

```text
All services start locally through Docker Compose.
Health checks return success.
Database migrations run successfully.
```

---

## Milestone 2 - AI Agent and RAG

Owner: Role 1

Deliverables:

1. LangChain tools.
2. LangGraph workflow.
3. Pinecone adapter.
4. pgvector adapter.
5. Technical document ingestion pipeline.
6. Initial troubleshooting endpoint.
7. Vision analysis integration.
8. Safety checker.

Acceptance criteria:

```text
The AI agent can receive a PLC error query, retrieve documents, analyze optional image input, and return a structured recommendation.
```

---

## Milestone 3 - API, History, and Cache

Owner: Role 2

Deliverables:

1. Go API Gateway endpoints.
2. PostgreSQL history queries.
3. Incident logging.
4. Agent run logging.
5. Redis caching.
6. Service-to-service client for Python AI service.

Acceptance criteria:

```text
The Go API can receive troubleshooting requests, call the AI service, store results, cache responses, and return data to the UI.
```

---

## Milestone 4 - n8n and WhatsApp Automation

Owner: Role 2

Deliverables:

1. incident_notification n8n workflow.
2. whatsapp_escalation n8n workflow.
3. Payload examples.
4. Delivery status logging.
5. Go API integration with n8n webhook.

Acceptance criteria:

```text
High-priority or unresolved incidents trigger n8n and produce a WhatsApp escalation notification.
```

---

## Milestone 5 - Monitoring UI and Telemetry

Owner: Role 2

Deliverables:

1. Next.js dashboard.
2. Incident list page.
3. Incident detail page.
4. Machines page.
5. Telemetry page.
6. Agent runs page.
7. OpenTelemetry instrumentation.
8. Prometheus and Grafana dashboards.

Acceptance criteria:

```text
The UI displays incidents, machines, agent runs, and telemetry summaries from the Go API.
```

---

## Milestone 6 - Model Evaluation Dashboard

Owner: Role 1

Deliverables:

1. LangSmith tracing.
2. Evaluation dataset.
3. Ragas evaluation script.
4. Metrics export.
5. Evaluation dashboard documentation.

Acceptance criteria:

```text
The model evaluation dashboard shows retrieval quality, groundedness, correctness, safety compliance, latency, and tool-call success rate.
```

---

## Milestone 7 - Final Demo

Owner: Role 1 and Role 2

Deliverables:

1. End-to-end demo scenario.
2. README.
3. Architecture documentation.
4. API contract documentation.
5. Demo screenshots.
6. Final test run.

Acceptance criteria:

```text
A reviewer can run the project locally, submit a PLC troubleshooting case, receive an AI recommendation, mark the issue unresolved, trigger second-level reasoning, send WhatsApp escalation, and monitor the incident in the Next.js UI.
```

---

## 10. Testing Scope

### Role 1 Tests

Role 1 must provide tests for:

1. RAG retrieval.
2. pgvector adapter.
3. Pinecone adapter.
4. LangGraph node transitions.
5. Vision analysis mock.
6. Safety checker.
7. Agent response schema.
8. Evaluation metrics script.

### Role 2 Tests

Role 2 must provide tests for:

1. Go API handlers.
2. PostgreSQL queries.
3. Redis cache behavior.
4. Python AI service client.
5. n8n webhook client.
6. Incident logging.
7. Telemetry instrumentation.
8. Next.js API integration mocks.

---

## 11. Environment Variables

Required environment variables:

```text
APP_ENV=local

# Python AI Service
OPENAI_API_KEY=
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=plc-troubleshooting-agent
PINECONE_API_KEY=
PINECONE_INDEX_NAME=plc-technical-docs
VECTOR_STORE_PROVIDER=pgvector

# Go API Gateway
API_PORT=8080
AI_AGENT_SERVICE_URL=http://ai-agent-service:8000
DATABASE_URL=postgres://postgres:postgres@postgres-db:5432/plc_agent?sslmode=disable
REDIS_URL=redis://redis-cache:6379
N8N_INCIDENT_WEBHOOK_URL=
N8N_WHATSAPP_WEBHOOK_URL=

# PostgreSQL
POSTGRES_DB=plc_agent
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

# Redis
REDIS_HOST=redis-cache
REDIS_PORT=6379

# Next.js
NEXT_PUBLIC_API_BASE_URL=http://localhost:8080

# Telemetry
OTEL_EXPORTER_OTLP_ENDPOINT=http://telemetry-service:4317
PROMETHEUS_PORT=9090
GRAFANA_PORT=3001
```

No additional required environment variables are allowed.

---

## 12. Final Demo Scenario

The final demo must use this single scenario:

```text
Machine: PACK-LINE-03
PLC Type: Siemens S7-1200
Error Code: OB82
Symptom: Machine cannot start after I/O module fault indicator appears.
Image Input: PLC panel or HMI screenshot showing fault condition.
```

Demo flow:

```text
1. Technician opens Next.js monitoring UI.
2. Technician submits machine ID, PLC type, error code, issue description, and image.
3. Go API forwards request to Python AI service.
4. AI agent analyzes image and retrieves relevant technical documents.
5. AI agent returns initial recommendation.
6. Technician marks issue as unresolved.
7. Go API retrieves maintenance history from PostgreSQL.
8. AI agent generates second-level recommendation.
9. Go API triggers n8n WhatsApp escalation.
10. Supervisor receives WhatsApp notification.
11. Incident appears in monitoring UI.
12. Telemetry and model evaluation dashboards record the run.
```

No other demo scenario should be used for the final portfolio presentation.

---

## 13. Definition of Done

The project is complete only when all conditions below are satisfied:

1. Docker Compose starts all services.
2. Go API health check works.
3. Python AI service health check works.
4. Next.js monitoring UI loads successfully.
5. PostgreSQL schema is created successfully.
6. Redis cache is connected.
7. Technical document ingestion works.
8. Initial troubleshooting flow works.
9. Unresolved issue flow works.
10. n8n WhatsApp escalation works.
11. Incident is visible in the monitoring UI.
12. Agent runs are visible in the monitoring UI.
13. Telemetry metrics are visible in Grafana.
14. Model evaluation dashboard contains at least one complete evaluation run.
15. README explains local setup and final demo flow.
16. No features outside this plan are implemented.

---

## 14. Final Instruction

This document is the final project plan.

Implementation must follow this document exactly.

Do not add new features, new services, new dashboards, new workflows, new public API endpoints, new database tables, or new top-level repository directories unless a new project plan is created separately.