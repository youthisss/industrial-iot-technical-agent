from pathlib import Path

from app.config import Settings, get_settings


class VisionService:
    """OpenAI Vision API-ready image analysis service."""

    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or get_settings()

    def analyze_image(self, image_path: str, prompt: str) -> str:
        """Return a mock visual summary for an image path."""
        path = Path(image_path)
        if not path.exists():
            return f"Image not found at {image_path}; visual analysis skipped."
        return (
            f"Mock vision summary for {path.name}: panel image received. "
            f"Prompt context: {prompt}"
        )
