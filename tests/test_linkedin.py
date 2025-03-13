import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_linkedin_page():
    response = client.get("/linkedin/deepsolv")
    assert response.status_code == 200
    assert "name" in response.json()
