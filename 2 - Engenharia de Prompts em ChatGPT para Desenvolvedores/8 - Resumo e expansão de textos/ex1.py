from openai import OpenAI

report = "idk man some example text here"

def get_response(prompt):
    print(prompt)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the report
prompt = f"""Summarize the report delimited by triple backticks in five sentences, focusing on aspects related to AI and data privacy:

```{report}```"""

response = get_response(prompt)

print("Summarized report: \n", response)

'''
O código acima é um exemplo de resumo de um relatório. O objetivo é resumir o relatório delimitado por três crases em cinco frases, com foco em aspectos relacionados à IA e privacidade de dados.
'''