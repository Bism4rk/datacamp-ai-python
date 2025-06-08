from openai import OpenAI
import uuid

client = OpenAI(api_key="<OPENAI_API_TOKEN>")
messages = [{'role': 'system', 'content': 'You are a content moderator for a social media platform.'}, {'role': 'user', 'content': 'How about leveling up your snack game for a whole year? Take a quick survey and get a chance to win a year-long subscription to our epic snack boxes! Your insights are super valuable and help us level up.'}]

# Generate a unique ID
unique_id = str(uuid.uuid4())

response = client.chat.completions.create(  
  model="gpt-4o-mini", 
  messages=messages,
# Pass a user identification key
  user = unique_id
)

print(response.choices[0].message.content)

'''
O código acima é um exemplo de como user IDs podem ser usados para rastrear e identificar usuários de forma única em interações com a API da OpenAI. Neste caso, um ID único é gerado usando a biblioteca `uuid` e passado como um parâmetro `user` na solicitação de conclusão de chat. Isso pode ser útil para monitorar o uso da API por usuários específicos, coletar dados sobre interações e melhorar a moderação de conteúdo, garantindo que as respostas sejam adequadas e relevantes para cada usuário individual.
'''