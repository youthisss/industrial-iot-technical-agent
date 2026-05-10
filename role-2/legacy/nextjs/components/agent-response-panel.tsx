import type { ChatResponse } from "@/types/agent";

type AgentResponsePanelProps = {
  response: ChatResponse | null;
};

export function AgentResponsePanel({ response }: AgentResponsePanelProps) {
  if (!response) {
    return (
      <section className="panel response-panel empty-state">
        <h2>Agent Response</h2>
        <p>Submit a troubleshooting question to review recommendation, sources, and history.</p>
      </section>
    );
  }

  return (
    <section className="panel response-panel">
      <div className="panel-header">
        <h2>Agent Response</h2>
        <span className={`badge badge-${response.safety_level}`}>{response.safety_level}</span>
      </div>
      <p className="answer">{response.answer}</p>

      <div className="evidence-grid">
        <div>
          <h3>Retrieved Sources</h3>
          {response.retrieved_sources.length > 0 ? (
            <ul className="stack-list">
              {response.retrieved_sources.map((source) => (
                <li key={`${source.source}-${source.score}`}>
                  <strong>{source.source}</strong>
                  <p>{source.content}</p>
                  <span>Score: {source.score}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="muted">No manual sources found.</p>
          )}
        </div>

        <div>
          <h3>Maintenance History</h3>
          {response.maintenance_history.length > 0 ? (
            <ul className="stack-list">
              {response.maintenance_history.map((history, index) => (
                <li key={`${history.machine_id}-${history.error_code}-${index}`}>
                  <strong>{history.machine_id}</strong>
                  <p>{history.solution_applied ?? history.root_cause ?? "History record found."}</p>
                  <span>{history.success_status ? "Resolved" : "Unresolved or unknown"}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p className="muted">No prior history found.</p>
          )}
        </div>
      </div>
    </section>
  );
}
