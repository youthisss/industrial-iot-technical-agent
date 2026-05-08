# AI Agent Service

Role 1 boilerplate service for troubleshooting recommendations.

Endpoints:

- `GET /health`
- `POST /agent/troubleshoot`
- `POST /agent/unresolved`

The service exposes a retriever interface with Pinecone and pgvector adapters, fixed LangGraph-style node names, GPT Vision placeholder analysis, safety checking, and evaluation metric placeholders.
