class VisionTool:
    def analyze(self, image_url: str) -> str:
        if not image_url:
            return ""
        return "Mock vision summary: PLC panel or HMI screenshot shows an I/O fault condition."
