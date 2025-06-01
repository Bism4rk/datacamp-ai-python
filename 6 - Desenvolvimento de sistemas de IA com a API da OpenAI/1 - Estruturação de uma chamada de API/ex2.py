from openai import OpenAI

# Create the OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the request
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
   {"role": "user", "content": "I have these notes with book titles and authors: New releases this week! The Beholders by Hester Musson, The Mystery Guest by Nita Prose. Please organize the titles and authors in a json file."}
  ],
  # Specify the response format
  response_format = {"type": "json_object"}
)

# Print the response
print(response.choices[0].message.content)

'''
O código acima mostra como obter a resposta de uma chamada de API da OpenAI no formato JSON. Especificamente, o prompt pede ao modelo que os títulos e autores dos livros sejam organizados em um arquivo JSON e o parâmetro `response_format` é usado para especificar que a resposta deve ser um objeto JSON.
'''