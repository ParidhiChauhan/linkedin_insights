from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
import datetime

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    linkedin_page_id = Column(Integer, ForeignKey("linkedin_pages.id", ondelete="CASCADE"), nullable=False)
    content = Column(String(1000), nullable=False)
    likes = Column(Integer, default=0)
    comments_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    page = relationship("LinkedInPage", back_populates="posts")
