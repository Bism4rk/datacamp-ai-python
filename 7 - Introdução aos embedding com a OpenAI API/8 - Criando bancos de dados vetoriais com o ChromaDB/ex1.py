import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# Create a persistant client
client = chromadb.PersistentClient()

# Create a netflix_title collection using the OpenAI Embedding function
collection = client.create_collection(
    name="netflix_titles",
    embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# List the collections
print(client.list_collections())

'''
O código acima é um exemplo de como criar uma coleção no ChromaDB usando a função de embedding da OpenAI.
A coleção é chamada "netflix_titles" e utiliza o modelo "text-embedding-3-small" da OpenAI para gerar embeddings dos dados.
A função create_collection toma 2 parâmetros: o nome da coleção e a função de embedding a ser utilizada, que em si toma 2 parâmetros: o nome do modelo e a chave da API da OpenAI.
'''