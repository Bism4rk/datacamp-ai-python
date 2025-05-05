from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    print(prompt)

# Create the chain-of-thought prompt
prompt = """Q: My dad's friend's age is double that of my friend, which is 20? How old will the dad be in 10 years?

A: Let's think this step by step"""

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de prompting com cadeia de pensamentos, onde o modelo é solicitado a pensar passo a passo para chegar à resposta correta. O prompt inicial apresenta uma pergunta e, em seguida, pede ao modelo para raciocinar sobre a resposta. Isso ajuda a melhorar a precisão e a clareza das respostas geradas pelo modelo.
'''