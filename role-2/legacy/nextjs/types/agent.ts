export type SourceDocument = {
  source: string;
  content: string;
  score: number;
};

export type MaintenanceHistory = {
  id?: number;
  machine_id: string;
  error_code: string;
  root_cause?: string;
  solution_applied?: string;
  success_status?: boolean;
  downtime_minutes?: number;
  technician_notes?: string;
  created_at?: string | null;
};

export type ChatRequest = {
  machine_id: string;
  plc_type: string;
  error_code: string;
  message: string;
  image_path?: string | null;
};

export type ChatResponse = {
  answer: string;
  machine_id: string;
  error_code: string;
  safety_level: string;
  retrieved_sources: SourceDocument[];
  maintenance_history: MaintenanceHistory[];
  incident_id?: string | null;
};

export type UploadImageResponse = {
  filename: string;
  saved_path: string;
  content_type?: string | null;
};

export type IncidentActionRequest = {
  machine_id: string;
  error_code: string;
  issue_summary: string;
  ai_recommendation: string;
};

export type IncidentActionResponse = {
  status: string;
  automation: Record<string, unknown>;
  payload: Record<string, unknown>;
};
