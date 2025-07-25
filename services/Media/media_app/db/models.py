from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from media_app.db.base import Base

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    filetype = Column(String)
    uploader_id = Column(Integer)
    upload_date = Column(DateTime, default=datetime.utcnow)
    related_type = Column(String)
    related_id = Column(Integer)
