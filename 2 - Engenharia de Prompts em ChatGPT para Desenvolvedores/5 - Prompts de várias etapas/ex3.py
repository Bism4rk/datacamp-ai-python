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

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

code = '''
def calculate_rectangle_area(length, width):
    area = length * width
    return area
'''

# Create a prompt that analyzes correctness of the code
prompt = f"""Determine the correctnes of the code delimited by triple backticks as follows:
Step 1: Check the correctness of the syntax.
Step 2: Check if the function receives two inputs
Step 3: Check if the function returns an output

Code: ```{code}```
"""

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de multi-step prompting, ou seja, um prompt de várias etapas.	
Nesse caso, o modelo é solicitado a checar se o código está correto, se a função recebe dois inputs e se a função retorna um output.
O modelo é solicitado a seguir uma série de etapas para gerar uma resposta mais completa e estruturada - a sintaxe, se a função recebe dois inputs e se a função retorna um output.
'''