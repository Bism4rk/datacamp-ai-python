from openai import OpenAI

service_description = "MyPersonalDelivery is a delivery service that offers fast and reliable delivery of a wide range of items, including groceries, electronics, clothing, and furniture. We prioritize customer satisfaction and ensure that all deliveries are handled with care. Our service is available 24/7, and we offer real-time tracking for all deliveries."

def get_response(system_prompt, user_prompt):
    # Assign the role and content for each message
    messages = [{"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}]  
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, temperature=0)
    
    return response.choices[0].message.content

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the system prompt
system_prompt = f"""You are a customer service chatbot for a delivery service that responds to user queries in a gentle way. A description of the service is delimited by triple backticks.
```{service_description}```
"""

user_prompt = "What benefits does MyPersonalDelivery offer?"

# Get the response to the user prompt
response = get_response(system_prompt, user_prompt)

print(response)

'''
O código acima é mais um exemplo de como incorporar contexto externo em um chatbot. O sistema atua como um chatbot de atendimento ao cliente para um serviço de entrega, respondendo a perguntas dos usuários de forma gentil. Dessa vez, o modelo é informado sobre a descrição do serviço por meio de uma string delimitada por três crases. Isso permite que o modelo utilize essas informações para responder a perguntas subsequentes, como os benefícios do serviço.
'''