# Next.js Frontend

Minimal operator dashboard for the PLC Troubleshooting Agent API.

## Setup

```bash
npm install
Copy-Item .env.example .env.local
npm run dev
```

Open `http://localhost:3000`.

The app calls the FastAPI backend through `NEXT_PUBLIC_API_URL`, defaulting to `http://localhost:8000`.

## Included Flows

- Submit machine context and technician question to `POST /chat`.
- Upload optional image evidence through `POST /upload/image`.
- Mark unresolved issues through `POST /incidents/unresolved`.
- Escalate issues through `POST /incidents/escalate`.
