from openai import OpenAI

ticket_1 = "Help me with my billing issue"
ticket_2 = "I want to cancel my subscription"
ticket_3 = "I want to change my plan"
ticket_4 = "My password is not working"

entities_1 = "billing issue"
entities_2 = "subscription cancellation"
entities_3 = "technical issue"

def get_response(prompt):
    """
    Function to get a response from OpenAI API.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=100
    )
    return response.choices[0].message.content.strip()

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a few-shot prompt to get the ticket's entities
prompt = f"""Ticket: {ticket_1} -> Entities: {entities_1}
             Ticket: {ticket_2} -> Entities: {entities_2}
             Ticket: {ticket_3} -> Entities: {entities_3}
             Ticket: {ticket_4} -> Entities: """

response = get_response(prompt)

print("Ticket: \n", ticket_4)
print("Entities: \n", response)

'''
O código acima é mais um exemplo de análise de texto usando a API do OpenAI. Ele extrai entidades de um ticket de suporte, como problemas de cobrança, cancelamento de assinatura e problemas técnicos por meio da técnica de few-shot prompting e retorna as entidades extraídas.
'''