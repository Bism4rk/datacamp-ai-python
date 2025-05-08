from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1500,
        n=1,
        stop=None
    )
    return response.choices[0].message['content']

sample_email = """Subject: Check out our latest products!
    
    Dear Customer,
    
    We are excited to introduce our latest product line that includes a wide range of items to suit your needs. Whether you're looking for electronics, home appliances, or fashion accessories, we have it all!
    
    Hurry and visit our website to explore the fantastic deals and discounts we have for you. Don't miss out on the opportunity to get the best products at unbeatable prices.
    
    Thank you for being a valued customer, and we look forward to serving you soon!
    
    Best regards,
    The Marketing Team"""

# Craft a prompt to change the email's tone
prompt = f"""Write the text delimited by triple backticks using a professional, positive, user-centric tone:
```{sample_email}```"""

response = get_response(prompt)

print("Before transformation: \n", sample_email)
print("After transformation: \n", response)

'''
O código acima é mais um exemplo de transformação de texto, nesse caso mudança de tom. O prompt pede que o modelo reescrite o texto em um tom profissional, positivo, e centrado no usuário.
'''