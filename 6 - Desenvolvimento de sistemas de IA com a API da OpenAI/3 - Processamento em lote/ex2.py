from openai import OpenAI

measurements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_response(messages):
    # Use the OpenAI client to get a response from the chat completion endpoint
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = []
# Provide a system message and user messages to send the batch
messages.append({
    "role": "system",
    "content": """You are given a series of measurements in kilometers and are     asked to return a table with these measurements converted to miles.
    """})
# Append measurements to the message
[messages.append({"role": "user", "content": str(i)}) for i in measurements]

response = get_response(messages)

print(response)

'''
O código acima é um exemplo de processamento em lote usando a API da OpenAI. Ele envia uma série de medições em quilômetros como mensagens para o modelo GPT-4o-mini, que é solicitado a retornar uma tabela com essas medições convertidas para milhas. As mensagens são organizadas em uma lista, começando com uma mensagem de sistema que define o contexto, seguida por mensagens de usuário contendo as medições. A função `get_response` é chamada para obter a resposta do modelo, que é então impressa.
'''
