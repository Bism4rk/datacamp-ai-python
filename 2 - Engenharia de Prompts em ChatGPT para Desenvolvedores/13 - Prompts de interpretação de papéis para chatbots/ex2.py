from openai import OpenAI

def get_response(system_prompt, user_prompt):
    # Assign the role and content for each message
    messages = [{"role": "system", "content": system_prompt},
                 {"role": "user", "content": user_prompt}]  
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages= messages, temperature=0)
    
    return response.choices[0].message.content


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = "Ask the user about their background, experience, and goals whenever these aren't given."

# Define response guidelines
response_guidelines = "Recommend at most three textbooks."

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt, user_prompt)
print(response)


'''
O código acima é mais um exemplo de papéis de interpretação para chatbots, dessa vez com diretrizes de comportamento e resposta. O sistema atua como um conselheiro de aprendizado, fazendo perguntas ao usuário sobre seu histórico e interesses, e recomendando livros adequados baseados nessas informações.
O sistema também tem diretrizes para limitar o número de recomendações a três livros e perguntar ao usuário sobre seu histórico e objetivos, caso essas informações não sejam fornecidas.
'''