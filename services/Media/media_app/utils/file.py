import os
import shutil
import uuid

UPLOAD_DIR = "storage"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_file(file):
    ext = os.path.splitext(file.filename)[1]
    unique_name = f"{uuid.uuid4()}{ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return unique_name

def get_file_path(filename):
    return os.path.join(UPLOAD_DIR, filename)

def delete_file(filename):
    path = get_file_path(filename)
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
