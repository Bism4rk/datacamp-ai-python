from openai import OpenAI

def get_response(prompt):
    print(prompt)

# Refine the following prompt
prompt = "Generate a table that contains the top 10 pre-trained language models, with columns for language model, release year, and owners."

response = get_response(prompt)
print(response)

'''
O código acima é um exemplo de refinamento de prompt. O objetivo é gerar uma tabela com os 10 principais modelos de linguagem pré-treinados, incluindo o nome do modelo, ano de lançamento e proprietários. 
'''