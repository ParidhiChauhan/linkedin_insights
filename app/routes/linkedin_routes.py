from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.scraper_service import scrape_linkedin_page
from app.models.linkedin_page import LinkedInPage

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/linkedin/{page_id}")
def get_linkedin_page(page_id: int, db: Session = Depends(get_db)):
    # Check if page exists in DB
    page = db.query(LinkedInPage).filter(LinkedInPage.id == page_id).first()  # FIXED: Use 'id' instead of 'page_id'
    
    if page:
        return page  # Return stored data

    # If not in DB, scrape and store
    scraped_data = scrape_linkedin_page(page_id)
    
    if not scraped_data:
        raise HTTPException(status_code=404, detail="Page not found")

    # Save scraped data to DB
    new_page = LinkedInPage(
        id=page_id,  # Ensure ID is correctly assigned
        name=scraped_data.get("name", "Unknown")  # Ensure safe assignment
    )
    
    db.add(new_page)
    db.commit()
    db.refresh(new_page)
    
    return new_page
