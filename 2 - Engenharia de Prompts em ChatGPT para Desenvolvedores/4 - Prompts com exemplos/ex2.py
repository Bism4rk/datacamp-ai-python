from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    print(prompt)

# Create a one-shot prompt
prompt = """Extract the odd numbers from a group of numbers as follows:
Q: {1, 3, 7, 12, 9} A: {1, 3, 7, 9}
Q: {3, 5, 11, 12, 16} A:
"""

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de one-shot prompting, onde o modelo é apresentado a um exemplo de entrada e saída antes de fazer uma pergunta semelhante. O modelo deve aprender a tarefa com base nesse exemplo e aplicar o mesmo raciocínio à nova entrada.
'''