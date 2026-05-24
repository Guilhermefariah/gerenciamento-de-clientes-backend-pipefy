from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Banco fake em memória
clients = []

# Model do cliente
class Client(BaseModel):
    id: int
    name: str
    email: str
    patrimonio: float


@app.get("/")
def home():
    return {"message": "API funcionando"}


# Listar clientes
@app.get("/clients")
def get_clients():
    return clients


# Criar cliente
@app.post("/clients")
def create_client(client: Client):
    clients.append(client)
    return {
        "message": "Cliente criado com sucesso",
        "client": client
    }