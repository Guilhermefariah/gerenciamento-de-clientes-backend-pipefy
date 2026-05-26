# Client Management & Pipefy Integration API
Backend API desenvolvida com FastAPI para gerenciamento de clientes e simulação de integração GraphQL com Pipefy.

---

# Tecnologias Utilizadas
- Python 3.14
- FastAPI
- SQLite
- SQLAlchemy
- Pytest
- Pydantic
- Uvicorn

---

# Objetivo do Projeto
A API foi desenvolvida para:
- Gerenciar clientes
- Persistir dados localmente com SQLite
- Simular integração GraphQL com Pipefy
- Processar webhooks
- Aplicar regras de negócio
- Validar duplicidade de eventos
- Executar testes automatizados

---

## Funcionalidades
## Fluxo 1 — Criação de Cliente
Endpoint:
```
POST /clients
```

### Payload
```
{
    "cliente_nome": "João Silva",
    "cliente_email": "joao@email.com",
    "tipo_solicitacao": "Atualização cadastral",
    "valor_patrimonio": 250000
}
```
## Funcionalidades
- Validação de e-mail
- Verificação de e-mail duplicado
- Persistência SQLite
- Status inicial:

```
Aguardando Análise
```
ou
```
prioridade_normal
```
- Simulação da mutation GraphQL `createCard`

---

## Fluxo 2 — Webhook Pipefy
Endpoint:
```
POST /webhooks/pipefy/card-updated
```
### Payload
```
{
  "event_id": "evt_123",
  "card_id": "card_456",
  "cliente_email": "joao@email.com",
  "timestamp": "2026-05-18T12:00:00Z"
}
```
## Funcionalidades
- Controle de idempotência
- Bloqueio de eventos duplicados
- Busca de cliente por e-mail
- Regra de prioridade baseada no patrimônio
- Atualização do status do cliente
- Simulação da mutation GraphQL `updateCardField`

---

# Regras de Negócio

### Prioridade Alta
`valor_patrimonio ≥ 200000`

### Prioridade Normal
`valor_patrimonio < 200000`

---

# Como Executar o Projeto

### 1. Clonar o repositório
```
git clone https://github.com/Guilhermefariah/gerenciamento-de-clientes-backend-pipefy.git 
```

---

### 2. Criar ambiente virtual
```
python -m venv venv
```

---

### 3. Ativar ambiente virtual
```
venv\Scripts\activate
```
---

### 4. Instalar dependências
```
pip install -r requirements.txt
```

---

### 5. Executar aplicação
```
uvicorn app.main:app --reload
```

---

# Swagger
Após iniciar o projeto:
```
http://127.0.0.1:8000/docs
```

---

# Testes Automatizados
O projeto possui testes para:
- Criação de cliente
- Regra de prioridade
- Processamento webhook
- Idempotência de eventos

---

# Banco de Dados
Banco utilizado:
```
SQLite
```