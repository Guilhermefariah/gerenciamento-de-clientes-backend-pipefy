def send_client_to_pipefy(client_data):

    mutation = f"""
    mutation {{
        createCard(input: {{
            pipe_id: 123456,
            fields_attributes: [
                {{
                    field_id: "nome",
                    field_value: "{client_data['name']}"
                }},
                {{
                    field_id: "email",
                    field_value: "{client_data['email']}"
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