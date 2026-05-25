from fastapi import FastAPI

from app.database import engine, Base
from app.routes.client_routes import router as client_router
from app.webhook.webhook import router as webhook_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Client Management API",
    version="1.0.0"
)

app.include_router(client_router)
app.include_router(webhook_router)

@app.get("/")
def home():
    return {
        "message": "API funcionando"
    }