from pydantic import BaseModel

class ClientCreate(BaseModel):
    name: str
    email: str
    patrimonio: float


class ClientResponse(ClientCreate):
    id: int

    class Config:
        from_attributes = True