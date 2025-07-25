from motor.motor_asyncio import AsyncIOMotorClient
from media_app.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)
db = client[settings.MONGO_DB_NAME]
media_collection = db["media"]
fs = db.gridfs_bucket
