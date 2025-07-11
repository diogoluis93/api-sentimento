from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_analyze_text_success():
    response = client.post("/analyze-text", json={"text": "Hoje o dia está ótimo"})
    assert response.status_code == 200
    data = response.json()
    assert "word_count" in data
    assert "top_words" in data
    assert "sentiment" in data
    assert data["word_count"] > 0

def test_analyze_text_invalid_type():
    response = client.post("/analyze-text", json={"text": 123})
    assert response.status_code == 422
    assert "error" in response.json()
