from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_create_client():

    response = client.post(
        "/clients",
        json={
            "name": "Guilherme",
            "email": "guilherme@gmail.com",
            "patrimonio": 5000
        }
    )

    assert response.status_code == 200