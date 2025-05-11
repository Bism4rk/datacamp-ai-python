from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(system_prompt, user_prompt):
  # Assign the role and content for each message
  messages = [{"role": "system", "content": system_prompt},
             {"role": "user", "content": user_prompt}]  
  response = client.chat.completions.create(
      model="gpt-4o-mini", messages= messages, temperature=0)
  
  return response.choices[0].message.content

# Define the purpose of the chatbot
chatbot_purpose = "You are the customer support chatbot for an e-commerce platform specializing in electronics. Your role is to assist customers with inquiries, order tracking, and troubleshooting common issues related to their purchases. "

# Define audience guidelines
audience_guidelines = "Your primary audience consists of tech-savvy individuals who are interested in purchasing electronic gadgets. "

# Define tone guidelines
tone_guidelines = "Maintain a professional and user-friendly tone in your responses."

base_system_prompt = chatbot_purpose + audience_guidelines + tone_guidelines
response = get_response(base_system_prompt, "My new headphones aren't connecting to my device")
print(response)

'''
O código acima é um exemplo de engenharia de prompts para um chatbot. A função get_response recebe dois parâmetros: system_prompt e user_prompt. O system_prompt define o comportamento do chatbot, enquanto o user_prompt é a pergunta feita pelo usuário. O chatbot é projetado para fornecer suporte ao cliente em uma plataforma de comércio eletrônico especializada em eletrônicos. O chatbot deve manter um tom profissional e amigável, atendendo a um público-alvo de indivíduos interessados em gadgets eletrônicos.
'''
