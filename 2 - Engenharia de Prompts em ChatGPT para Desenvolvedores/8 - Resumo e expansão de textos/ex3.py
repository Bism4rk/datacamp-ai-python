from openai import OpenAI

product_description = "yeah fuck off"

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    print(prompt)

# Craft a prompt to expand the product's description
prompt = f"""
Expand the product description for the Smart Home Security Camera delimited by triple backticks to provide a comprehensive overview of its features, benefits, potential applications, without bypassing the limit of one paragraph. 
 ```{product_description}```
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)

'''
O código acima é um exemplo de expansão de texto usando LLMs. O prompt pede que o modelo expanda a descrição do produto, no caso um sistema de segurança, focando nas suas características, benefícios, e aplicações potenciais, sem ultrapassar o limite de um parágrafo.
'''