# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")


# Set up the client with your API key
pc = Pinecone(api_key=apikey)

# Connect to your index
index = pc.Index("my-first-index")

# Print the index statistics
print(index.describe_index_stats())

'''
O código acima mostra como se conectar a um índice existente no Pinecone e imprimir as estatísticas do índice. A classe Pinecone é usada para inicializar o cliente com uma chave de API, e o método Index é usado para se conectar ao índice especificado. As estatísticas do índice são então impressas usando o método describe_index_stats(). As estatísticas do índice incluem informações como o número de vetores, o número de namespaces e o tamanho total do índice. Isso é útil para monitorar o desempenho e a utilização do índice no Pinecone.
'''