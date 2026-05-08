"use client";

import { useState } from "react";
import { AgentResponsePanel } from "@/components/agent-response-panel";
import { EvidenceUpload } from "@/components/evidence-upload";
import { IncidentControls } from "@/components/incident-controls";
import { MachineContextForm } from "@/components/machine-context-form";
import { TroubleshootingForm } from "@/components/troubleshooting-form";
import { sendChat, sendIncidentAction, uploadImage } from "@/lib/api";
import type { ChatResponse, IncidentActionResponse } from "@/types/agent";

export default function Home() {
  const [machineId, setMachineId] = useState("PLC-001");
  const [plcType, setPlcType] = useState("Siemens S7-1200");
  const [errorCode, setErrorCode] = useState("E-STOP");
  const [message, setMessage] = useState("Machine stopped after emergency stop reset.");
  const [file, setFile] = useState<File | null>(null);
  const [response, setResponse] = useState<ChatResponse | null>(null);
  const [incidentResult, setIncidentResult] = useState<IncidentActionResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [loadingAction, setLoadingAction] = useState<"unresolved" | "escalate" | null>(null);
  const [error, setError] = useState<string | null>(null);

  async function handleSubmit() {
    setLoading(true);
    setError(null);
    setIncidentResult(null);

    try {
      const uploaded = file ? await uploadImage(file) : null;
      const result = await sendChat({
        machine_id: machineId,
        plc_type: plcType,
        error_code: errorCode,
        message,
        image_path: uploaded?.saved_path ?? null,
      });
      setResponse(result);
    } catch (requestError) {
      setError(requestError instanceof Error ? requestError.message : "Failed to contact API.");
    } finally {
      setLoading(false);
    }
  }

  async function handleIncidentAction(action: "unresolved" | "escalate") {
    if (!response) {
      return;
    }

    setLoadingAction(action);
    setError(null);

    try {
      const result = await sendIncidentAction(action, {
        machine_id: machineId,
        error_code: errorCode,
        issue_summary: message || "Troubleshooting issue remains unresolved.",
        ai_recommendation: response.answer,
      });
      setIncidentResult(result);
    } catch (requestError) {
      setError(requestError instanceof Error ? requestError.message : "Failed to send incident action.");
    } finally {
      setLoadingAction(null);
    }
  }

  return (
    <main>
      <header className="app-header">
        <div>
          <p className="eyebrow">Industrial IoT Maintenance</p>
          <h1>PLC Troubleshooting Agent</h1>
          <p>
            Field-ready interface for RAG-assisted troubleshooting, maintenance history lookup,
            image evidence, and n8n escalation.
          </p>
        </div>
      </header>

      {error ? <div className="error-banner">{error}</div> : null}

      <div className="layout-grid">
        <aside className="sidebar">
          <MachineContextForm
            machineId={machineId}
            plcType={plcType}
            errorCode={errorCode}
            onMachineIdChange={setMachineId}
            onPlcTypeChange={setPlcType}
            onErrorCodeChange={setErrorCode}
          />
          <EvidenceUpload file={file} onFileChange={setFile} />
        </aside>

        <section className="workspace">
          <TroubleshootingForm
            message={message}
            loading={loading}
            onMessageChange={setMessage}
            onSubmit={handleSubmit}
          />
          <AgentResponsePanel response={response} />
          <IncidentControls
            disabled={!response}
            loadingAction={loadingAction}
            result={incidentResult}
            onAction={handleIncidentAction}
          />
        </section>
      </div>
    </main>
  );
}
