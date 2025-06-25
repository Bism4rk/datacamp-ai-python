# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec, itertools
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

vector_set1 = [
    ("vec1", [0.1, 0.2, 0.3]),
    ("vec2", [0.4, 0.5, 0.6]),
    ("vec3", [0.7, 0.8, 0.9])
]

vector_set2 = [
    ("vec4", [0.9, 0.8, 0.7]),
    ("vec5", [0.6, 0.5, 0.4]),
    ("vec6", [0.3, 0.2, 0.1])  
]

# Vector_set1 and vector_set2 are just examples, replace them with your actual vectors.

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key="pcsk_6bDVCU_PWeXezYoQHimbyb5DgcVM7kFwAYScuv1MtgLU7sRqBfD5rwg17vKqLAvaaQ6Rwi")
index = pc.Index('datacamp-index')

# Upsert vector_set1 to namespace1
index.upsert(
  vectors=vector_set1,
  namespace='namespace1'
)

# Upsert vector_set2 to namespace2
index.upsert(
  vectors=vector_set2,
  namespace='namespace2'
)

# Print the index statistics
print(index.describe_index_stats())

'''
O códgio acima mostra como adicionar vetores a namespaces diferentes em um índice do Pinecone. Ele utiliza o método `upsert` para inserir vetores em dois namespaces distintos, `namespace1` e `namespace2`. Após a inserção, o código imprime as estatísticas do índice conectado usando o método `describe_index_stats`, que fornece informações sobre o estado atual do índice, como o número de vetores armazenados e espaço utilizado.
'''