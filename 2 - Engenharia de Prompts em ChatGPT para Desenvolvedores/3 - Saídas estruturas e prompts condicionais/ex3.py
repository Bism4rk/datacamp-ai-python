from openai import OpenAI

text = "[texto de exemplo aqui]"
def get_response(prompt):
    print(prompt)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create the instructions
instructions = "You will be provided a text delimited by triple backticks. Identify its language and the number of sentences in it. If the text has more than one sentence, generate a title for it. If not, do not generate a title, and instead write 'N/A'."

# Create the output format
output_format = """Use the following format for the output:
- Text: <the text provided>
- Language: <the language the text is in>
- Title: <the title generated or N/A if the text only has one sentence>
"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de como criar um prompt que não apenas gera uma saída estruturada, mas também inclui lógica condicional. O modelo é instruído a identificar a linguagem do texto e o número de frases. Se o texto tiver mais de uma frase, ele deve gerar um título; caso contrário, deve escrever 'N/A'. Isso demonstra como a engenharia de prompts pode ser usada para guiar o modelo a gerar respostas mais complexas e adaptativas.
'''