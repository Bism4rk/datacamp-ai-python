from openai import OpenAI

# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>") # OpenAI foi inserido no lugar de ____

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create( # Aqui, create foi inserido no lugar de ____
  model="gpt-4o-mini",
  messages=[
    {"role": "user", 
     "content": "Write a polite reply accepting an AI Engineer job offer."}]
)

print(response.choices[0].message.content)

# O código acima faz uma solicitação à API da OpenAI para gerar uma resposta a uma mensagem de um usuário.
# Nesse caso, a mensagem do usuário pede uma resposta educada aceitando uma oferta de emprego como engenheiro de IA.
# A resposta gerada pela API é impressa no console.
# No caso, o arquivo gerado pelo curso gera uma API Key automaticamente, mas aqui você deve colocar a sua API Key.
