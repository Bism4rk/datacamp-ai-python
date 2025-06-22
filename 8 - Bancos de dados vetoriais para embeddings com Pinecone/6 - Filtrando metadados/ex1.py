# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)

vector = [0.1] * 512, [0.5] * 512, [0.9] * 512  # Example vector, replace with your actual vector
apikey = os.getenv("apikey")

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

index = pc.Index('datacamp-index')

# Retrieve the MOST similar vector with the year 2024
query_result = index.query(
    vector=vector,
    filter={
        'year': 2024
    },
    top_k=1
)
print(query_result)

'''
O código acima mostra como filtrar resultados de uma consulta no Pinecone com base em metadados específicos. Ele utiliza o método `query` do índice para buscar o vetor mais similar ao vetor fornecido, aplicando um filtro que limita os resultados aos vetores que possuem o ano 2024 nos seus metadados. O resultado da consulta é impresso, mostrando os detalhes do vetor mais similar encontrado.
'''