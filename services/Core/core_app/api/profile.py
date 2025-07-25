from fastapi import APIRouter, Depends,HTTPException
from services.Core.core_app.core.security import get_current_user,get_current_admin
from services.Core.core_app.iam_client import get_user_profile_from_iam, get_admin_profile_from_iam

profile_router = APIRouter()

@profile_router.get("/me")
async def read_own_profile(current_user: dict = Depends(get_current_user)):
    user_id = current_user["id"]
    token = current_user["token"]
    profile = await get_user_profile_from_iam(user_id=user_id, token=token)
    return profile

@profile_router.get("/meAdmin")
async def read_own_profile(current_admin: dict = Depends(get_current_admin)):
    admin_id = current_admin.get("id")
    token = current_admin.get("token")

    print(f"admin_id: {admin_id}, type: {type(admin_id)}")

    if admin_id is None:
        raise HTTPException(status_code=400, detail="admin_id is None in token payload")
    if not isinstance(admin_id, int):
        try:
            admin_id = int(admin_id)
        except ValueError:
            raise HTTPException(status_code=400, detail="admin_id in token is not a valid integer")

    profile = await get_admin_profile_from_iam(admin_id=admin_id, token=token)
    return profile
