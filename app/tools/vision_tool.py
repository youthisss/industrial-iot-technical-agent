from app.services.vision_service import VisionService


class VisionTool:
    """Analyze image evidence with a vision service."""

    def __init__(self, vision_service: VisionService) -> None:
        self.vision_service = vision_service

    def analyze_image(self, image_path: str, prompt: str) -> str:
        """Return a visual summary for an uploaded image."""
        return self.vision_service.analyze_image(image_path=image_path, prompt=prompt)
