from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.linkedin_page import LinkedInPage
from app.services.scraper_service import ScraperService

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()  # Creates a new session
    try:
        yield db  # Provides the session to the route handler
    finally:
        db.close()  # Closes the session when done

# Example endpoint to scrape and store LinkedIn page details
@router.get("/linkedin/{page_id}")
async def get_linkedin_page_details(page_id: str, db: Session = Depends(get_db)):
    scraper_service = ScraperService()
    page_details = scraper_service.scrape_page(page_id)
    
    # Save the data to the database
    linkedin_page = LinkedInPage(**page_details)
    db.add(linkedin_page)
    db.commit()  # Commit the transaction
    db.refresh(linkedin_page)  # Refresh the instance to get any auto-generated fields
    
    return {"message": "LinkedIn page details fetched and stored."}
