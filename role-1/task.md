# Role 1 Task Tracker

Source of truth: `../plan.md` and `../role.md`.

Scope: Role 1 only. Do not add services, public endpoints, workflows, UI pages, database tables, or required environment variables outside the final plan.

## Current Audit Status

Role 1 currently has the required folder skeleton, API route stubs, schema files, LangGraph node contract, and evaluation scaffold. It is not yet functionally complete because retrieval adapters, vision analysis, tool behavior, and evaluation flows are mostly placeholder implementations.

## Execution Order

Follow this order strictly:

1. Milestone 2 - AI Agent and RAG.
2. Milestone 6 - Model Evaluation Dashboard.
3. Role 1 mandatory tests.
4. Milestone 7 - Final demo readiness.

## Milestone 2 - AI Agent and RAG

- [ ] Implement `POST /agent/troubleshoot` behavior to match the approved request and response contract.
- [ ] Implement `POST /agent/unresolved` behavior to match the approved request and response contract.
- [ ] Keep LangGraph nodes restricted to the 9 approved nodes.
- [ ] Keep LangGraph edges restricted to the approved edge list.
- [ ] Implement document retrieval through the retriever interface only.
- [ ] Implement Pinecone retriever adapter behavior beyond placeholder responses.
- [ ] Implement pgvector retriever adapter behavior beyond placeholder responses.
- [ ] Implement ingestion flow: load, chunk, embed, and index technical documents.
- [ ] Implement GPT Vision analysis behavior for image-assisted troubleshooting.
- [ ] Implement safety checker behavior to enforce safety warnings and response gating.
- [ ] Ensure unresolved flow consumes maintenance history input from Role 2 without direct database writes.
- [ ] Ensure Role 1 does not directly write to PostgreSQL, Redis, n8n, or Next.js.
- [ ] Keep response payloads structured and deterministic for Role 2 API consumption.

Acceptance target:

```text
The AI service receives troubleshooting context, retrieves relevant documents, applies reasoning and safety checks, and returns structured recommendations for initial and unresolved flows.
```

## Milestone 6 - Model Evaluation Dashboard

- [ ] Implement LangSmith tracing for Role 1 runs.
- [ ] Implement evaluation dataset usage from `app/evaluation/datasets`.
- [ ] Implement evaluation runner beyond placeholder metric values.
- [ ] Implement Ragas-based offline RAG evaluation path.
- [ ] Track only the 10 approved metrics from the plan.
- [ ] Document evaluation execution and interpretation in Role 1 docs.
- [ ] Ensure evaluation logging integrates with Role 1 response lifecycle.

Acceptance target:

```text
The model evaluation dashboard shows retrieval quality, groundedness, correctness, safety compliance, latency, and tool-call success for Role 1 agent runs.
```

## Mandatory Role 1 Tests

- [ ] RAG retrieval tests.
- [ ] pgvector adapter tests.
- [ ] Pinecone adapter tests.
- [ ] LangGraph node transition tests.
- [ ] Vision analysis mock tests.
- [ ] Safety checker tests.
- [ ] Agent response schema tests.
- [ ] Evaluation metrics script tests.

## Milestone 7 - Final Demo Readiness

- [ ] Validate Role 1 health endpoint.
- [ ] Validate initial troubleshooting flow for `PACK-LINE-03` and `OB82`.
- [ ] Validate unresolved troubleshooting flow using maintenance history payload from Role 2.
- [ ] Validate image-assisted troubleshooting flow.
- [ ] Validate retrieved sources are included in response contracts.
- [ ] Validate safety warnings are always present in recommendations.
- [ ] Validate evaluation traces are emitted for demo flow.
- [ ] Confirm no out-of-scope Role 1 additions exist.

## Known Blockers From Audit

- [ ] Retriever adapters currently return hardcoded placeholder snippets.
- [ ] Vision tool currently returns a static mock summary.
- [ ] Graph recommendation logic is currently static and non-contextual.
- [ ] Safety tool behavior needs strict rule-based enforcement checks.
- [ ] History lookup tool does not yet enforce robust integration behavior with Role 2 contracts.
- [ ] Evaluation runner currently executes placeholder metrics only.
- [ ] Role 1 tests are currently minimal and do not cover all mandatory scenarios.
- [ ] `role-1/legacy` is outside the current Role 1 deliverable path and must be removed, archived outside final scope, or explicitly excluded from final delivery.

## Validation Commands

Use service-local virtual environment and run tests from `role-1/services/ai-agent-service`:

```powershell
Set-Location role-1/services/ai-agent-service
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
```

If `python` is not available on this machine, use `py` launcher:

```powershell
Set-Location role-1/services/ai-agent-service
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py -m pytest
```
