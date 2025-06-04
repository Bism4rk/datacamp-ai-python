from openai import OpenAI

def get_response(messages, function_definition):
  print(messages)
  print(function_definition)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

messages = "text"
function_definition = "exemplo"

response = get_response(messages, function_definition)

# Define the function to extract the data dictionary
def extract_dictionary(response):
  return response.choices[0].message.tool_calls[0].function.arguments

# Print the data dictionary
print(extract_dictionary(response))

'''
O código acima é mais um exemplo da extração de dados estruturados de um texto. No caso, a função "extract_dictionary" retorna um dicionário JSON, que então é imprimido passando a resposta como parâmetro.
'''