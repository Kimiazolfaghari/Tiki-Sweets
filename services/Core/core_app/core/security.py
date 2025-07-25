from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from services.Core.core_app.core.config import settings

bearer_scheme = HTTPBearer(auto_error=True)

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")
        user_id = payload.get("id")  
        if not email or not user_id:
            raise HTTPException(status_code=401, detail="Token payload invalid")
        return {"email": email, "id": user_id, "token": token}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid")

def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials is None or credentials.scheme.lower() != "bearer":
        raise HTTPException(status_code=401, detail="Invalid or missing token")

    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        role = payload.get("role")
        Admin_id = payload.get("id")
        email = payload.get("sub")
        if role != "admin":
            raise HTTPException(status_code=403, detail="Not an admin")
        return {"email": email, "id": Admin_id, "role": role, "token": token}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token is invalid")
