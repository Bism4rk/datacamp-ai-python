from openai import OpenAI

# Create an OpenAI client
client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a request to obtain embeddings
response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Embeddings are a very useful tool to help capture the semantic meaning of text!"
)

# Convert the response into a dictionary
response_dict = response.model_dump()
print(response_dict)

'''
O código acima é um exemplo de como utilizar a API da OpenAI para obter embeddings de um texto. Embeddings são representações vetoriais de palavras ou frases que capturam o significado semântico do texto. No exemplo, estamos solicitando embeddings para a frase "Embeddings are a very useful tool to help transmit the semantic meaning of text!" usando o modelo "text-embedding-3-small".
'''