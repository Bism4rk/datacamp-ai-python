# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

vectors = [
    {
        'id': 'vec1',
        'values': [0.1] * 1536,  # Example vector with 1536 dimensions
        'metadata': {
            'text': 'This is the first vector',
            'source': 'example_source_1'
        }
    },
    {
        'id': 'vec2',
        'values': [0.2] * 1536,  # Another example vector
        'metadata': {
            'text': 'This is the second vector',
            'source': 'example_source_2'
        }
    }
]

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

# Connect to your index
index = pc.Index("datacamp-index")

# Ingest the vectors and metadata
index.upsert(
    vectors=vectors
)
# Print the index statistics
print(index.describe_index_stats())

'''
O código acima demonstra como ingerir vetores com metadados no Pinecone. Ele define dois vetores, cada um com um ID, valores e metadados associados. Após inicializar o cliente Pinecone com a chave de API, o código conecta-se ao índice "datacamp-index" e insere os vetores usando o método `upsert`. Por fim, ele imprime as estatísticas do índice para verificar o sucesso da operação de ingestão.
'''