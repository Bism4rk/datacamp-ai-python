# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec, itertools
from dotenv import load_dotenv
import vectorfr


# Initialize the client
pc = Pinecone(api_key="pcsk_6bDVCU_PWeXezYoQHimbyb5DgcVM7kFwAYScuv1MtgLU7sRqBfD5rwg17vKqLAvaaQ6Rwi", pool_threads=20)

index = pc.Index('datacamp-index')

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

# Upsert vectors in batches of 200 vectors
with pc.Index('datacamp-index', pool_threads=20) as index:
    async_results = [index.upsert(vectors=chunk, async_req=True) for chunk in chunks(vectors, batch_size=200)]
    [async_result.get() for async_result in async_results]

# Retrieve statistics of the connected Pinecone index
print(index.describe_index_stats())

'''
O código acima mostra como fazer upserts (inserções ou atualizações) de vetores no Pinecone em lotes de 200 vetores de forma paralela. Ele utiliza a função `chunks` para dividir os vetores em pedaços menores, permitindo que você processe grandes conjuntos de dados sem sobrecarregar a memória. O método `upsert` do índice é chamado com o parâmetro `async_req=True`, o que permite que as operações sejam executadas de forma assíncrona. Após o processamento, o código busca as estatísticas do índice conectado usando o método `describe_index_stats`, que fornece informações sobre o estado atual do índice, como o número de vetores armazenados e espaço utilizado.
'''