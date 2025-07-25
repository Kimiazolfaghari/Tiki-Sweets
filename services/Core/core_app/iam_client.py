import httpx
from fastapi import HTTPException

IAM_SERVICE_URL = "http://localhost:8001"

async def get_user_profile_from_iam(user_id: int, token: str):
    url = f"{IAM_SERVICE_URL}/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found in IAM")
        else:
            raise HTTPException(status_code=500, detail="Failed to get user profile from IAM")


async def get_admin_profile_from_iam(admin_id: int, token: str):
    url = f"{IAM_SERVICE_URL}/admins/{admin_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="User not found in IAM")
        else:
            raise HTTPException(status_code=500, detail="Failed to get user profile from IAM")
