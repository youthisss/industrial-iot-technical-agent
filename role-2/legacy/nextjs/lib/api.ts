import type {
  ChatRequest,
  ChatResponse,
  IncidentActionRequest,
  IncidentActionResponse,
  UploadImageResponse,
} from "@/types/agent";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

async function requestJson<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    ...init,
    headers: {
      ...(init?.body instanceof FormData ? {} : { "Content-Type": "application/json" }),
      ...init?.headers,
    },
  });

  if (!response.ok) {
    const message = await response.text();
    throw new Error(message || `Request failed with status ${response.status}`);
  }

  return response.json() as Promise<T>;
}

export async function sendChat(payload: ChatRequest): Promise<ChatResponse> {
  return requestJson<ChatResponse>("/chat", {
    method: "POST",
    body: JSON.stringify(payload),
  });
}

export async function uploadImage(file: File): Promise<UploadImageResponse> {
  const formData = new FormData();
  formData.append("file", file);

  return requestJson<UploadImageResponse>("/upload/image", {
    method: "POST",
    body: formData,
  });
}

export async function sendIncidentAction(
  action: "unresolved" | "escalate",
  payload: IncidentActionRequest,
): Promise<IncidentActionResponse> {
  return requestJson<IncidentActionResponse>(`/incidents/${action}`, {
    method: "POST",
    body: JSON.stringify(payload),
  });
}
