from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    print(prompt)

# Define the example 
example = """Q: Sum the even numbers in the following set: {9, 10, 13, 4, 2}.
             A: Even numbers: 10, 4, 2. Adding them: 10+4+2 = 16"""

# Define the question
question = """Q: Sum the even numbers in the following set: {15, 13, 82, 7, 14}
              A:"""

# Create the final prompt
prompt = example + question
response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de prompting com cadeia de pensamentos por meio de one-shot prompting, onde o modelo é solicitado a pensar passo a passo para chegar à resposta correta. O prompt inicial apresenta um exemplo de pergunta e resposta, e em seguida, pede ao modelo para raciocinar sobre a resposta de uma nova pergunta. Isso ajuda a melhorar a precisão e a clareza das respostas geradas pelo modelo.
'''