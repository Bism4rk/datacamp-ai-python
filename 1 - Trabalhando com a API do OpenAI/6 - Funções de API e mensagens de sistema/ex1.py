from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  max_tokens=150,
  messages=[
    {"role": "system",
     "content": "You are a study planning assistant that creates plans for learning new skills."},
    {"role": "user",
     "content": "I want to learn to speak Dutch."}
  ]
)

# Extract the assistant's text response
print(response.choices[0].message.content)

# O código acima utiliza a função de sistema para optimizar a resposta do modelo GPT.
# No caso, a mensagem systema diz que o modelo deve agir como um planejador de estudos que cria planos para aprender novas habilidades, guiando a sua resposta ao prompt de "quer aprender a falar holandês"