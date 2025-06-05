from openai import OpenAI  

messages = ['idk brother this is an example of a message']

def get_response(messages, function_definition):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=function_definition,
        function_call={'name': 'extract_review_info'}
    )
    return response.choices[0].message

function_definition = ['god knows bro this is just an example of a function definition inserted so that no errors are flagged']

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Modify the messages
messages.append({'role': 'system', 'content': "Don't make assumptions about what values to plug into answers"})

response = get_response(messages, function_definition)

print(response)

'''
O código acima mostra como mensagens do sistema podem ser modificadas para alterar o comportamento do modelo. Neste caso, a mensagem do sistema foi alterada para instruir o modelo a não fazer suposições sobre os valores a serem usados nas respostas. Isso pode ser útil para garantir que o modelo responda de maneira mais precisa e relevante às perguntas feitas.
'''