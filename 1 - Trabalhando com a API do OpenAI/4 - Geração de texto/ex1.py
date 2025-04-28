from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": "Please create an attractive slogan for a new Italian restaurant called 'Bella', which seeks to attract customers with a homely charm and hearty and authentically Italian meals."}], # Aqui o conteúdo foi inserido no lugar de ____ 
)

print(response.choices[0].message.content)

# O código acima faz uma solicitação à API da OpenAI para gerar um slogan atraente para um novo restaurante italiano chamado "Bella".
# A resposta gerada pela API é impressa no console.
# O slogan deve refletir o charme caseiro e as refeições italianas autênticas que o restaurante oferece.
