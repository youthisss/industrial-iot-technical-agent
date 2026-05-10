import logging
from typing import Any

import requests

logger = logging.getLogger(__name__)


class N8NTool:
    """Send incident payloads to an n8n webhook."""

    def __init__(self, webhook_url: str = "", timeout_seconds: int = 10) -> None:
        self.webhook_url = webhook_url
        self.timeout_seconds = timeout_seconds

    def send_payload(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Send a payload to n8n or return a dry-run response when not configured."""
        if not self.webhook_url:
            return {"sent": False, "mode": "dry_run", "payload": payload}

        try:
            response = requests.post(
                self.webhook_url,
                json=payload,
                timeout=self.timeout_seconds,
            )
            response.raise_for_status()
            return {
                "sent": True,
                "status_code": response.status_code,
                "response": self._safe_json(response),
            }
        except requests.RequestException as exc:
            logger.warning("Failed to send n8n payload: %s", exc)
            return {"sent": False, "error": str(exc), "payload": payload}

    @staticmethod
    def _safe_json(response: requests.Response) -> dict[str, Any] | str:
        try:
            return response.json()
        except ValueError:
            return response.text
