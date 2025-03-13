from fastapi import APIRouter, HTTPException
from app.models.linkedin_page import LinkedInPage
from app.database import SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/linkedin-page/{page_id}")
def get_linkedin_page(page_id: str):
    db: Session = SessionLocal()
    page = db.query(LinkedInPage).filter(LinkedInPage.page_id == page_id).first()
    db.close()
    
    if page is None:
        raise HTTPException(status_code=404, detail="LinkedIn page not found")
    
    return {
        'page_id': page.page_id,
        'name': page.name,
        'url': page.url,
        'profile_picture': page.profile_picture,
        'description': page.description,
        'website': page.website,
        'industry': page.industry,
        'followers': page.followers,
        'headcount': page.headcount,
        'specialities': page.specialities,
    }
