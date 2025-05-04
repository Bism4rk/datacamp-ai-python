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

prompt = """
     Help me plan a beach vacation.
     Step 1 - Specify four potential locations for beach vacations
     Step 2 - State some accommodation options in each
     Step 3 - State activities that could be done in each
     Step 4 - Evaluate the pros and cons for each destination
    """

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de multi-step prompting, ou seja, um prompt de várias etapas.
O modelo é solicitado a seguir uma série de etapas para gerar uma resposta mais completa e estruturada.
O modelo é solicitado a especificar quatro locais de férias na praia, opções de acomodação, atividades e avaliar os prós e contras de cada destino.
'''