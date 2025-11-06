from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_books_endpoint():
    response = client.get("/books")
    assert response.status_code == 200
    assert "Clean Code" in response.text
    assert "The Pragmatic Programmer" in response.text
