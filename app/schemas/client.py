from pydantic import BaseModel, EmailStr


class ClientCreate(BaseModel):
    cliente_nome: str
    cliente_email: EmailStr
    tipo_solicitacao: str
    valor_patrimonio: float


class ClientResponse(ClientCreate):
    id: int
    priority: str
    status: str

    class Config:
        from_attributes = True