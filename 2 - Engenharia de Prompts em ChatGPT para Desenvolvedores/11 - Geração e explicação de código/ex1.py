from openai import OpenAI

def get_response(prompt):
    print(prompt)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that asks the model for the function
prompt = "Write a Python function that accepts a list of 12 floats representing monthly sales, and outputs the month with the highest sales."

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de geração de código usando a API do OpenAI. Ele solicita ao modelo que escreva uma função Python que aceita uma lista de 12 floats representando vendas mensais e retorna o mês com as vendas mais altas.
'''