from openai import OpenAI

def get_response(prompt):
    print(prompt)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

examples="""input = [10, 5, 8] -> output = 23
input = [5, 2, 4] -> output = 11
input = [2, 1, 3] -> output = 6
input = [8, 4, 6] -> output = 18
"""

# Craft a prompt that asks the model for the function
prompt = f"""You are provided with input-output examples delimited by triple backticks for a Python function where different factors are associated with project completion time. Each example includes numerical values for the factors and the corresponding estimated completion time. Write code for this function.
 ```{examples}```"""

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de geração de código usando a API do OpenAI e exemplos. O prompt solicita ao modelo que escreva uma função Python que aceita exemplos de entrada e saída delimitados por três crases para uma função onde diferentes fatores estão associados ao tempo de conclusão do projeto. Cada exemplo inclui valores numéricos para os fatores e o tempo estimado de conclusão correspondente.
'''