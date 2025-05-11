from openai import OpenAI

base_system_prompt = "You are the customer support chatbot for an e-commerce platform specializing in electronics. Your role is to assist customers with inquiries, order tracking, and troubleshooting common issues related to their purchases. Your primary audience consists of tech-savvy individuals who are interested in purchasing electronic gadgets. Maintain a professional and user-friendly tone in your responses."

def get_response(system_prompt, user_prompt):
    # Assign the role and content for each message
    messages = [{"role": "system", "content": system_prompt},
                 {"role": "user", "content": user_prompt}]  
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages= messages, temperature=0)
    
    return response.choices[0].message.content

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the order number condition
order_number_condition = "If you are not provided with an order number, ask that the user provide one."

# Define the technical issue condition
technical_issue_condition = "If the user is relating a technical problem, start your answer with 'I'm sorry to hear about your issue with...'"

# Create the refined system prompt
refined_system_prompt = base_system_prompt + order_number_condition + technical_issue_condition

response_1 = get_response(refined_system_prompt, "My laptop screen is flickering. What should I do?")
response_2 = get_response(refined_system_prompt, "Can you help me track my recent order?")

print("Response 1: ", response_1)
print("Response 2: ", response_2)

'''
O código acima é mais um exemplo de engenharia de prompts para um chatbot. Nesse caso, o prompt do sistema foi refinado para incluir condições específicas sobre o número do pedido e problemas técnicos. O chatbot agora pode lidar com perguntas relacionadas a problemas técnicos e solicitações de rastreamento de pedidos de forma mais eficaz. Se o cliente não fornecer um número de pedido, o chatbot solicitará que o usuário forneça um. Se o usuário relatar um problema técnico, o chatbot começará sua resposta com "Sinto muito por saber sobre seu problema com...".
'''