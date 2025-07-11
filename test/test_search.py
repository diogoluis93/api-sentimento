from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_term_success():
    client.post("/analyze-text", json={"text": "Testando cache local"})
    
    response = client.get("/search-term", params={"term": "cache"})
    assert response.status_code == 200
    data = response.json()
    assert "word_count" in data

def test_search_term_not_found():
    response = client.get("/search-term", params={"term": "inexistente"})
    assert response.status_code == 404
    assert response.json()["error"] == "Termo não encontrado"
