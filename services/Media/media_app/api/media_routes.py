from uuid import uuid4
from fastapi.responses import FileResponse
import os
from fastapi import UploadFile, File, HTTPException, APIRouter, Depends
from sqlalchemy.orm import Session
from iam_app.core.dependencies import get_current_active_user_or_admin
from iam_app.db.models import MediaFile, User
from iam_app.db.session import SessionLocal

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".mp4", ".mov"}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORAGE_DIR = os.path.join(BASE_DIR, "storage")


async def validate_file(file: UploadFile):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File type not allowed.")

    contents = await file.read()
    await file.seek(0)

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large.")


def save_upload_file(upload_file: UploadFile) -> str:
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    ext = os.path.splitext(upload_file.filename)[1].lower()
    filename = f"{uuid4()}{ext}"
    file_path = os.path.join(STORAGE_DIR, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())
    return filename


def get_file_path(filename: str) -> str:
    return os.path.join(STORAGE_DIR, filename)


def delete_file(filename: str) -> bool:
    path = get_file_path(filename)
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
        return True
    return False


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user_or_admin),
):
    contents = await file.read()

    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File type not allowed.")

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large.")

    # دریافت user از دیتابیس با ایمیل توکن
    uploader_email = current_user.get("sub")
    if not uploader_email:
        raise HTTPException(status_code=401, detail="Invalid token: missing user email")

    user = db.query(User).filter(User.email == uploader_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    filename = f"{uuid4()}{ext}"
    file_path = os.path.join(STORAGE_DIR, filename)
    with open(file_path, "wb") as buffer:
        buffer.write(contents)

    media = MediaFile(
        id=uuid4(),
        filename=filename,
        original_filename=file.filename,
        size=len(contents),
        content_type=file.content_type,
        uploader_id=user.id,
    )
    db.add(media)
    db.commit()
    db.refresh(media)

    return {"file_id": str(media.id), "filename": filename, "message": "File uploaded successfully."}


@router.get("/download/{file_id}")
def download_file(
    file_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user_or_admin),
):
    media = db.query(MediaFile).filter_by(id=file_id).first()
    if not media:
        raise HTTPException(status_code=404, detail="File not found")

    uploader_email = current_user.get("sub")
    if not uploader_email:
        raise HTTPException(status_code=401, detail="Invalid token: missing user email")

    user = db.query(User).filter(User.email == uploader_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.id != media.uploader_id and current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to access this file")

    path = get_file_path(media.filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Physical file not found")

    return FileResponse(path, filename=media.filename)


@router.delete("/delete/{file_id}")
def remove_file(
    file_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_active_user_or_admin),
):
    media = db.query(MediaFile).filter_by(id=file_id).first()
    if not media:
        raise HTTPException(status_code=404, detail="File not found")

    uploader_email = current_user.get("sub")
    if not uploader_email:
        raise HTTPException(status_code=401, detail="Invalid token: missing user email")

    user = db.query(User).filter(User.email == uploader_email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.id != media.uploader_id and current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Not authorized to delete this file")

    try:
        deleted = delete_file(media.filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting file: {str(e)}")

    db.delete(media)
    db.commit()

    return {"message": "File deleted successfully."}
