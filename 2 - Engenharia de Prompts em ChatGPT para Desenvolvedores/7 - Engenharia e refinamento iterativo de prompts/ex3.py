from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    print(prompt)

# Refine the following prompt
prompt = """
Receiving a promotion at work made me feel on top of the world -> Happiness
The movie's ending left me with a heavy feeling in my chest -> Sadness
Walking alone in the dark alley sent shivers down my spine -> Fear
Time flies like an arrow -> No explicit emotion
I watched TV today -> No explicit emotion
They sat and ate their meal ->
"""

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de refinamento de prompt. O objetivo é classificar as frases em emoções explícitas ou não explícitas.
O modelo deve identificar as emoções associadas a cada frase e classificá-las corretamente.
Os exemplos foram refinados para que o modelo retorne uma resposta mais precisa e relevante.
'''