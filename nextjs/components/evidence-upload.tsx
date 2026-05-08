"use client";

type EvidenceUploadProps = {
  file: File | null;
  onFileChange: (file: File | null) => void;
};

export function EvidenceUpload({ file, onFileChange }: EvidenceUploadProps) {
  return (
    <section className="panel">
      <div className="panel-header">
        <h2>Image Evidence</h2>
        <span className="panel-kicker">Optional</span>
      </div>
      <input
        accept="image/*"
        type="file"
        onChange={(event) => onFileChange(event.target.files?.[0] ?? null)}
      />
      <p className="muted">
        {file ? `${file.name} selected` : "Attach a PLC panel or HMI screenshot when available."}
      </p>
    </section>
  );
}
