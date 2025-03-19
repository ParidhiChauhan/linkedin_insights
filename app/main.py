from fastapi import FastAPI
from app.routes import linkedin_routes

app = FastAPI()

# Include Routes
app.include_router(linkedin_routes.router)
