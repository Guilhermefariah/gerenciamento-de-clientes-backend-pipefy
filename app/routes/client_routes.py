from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.client import Client
from app.schemas.client import (
    ClientCreate,
    ClientResponse
)

from app.services.pipefy_service import (
    send_client_to_pipefy
)

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post(
    "/clients",
    response_model=ClientResponse
)

def create_client(
    client: ClientCreate,
    db: Session = Depends(get_db)
):

    existing_client = db.query(Client).filter(
        Client.cliente_email ==
        client.cliente_email
    ).first()

    if existing_client:

        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

    priority = (
        "prioridade_alta"
        if client.valor_patrimonio >= 200000
        else "prioridade_normal"
    )

    new_client = Client(
        cliente_nome=client.cliente_nome,
        cliente_email=client.cliente_email,
        tipo_solicitacao=client.tipo_solicitacao,
        valor_patrimonio=client.valor_patrimonio,
        priority=priority,
        status="Aguardando Análise"
    )

    db.add(new_client)

    db.commit()

    db.refresh(new_client)

    pipefy_response = send_client_to_pipefy({

        "cliente_nome":
        client.cliente_nome,

        "cliente_email":
        client.cliente_email,

        "valor_patrimonio":
        client.valor_patrimonio
    })

    print(pipefy_response)

    return new_client


@router.get(
    "/clients",
    response_model=list[ClientResponse]
)

def list_clients(
    db: Session = Depends(get_db)
):

    return db.query(Client).all()