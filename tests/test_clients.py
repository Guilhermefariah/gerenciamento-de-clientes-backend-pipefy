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
            "cliente_nome": "Guilherme",
            "cliente_email": "guilherme@gmail.com",
            "tipo_solicitacao": "Atualização cadastral",
            "valor_patrimonio": 250000
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["priority"] == "prioridade_alta"

    assert data["status"] == "Aguardando Análise"


def test_webhook_processing():

    response = client.post(
        "/webhooks/pipefy/card-updated",
        json={
            "event_id": "evt_123",
            "card_id": "card_456",
            "cliente_email": "guilherme@gmail.com",
            "timestamp": "2026-05-18T12:00:00Z"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["priority"] == "prioridade_alta"


def test_duplicate_webhook():

    client.post(
        "/webhooks/pipefy/card-updated",
        json={
            "event_id": "evt_duplicate",
            "card_id": "card_456",
            "cliente_email": "guilherme@gmail.com",
            "timestamp": "2026-05-18T12:00:00Z"
        }
    )

    response = client.post(
        "/webhooks/pipefy/card-updated",
        json={
            "event_id": "evt_duplicate",
            "card_id": "card_456",
            "cliente_email": "guilherme@gmail.com",
            "timestamp": "2026-05-18T12:00:00Z"
        }
    )

    assert response.status_code == 400