# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

vector = [0.1] * 512, [0.5] * 512, [0.9] * 512  # Example vector, replace with your actual vector

# Initialize the Pinecone client using your API key
pc = Pinecone(api_key= "pcsk_6bDVCU_PWeXezYoQHimbyb5DgcVM7kFwAYScuv1MtgLU7sRqBfD5rwg17vKqLAvaaQ6Rwi"
)

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with genre and year filters
query_result = index.query(
    vector=vector,
    top_k=1,
    filter={
        "genre": {"$eq": "thriller"},
        "year": {"$lt": 2018}
    }
)
print(query_result)

'''
O código acima mostra como aplicar múltiplos filtros em uma consulta no Pinecone. Ele busca o vetor mais similar ao vetor fornecido, aplicando filtros que limitam os resultados aos vetores que possuem o gênero "thriller" e cujo ano é menor que 2018. O resultado da consulta é impresso, mostrando os detalhes do vetor mais similar encontrado, incluindo os metadados associados.
'''