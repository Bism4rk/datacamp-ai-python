# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

vector = [0.1] * 512 + [0.2] * 512 + [0.3] * 512  # Example vector with 1536 dimensions

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

index = pc.Index('datacamp-index')

# Retrieve the top three most similar records
query_result = index.query(
    vector=vector,
    top_k=3
)

print(query_result)

'''
O código acima consulta um índice no Pinecone usando um vetor de exemplo de 1536 dimensões e retorna os três registros mais semelhantes. O método `query` é utilizado para realizar a consulta, especificando o vetor e o número de resultados desejados com o parâmetro `top_k`. O resultado da consulta é impresso no console.
'''