from fastapi import APIRouter

router = APIRouter()

@router.post("/webhook")
def receive_webhook(payload: dict):

    print("Webhook recebido:")
    print(payload)

    return {
        "message": "Webhook recebido com sucesso"
    }