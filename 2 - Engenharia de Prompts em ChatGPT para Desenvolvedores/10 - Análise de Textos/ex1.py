from openai import OpenAI

def get_response(prompt):
    """
    Function to get a response from OpenAI API.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

ticket = "idk man shits fucked"

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to classify the ticket
prompt = f"""Classify the ticket delimited by triple backticks as technical issue, billing inquiry, or product feedback. Your response should just contain the class and nothing else.
 ```{ticket}```"""

response = get_response(prompt)

print("Ticket: ", ticket)
print("Class: ", response)

'''
O código acima é um exemplo de análise de texto usando a API do OpenAI. Ele classifica um ticket de suporte em uma das três categorias: problema técnico, consulta de cobrança ou feedback do produto.
'''