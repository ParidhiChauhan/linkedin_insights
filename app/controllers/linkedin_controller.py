from fastapi import APIRouter, HTTPException
from app.services.scraper_service import scrape_linkedin_page
from app.models.linkedin_page import LinkedInPage
from app.database import SessionLocal

router = APIRouter()

@router.get("/linkedin/{page_id}")
def get_linkedin_page(page_id: str):
    db = SessionLocal()
    page = db.query(LinkedInPage).filter(LinkedInPage.page_id == page_id).first()
    
    if not page:
        data = scrape_linkedin_page(page_id)
        if not data:
            raise HTTPException(status_code=404, detail="Page not found")
        
        page = LinkedInPage(**data)
        db.add(page)
        db.commit()
        db.refresh(page)

    return page
