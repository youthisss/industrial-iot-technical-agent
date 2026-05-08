"use client";

type TroubleshootingFormProps = {
  message: string;
  loading: boolean;
  onMessageChange: (value: string) => void;
  onSubmit: () => void;
};

export function TroubleshootingForm({
  message,
  loading,
  onMessageChange,
  onSubmit,
}: TroubleshootingFormProps) {
  return (
    <section className="panel workspace-panel">
      <div className="panel-header">
        <h2>Technician Question</h2>
        <span className="panel-kicker">Agent input</span>
      </div>
      <textarea
        value={message}
        onChange={(event) => onMessageChange(event.target.value)}
        placeholder="Example: Machine stopped after emergency stop reset. What should I check first?"
      />
      <button className="primary-button" disabled={loading || !message.trim()} onClick={onSubmit}>
        {loading ? "Analyzing..." : "Ask Agent"}
      </button>
    </section>
  );
}
