from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)

from sqlalchemy.orm import Session

from app.database import SessionLocal

from app.models.client import Client

from app.services.pipefy_service import (
    update_pipefy_card
)

router = APIRouter()

processed_events = set()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post(
    "/webhooks/pipefy/card-updated"
)

def receive_webhook(
    payload: dict,
    db: Session = Depends(get_db)
):

    event_id = payload["event_id"]

    if event_id in processed_events:

        raise HTTPException(
            status_code=400,
            detail="Evento já processado"
        )

    processed_events.add(event_id)

    client = db.query(Client).filter(
        Client.cliente_email ==
        payload["cliente_email"]
    ).first()

    if not client:

        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )

    priority = (
        "prioridade_alta"
        if client.valor_patrimonio >= 200000
        else "prioridade_normal"
    )

    client.priority = priority

    client.status = "Processado"

    db.commit()

    graphql_response = update_pipefy_card(
        payload["card_id"],
        priority
    )

    print(graphql_response)

    return {
        "message": "Webhook processado",
        "priority": priority
    }