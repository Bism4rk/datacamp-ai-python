from openai import OpenAI

def get_response(prompt):
    print(prompt)

product_description = "like yeah the product's real good mate innit"

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt to summarize the product description
prompt = """Summarize the text delimited by triple backticks, in at most five bullet points.

```{product_description}``` 
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)

'''
O código acima é um exemplo de resumo de uma descrição de produto. O objetivo é resumir a descrição do produto delimitada por três crases em no máximo cinco pontos principais.
O modelo deve identificar os principais aspectos do produto e apresentá-los de forma concisa e clara.
'''