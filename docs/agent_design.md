# Agent Design

`MaintenanceAgent` is the main orchestration class. It exposes four portfolio-facing methods:

- `run_text_query()`: handles standard text troubleshooting.
- `run_multimodal_query()`: combines text troubleshooting with image analysis.
- `handle_unresolved_issue()`: prepares an unresolved incident payload.
- `escalate_incident()`: sends an escalation payload through n8n.

## Current Behavior

The initial implementation uses deterministic mock logic:

- Keyword document retrieval.
- SQL history fallback for `PLC-001`.
- Mock vision summary.
- Dry-run n8n response when `N8N_WEBHOOK_URL` is not set.

## Future LangChain Path

The tool classes are designed to become LangChain tools:

- `RAGTool` can become a retriever tool.
- `SQLHistoryTool` can become a structured SQL tool.
- `VisionTool` can become an OpenAI multimodal tool.
- `N8NTool` can become an action tool.
- `SafetyTool` can become a guardrail node before recommendations.
