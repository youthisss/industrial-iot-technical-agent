"use client";

import type { IncidentActionResponse } from "@/types/agent";

type IncidentControlsProps = {
  disabled: boolean;
  loadingAction: "unresolved" | "escalate" | null;
  result: IncidentActionResponse | null;
  onAction: (action: "unresolved" | "escalate") => void;
};

export function IncidentControls({
  disabled,
  loadingAction,
  result,
  onAction,
}: IncidentControlsProps) {
  return (
    <section className="panel incident-panel">
      <div className="panel-header">
        <h2>Incident Automation</h2>
        <span className="panel-kicker">n8n ready</span>
      </div>
      <div className="button-row">
        <button disabled={disabled || loadingAction !== null} onClick={() => onAction("unresolved")}>
          {loadingAction === "unresolved" ? "Logging..." : "Issue Not Resolved"}
        </button>
        <button disabled={disabled || loadingAction !== null} onClick={() => onAction("escalate")}>
          {loadingAction === "escalate" ? "Escalating..." : "Escalate"}
        </button>
      </div>
      {result ? (
        <pre className="json-output">{JSON.stringify(result, null, 2)}</pre>
      ) : (
        <p className="muted">Ask the agent first, then log or escalate the issue.</p>
      )}
    </section>
  );
}
