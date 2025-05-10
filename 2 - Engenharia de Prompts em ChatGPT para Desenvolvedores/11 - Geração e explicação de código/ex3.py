from openai import OpenAI

def get_response(prompt):
    print(prompt)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

function = """def calculate_area_rectangular_floor(width, length):
					return width*length"""

# Craft a multi-step prompt that asks the model to adjust the function
prompt = f"""Modify the script delimited by triple backticks as follows:
			 - Make sure to verify inputs are positive, otherwise, display an error message for the user
			 - Otherwise, return the area and perimeter of the rectangle.
			 ```{function}```"""

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de modificação de código usando a API do OpenAI. Ele solicita ao modelo que modifique uma função Python que calcula a área de um piso retangular, garantindo que as entradas sejam positivas e, caso contrário, exiba uma mensagem de erro para o usuário. Caso contrário, ele deve retornar a área e o perímetro do retângulo.
'''