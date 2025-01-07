from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_check_spam():
    response = client.get("/check?message=SIX chances to win CASH!")
    assert response.status_code == 200
    assert response.json() == {"resp": True}

def test_check_ham():
    response = client.get("/check?message=Hello, world, my name is Fred")
    assert response.status_code == 200
    assert response.json() == {"resp": False}