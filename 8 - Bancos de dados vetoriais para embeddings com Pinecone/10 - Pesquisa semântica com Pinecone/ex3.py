from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from dotenv import load_dotenv
from uuid import uuid4
import numpy as np
import pandas as pd
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)
client = OpenAI(api_key=apikey)
index = pc.Index('pinecone-datacamp')

df = pd.read_csv('https://raw.githubusercontent.com/datacamp/datacamp-datasets/main/squad_dataset.csv')

batch_limit = 100

query = "What is in front of the Notre Dame Main Building?"

# Create the query vector
query_response = client.embeddings.create(
    input=query,
    model="text-embedding-3-small"
)
query_emb = query_response.data[0].embedding

# Query the index and retrieve the top five most similar vectors
retrieved_docs = index.query(vector=query_emb, top_k=5, namespace='squad_dataset', include_metadata=True)

for result in retrieved_docs['matches']:
    print(f"{result['id']}: {round(result['score'], 2)}")
    print('\n')

'''
O código acima mostra como realizar uma consulta semântica em um índice do Pinecone usando um vetor de consulta gerado a partir de uma pergunta. Ele utiliza a API OpenAI para criar o vetor de consulta e, em seguida, consulta o índice do Pinecone para recuperar os cinco vetores mais semelhantes, incluindo seus metadados. Os resultados são impressos, mostrando os IDs dos vetores correspondentes e suas pontuações de similaridade.
'''