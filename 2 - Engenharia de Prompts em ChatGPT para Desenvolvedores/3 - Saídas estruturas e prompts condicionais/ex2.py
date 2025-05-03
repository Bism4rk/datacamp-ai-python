from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

text = "[texto de exemplo aqui]"
def get_response(prompt):
    print(prompt)

# Create the instructions
instructions = f"You will be provided with a text delimited by triple backticks. Generate a suitable title for it and identify the language it is written in."

# Create the output format
output_format = """Use the following format for the output:
- Text: <Text we want to title>
- Language: <The language the text is written in>
- Title: <The generated title>
"""

# Create the final prompt
prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

'''
O código acima é mais um exemplo de saídas estruturadas. O prompt é dividido em duas partes: as instruções e o formato de saída. As instruções dizem ao modelo o que fazer, enquanto o formato de saída especifica como a resposta deve ser estruturada. Isso ajuda a garantir que a resposta do modelo seja organizada e fácil de entender.
'''