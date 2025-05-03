from openai import OpenAI

def get_response(prompt):
    print(prompt)

# Create a prompt that generates the table
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a prompt that generates the table
prompt = "Create a table with 10 books I should read with 3 columns - Title, Author and Publishing Year - as I like science fiction novels."

# Get the response
response = get_response(prompt)
print(response)
'''
O código acima é um exemplo de saídas estruturadas. O prompt pede que o modelo gere uma tabela com 10 livros de ficção científica, incluindo o título, autor, e o ano de publicação. Isso demonstra como a engenharia de prompts pode ser usada para guiar o modelo a gerar respostas mais organizadas e estruturadas.

'''