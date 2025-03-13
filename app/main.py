from fastapi import FastAPI
from app.routes.linkedin_routes import router as linkedin_router
from app.database import init_db

app = FastAPI()

# Initialize the database
init_db()

app.include_router(linkedin_router)
