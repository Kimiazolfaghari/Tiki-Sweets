from core_app.db.base import Base
from media_app.db.models import Media
from core_app.db.session import engine

__all__ = [
   "Media"
]

Base.metadata.create_all(bind=engine)