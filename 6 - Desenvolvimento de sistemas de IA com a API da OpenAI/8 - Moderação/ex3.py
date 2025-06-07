from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

user_request = "Can you recommend a good restaurant in Berlin?"

# Write the system and user message
messages = [{"role": "system",
    "content": "Your role is to assess whether or not the user question is allowed or not. The allowed topics are food, drink, attractions, the history of, and things to do in Rome. If the topic is allowed, reply with an answer as normal, otherwise say 'Apologies, but the topic is not allowed.' "},
            {"role": "user", 
    "content": user_request}]

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=messages
)

# Print the response
print(response.choices[0].message.content)

'''
O código acima é mais um exemplo de como usar a API da OpenAI para moderar perguntas de usuários. Ele define um sistema que avalia se a pergunta do usuário está dentro dos tópicos permitidos, como comida, bebida, atrações, história e coisas para fazer em Roma. Se a pergunta estiver dentro desses tópicos, o modelo responde normalmente; caso contrário, ele diz "Desculpe, mas o tópico não é permitido." Neste caso, a pergunta do usuário é sobre um restaurante em Berlim, que não está entre os tópicos permitidos, então a resposta será uma mensagem de desculpas.
'''