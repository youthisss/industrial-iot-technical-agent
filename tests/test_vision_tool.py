from app.tools.vision_tool import VisionTool


class FakeVisionService:
    def analyze_image(self, image_path: str, prompt: str) -> str:
        return f"summary for {image_path}: {prompt}"


def test_vision_tool_returns_summary():
    tool = VisionTool(vision_service=FakeVisionService())

    summary = tool.analyze_image("panel.jpg", "check panel")

    assert "panel.jpg" in summary
