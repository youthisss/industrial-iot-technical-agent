from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


async def save_upload_file(file: UploadFile, directory: str | Path) -> Path:
    """Save an uploaded file to a local directory with a unique name."""
    target_dir = Path(directory)
    target_dir.mkdir(parents=True, exist_ok=True)
    suffix = Path(file.filename or "").suffix
    target_path = target_dir / f"{uuid4().hex}{suffix}"
    content = await file.read()
    target_path.write_bytes(content)
    return target_path
