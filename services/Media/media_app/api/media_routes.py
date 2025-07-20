from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STORAGE_DIR = os.path.join(BASE_DIR, "storage")

def save_upload_file(upload_file: UploadFile) -> str:
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    filename = upload_file.filename
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
async def upload_file(file: UploadFile = File(...)):
    try:
        filename = save_upload_file(file)  # چون تابع sync است نیازی به await نیست
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not save file: {str(e)}")
    return {"filename": filename, "message": "File uploaded successfully."}


@router.get("/download/{filename}")
def download_file(filename: str):
    path = get_file_path(filename)
    if not os.path.exists(path) or not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path, filename=filename)


@router.delete("/delete/{filename}")
def remove_file(filename: str):
    try:
        deleted = delete_file(filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting file: {str(e)}")
    if deleted:
        return {"message": "File deleted successfully."}
    raise HTTPException(status_code=404, detail="File not found")
