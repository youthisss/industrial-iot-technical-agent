"use client";

type MachineContextFormProps = {
  machineId: string;
  plcType: string;
  errorCode: string;
  onMachineIdChange: (value: string) => void;
  onPlcTypeChange: (value: string) => void;
  onErrorCodeChange: (value: string) => void;
};

export function MachineContextForm({
  machineId,
  plcType,
  errorCode,
  onMachineIdChange,
  onPlcTypeChange,
  onErrorCodeChange,
}: MachineContextFormProps) {
  return (
    <section className="panel">
      <div className="panel-header">
        <h2>Machine Context</h2>
        <span className="panel-kicker">PLC profile</span>
      </div>
      <label>
        Machine ID
        <input value={machineId} onChange={(event) => onMachineIdChange(event.target.value)} />
      </label>
      <label>
        PLC Type
        <input value={plcType} onChange={(event) => onPlcTypeChange(event.target.value)} />
      </label>
      <label>
        Error Code
        <input value={errorCode} onChange={(event) => onErrorCodeChange(event.target.value)} />
      </label>
    </section>
  );
}
