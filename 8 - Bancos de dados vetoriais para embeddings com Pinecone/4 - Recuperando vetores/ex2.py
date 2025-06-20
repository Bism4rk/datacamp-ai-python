# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

index = pc.Index('datacamp-index')
ids = ['2', '5', '8']

# Fetch the vectors from the connected Pinecone index
fetched_vectors = index.fetch(ids=ids)

# Extract the metadata from each result in fetched_vectors
metadatas = [fetched_vectors['vectors'][id]['metadata'] for id in ids]
print(metadatas)

'''
O código acima mostra como recuperar vetores de um índice Pinecone usando IDs específicos. Após inicializar o cliente Pinecone com a chave de API, ele conecta-se ao índice "datacamp-index". Em seguida, busca os vetores correspondentes aos IDs fornecidos e extrai os metadados de cada vetor recuperado. Por fim, imprime os metadados para visualização.
'''