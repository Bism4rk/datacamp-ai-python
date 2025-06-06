from openai import OpenAI

def get_response(system_prompt, user_prompt):
    # Assign the role and content for each message
    messages = [{"role": "system", "content": system_prompt},
                 {"role": "user", "content": user_prompt}]  
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages= messages, temperature=0)
    
    return response.choices[0].message.content

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft the system_prompt using the role-playing approach
system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

user_prompt = "Hello there! I'm a beginner with a marketing background, and I'm really interested in learning about Python, data analytics, and machine learning. Can you recommend some books?"

response = get_response(system_prompt, user_prompt)
print(response)

'''
O código acima é um exemplo de papéis de interpretação para chatbots, onde o sistema atua como um conselheiro de aprendizado. O usuário fornece informações sobre seu histórico e interesses, e o sistema recomenda livros adequados baseados nessas informações.
'''