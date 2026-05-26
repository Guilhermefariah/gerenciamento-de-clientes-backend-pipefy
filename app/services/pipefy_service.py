def send_client_to_pipefy(client_data):

    mutation = f"""
    mutation {{
        createCard(input: {{
            pipe_id: 123456,
            fields_attributes: [
                {{
                    field_id: "cliente_nome",
                    field_value: "{client_data['cliente_nome']}"
                }},
                {{
                    field_id: "cliente_email",
                    field_value: "{client_data['cliente_email']}"
                }},
                {{
                    field_id: "valor_patrimonio",
                    field_value: "{client_data['valor_patrimonio']}"
                }}
            ]
        }}) {{
            card {{
                id
            }}
        }}
    }}
    """

    return {
        "message": "Mutation GraphQL simulada",
        "mutation": mutation
    }


def update_pipefy_card(
    card_id,
    priority
):

    mutation = f"""
    mutation {{
        updateCardField(input: {{
            card_id: "{card_id}",
            field_id: "priority",
            new_value: "{priority}"
        }}) {{
            card {{
                id
            }}
        }}
    }}
    """

    return {
        "message": "Update GraphQL simulado",
        "mutation": mutation
    }