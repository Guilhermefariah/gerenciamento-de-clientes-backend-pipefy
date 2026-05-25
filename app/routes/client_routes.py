from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientResponse
from app.services.pipefy_service import send_client_to_pipefy

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/clients", response_model=ClientResponse)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):

    # Verifica se email já existe
    existing_client = db.query(Client).filter(
        Client.email == client.email
    ).first()

    if existing_client:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

    # Cria novo cliente
    new_client = Client(
        name=client.name,
        email=client.email,
        patrimonio=client.patrimonio
    )

    db.add(new_client)
    db.commit()
    db.refresh(new_client)

    # Simulação integração Pipefy GraphQL
    pipefy_response = send_client_to_pipefy({
        "name": client.name,
        "email": client.email
    })

    print(pipefy_response)

    return new_client


@router.get("/clients", response_model=list[ClientResponse])
def list_clients(db: Session = Depends(get_db)):
    return db.query(Client).all()