# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec, itertools
from dotenv import load_dotenv
import os
import vectorfr

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

vector = vectorfr.vector  # Example vector, replace with your actual vector

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

index = pc.Index('datacamp-index')

# Query namespace1 with the vector provided
query_result = index.query(
    vector=vector,
    namespace='namespace1',
    top_k=3
)
print(query_result)

'''
O código acima mostra como consultar um namespace específico em um índice do Pinecone usando um vetor fornecido. Ele utiliza o método `query` para buscar os vetores mais semelhantes ao vetor de consulta no namespace `namespace1`, retornando os 3 vetores mais próximos. O resultado da consulta é impresso, mostrando os vetores correspondentes e suas pontuações de similaridade.
'''