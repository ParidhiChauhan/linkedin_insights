from sqlalchemy import Column, Integer, String
from app.database import Base

class LinkedInPage(Base):
    __tablename__ = 'linkedin_pages'

    id = Column(Integer, primary_key=True, index=True)
    page_id = Column(String(255), unique=True, index=True)
    name = Column(String(255))
    url = Column(String(255))
    profile_picture = Column(String(255))
    description = Column(String(1000))
    website = Column(String(255))
    industry = Column(String(255))
    followers = Column(Integer)
    headcount = Column(Integer)
    specialities = Column(String(1000))

    def __repr__(self):
        return f"<LinkedInPage(name={self.name}, page_id={self.page_id})>"
