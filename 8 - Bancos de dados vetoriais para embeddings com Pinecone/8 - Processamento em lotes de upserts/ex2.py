# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec, itertools
from dotenv import load_dotenv
import os
import vectorfr

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

vectors = vectorfr.vector # Example vector, replace with your actual vector


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

index = pc.Index('datacamp-index')

# Upsert vectors in batches of 100
for chunk in chunks(vectors):
    index.upsert(vectors=chunk) 

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())

'''
O código acima demonstra como realizar upserts (inserções ou atualizações) de vetores no Pinecone em lotes de 100. A função `chunks` divide o vetor em pedaços menores, permitindo que você processe grandes conjuntos de dados sem sobrecarregar a memória. O método `upsert` do índice é utilizado para inserir ou atualizar os vetores em cada lote. Após o processamento, o código busca as estatísticas do índice conectado usando o método `describe_index_stats`, que fornece informações sobre o estado atual do índice, como o número de vetores armazenados e espaço utilizado.
'''