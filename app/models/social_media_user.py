from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class SocialMediaUser(Base):
    __tablename__ = 'social_media_users'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(100), unique=True)
    name = Column(String(255))
    profile_url = Column(String(255))
    page_id = Column(Integer, ForeignKey('linkedin_pages.id'))

    page = relationship('LinkedInPage', back_populates='users')
