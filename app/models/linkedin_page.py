from sqlalchemy import Column, Integer, String
from app.database import Base  # Correct import

class LinkedInPage(Base):
    __tablename__ = "linkedin_pages"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
