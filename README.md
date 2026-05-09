# Industrial IoT Technical Agent

This project is an enterprise-style AI troubleshooting platform for industrial PLC maintenance.  
Its main purpose is to help technicians diagnose machine issues faster by combining technical document retrieval, historical maintenance context, and AI reasoning into one workflow.

## What The Project Does

The platform accepts troubleshooting context such as machine ID, PLC type, error code, symptoms, and optional image evidence.  
It then processes that context through an AI agent to produce structured troubleshooting guidance, incident recommendations, and escalation-ready outputs.

At a high level, the system combines:

- AI reasoning for diagnosis and recommendation generation.
- RAG (retrieval-augmented generation) over technical documents.
- Historical maintenance lookup from SQL data.
- Workflow automation for operational notifications.
- Monitoring surfaces for operators and supervisors.

## System Components

- **AI Agent Service (Python)**: Handles reasoning flow, retrieval, image-assisted analysis, and response generation.
- **API Gateway (Go)**: Acts as the central API layer and coordinates calls between services.
- **Telemetry Service (Go)**: Provides observability and metrics plumbing.
- **Monitoring UI (Next.js)**: Presents incident, machine, and agent-run views for operational monitoring.
- **PostgreSQL + Redis**: Store maintenance context and support fast repeated access patterns.
- **n8n Automation**: Supports notification and escalation workflows.

## Architecture Overview

```text
Monitoring UI -> API Gateway -> AI Agent Service
                        |      -> PostgreSQL
                        |      -> Redis
                        |      -> n8n workflows
                        v
                 Telemetry and monitoring stack
```

## Setup

Prerequisites:

- Docker Desktop with Docker Compose enabled

Quick start:

```powershell
Copy-Item .env.example .env
docker compose up --build
```

After startup, validate these endpoints:

- API gateway health: `http://localhost:8080/health`
- AI agent health: `http://localhost:8000/health`
- Monitoring UI: `http://localhost:3000/dashboard`
- n8n: `http://localhost:5678`
- Prometheus: `http://localhost:9090`
- Grafana: `http://localhost:3001`

Environment template:

- Use [.env.example](/d:/portofolio/industrial-iot-technical-agent/.env.example) as the base for local `.env`.

## Scope Position

This repository is intentionally built as a structured portfolio-grade boilerplate.  
It focuses on correctness of architecture, service boundaries, and integration flow, while advanced production concerns and expanded product features remain outside this phase scope.
