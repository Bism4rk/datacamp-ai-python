# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

# Initialize the Pinecone client using your API key
pc = Pinecone(api_key=apikey)

index = pc.Index('datacamp-index')

# Delete vectors
index.delete(ids=['3', '4'])

# Retrieve metrics of the connected Pinecone index
print(index.describe_index_stats())

'''
O código acima é um exemplo de como deletar vetores específicos de um índice no Pinecone. Ele utiliza o método `delete` do índice para remover os vetores com os IDs '3' e '4'. Após a exclusão, o código busca as métricas do índice conectado usando o método `describe_index_stats`, que fornece informações sobre o estado atual do índice, como o número de vetores armazenados, espaço utilizado, entre outros. Isso é útil para gerenciar e monitorar os dados armazenados no Pinecone.
'''