from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt="""Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}], # content e prompt foram inseridos no lugar de ____
  max_completion_tokens = 100 # Número de tokens de resposta, pode ser ajustado conforme necessário
)

# Extract and print the response text
print(response.choices[0].message.content) # message e content foram inseridos no lugar de ____]

# O código acima faz uma solicitação à API da OpenAI para gerar uma resposta a uma mensagem de um usuário.
# Nesse caso, a mensagem do usuário pede para substituir a palavra "car" por "plane" e ajustar a frase.
# A resposta gerada pela API é impressa no console.
