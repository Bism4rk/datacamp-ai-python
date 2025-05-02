from openai import OpenAI

# Create the OpenAI client: you can leave "<OPENAI_API_TOKEN>" as is
client = OpenAI(api_key="<OPENAI_API_TOKEN>") # OpenAI foi inserido no lugar de ____

# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": ""} 
]

'''
Aqui, os papéis foam definidos como "system", "user" e "assistant" por mim.
System - Define o papel do assistente, que é um assistente de eventos, ajudando o modelo a entender o contexto da conversa.
User - Define o papel do usuário, que é o cliente que está fazendo a pergunta. 
Assistant - Define o papel do assistente, que é o modelo de linguagem que irá responder à pergunta do usuário.
'''

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=conversation_messages
)
print(response.choices[0].message.content)

