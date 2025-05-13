from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = "You are a customer service chatbot for a delivery service that responds to user queries in a gentle way."

context_question = "What types of items can be delivered using MyPersonalDelivery?"
context_answer = "We deliver everything from everyday essentials such as groceries, medications, and documents to larger items like electronics, clothing, and furniture. However, please note that we currently do not offer delivery for hazardous materials or extremely fragile items requiring special handling."

# Add the context to the model
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "system", "content": system_prompt},
            {"role": "user", "content": context_question},
            {"role": "assistant", "content": context_answer},
            {"role": "user", "content": "Do you deliver furniture?"}])
response = response.choices[0].message.content
print(response)

'''
O código acima é um exemplo de como incorporar contexto externo em um chatbot. O sistema atua como um chatbot de atendimento ao cliente para um serviço de entrega, respondendo a perguntas dos usuários de forma gentil.
O contexto é adicionado ao modelo através de mensagens que incluem uma pergunta do usuário e a resposta do assistente, permitindo que o modelo utilize essas informações para responder a perguntas subsequentes.
'''