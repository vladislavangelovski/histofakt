from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "HistoFakt API up!"}


def test_ask_endpoint():
    payload = {"query": "Who was Einstein?", "language": "en"}
    r = client.post("/ask", json=payload)
    assert r.status_code == 200

    data = r.json()
    assert data["answer"] == "Hello World"
    assert isinstance(data["sources"], list)
    assert data["mode"] == "local-stub"
