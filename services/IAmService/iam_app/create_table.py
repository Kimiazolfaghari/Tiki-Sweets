from services.IAmService.iam_app.db.base import Base
from services.IAmService.iam_app.db.models import Admin, User,OTP
from services.IAmService.iam_app.db.session import engine

__all__ = [
    "User",
    "Admin",
    "OTP",
]

Base.metadata.create_all(bind=engine)