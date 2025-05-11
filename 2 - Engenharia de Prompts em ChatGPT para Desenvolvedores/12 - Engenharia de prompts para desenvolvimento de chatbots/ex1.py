from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
      		  {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Try the function with a system and user prompts of your choice 
response = get_response("You are a chatbot that answers coding questions", "When was Python created?")
print(response)

'''
O código acima é um exemplo de engenharia de prompts para um chatbot. A função get_response recebe dois parâmetros: system_prompt e user_prompt. O system_prompt define o comportamento do chatbot, enquanto o user_prompt é a pergunta feita pelo usuário.
'''