from fastapi import APIRouter, File, UploadFile

from app.api.schemas import UploadImageResponse
from app.utils.file_utils import save_upload_file

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("/image", response_model=UploadImageResponse)
async def upload_image(file: UploadFile = File(...)) -> UploadImageResponse:
    """Store an uploaded troubleshooting image locally."""
    saved_path = await save_upload_file(file=file, directory="data/uploads")
    return UploadImageResponse(
        filename=file.filename or "uploaded-image",
        saved_path=str(saved_path),
        content_type=file.content_type,
    )
