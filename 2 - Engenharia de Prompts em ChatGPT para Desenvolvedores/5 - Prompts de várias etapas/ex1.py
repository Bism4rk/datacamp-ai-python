from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    # Call the OpenAI API to get a response for the given prompt
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].message['content']

# Create a single-step prompt to get help planning the vacation
prompt = "Help me plan a vacation to the beach."

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de one-step prompting, ou seja, um prompt de uma única etapa.
'''

