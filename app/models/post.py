from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(String(100), unique=True)
    content = Column(Text)
    likes_count = Column(Integer)
    comments_count = Column(Integer)
    page_id = Column(Integer, ForeignKey('linkedin_pages.id'))

    page = relationship('LinkedInPage', back_populates='posts')
