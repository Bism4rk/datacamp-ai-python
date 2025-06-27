from pinecone import Pinecone, ServerlessSpec
from openai import OpenAI
from dotenv import load_dotenv
from uuid import uuid4
import numpy as np
import pandas as pd
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

# Initialize the Pinecone client
pc = Pinecone(api_key=apikey)
client = OpenAI(api_key='INSERT API KEY HERE')
index = pc.Index('pinecone-datacamp')

youtube_df = pd.read_csv('https://raw.githubusercontent.com/datacamp/datacamp-datasets/main/youtube_dataset.csv')

batch_limit = 100

index = pc.Index('pinecone-datacamp')

# Define a retrieve function that takes four arguments: query, top_k, namespace, and emb_model
def retrieve(query, top_k, namespace, emb_model):
    # Encode the input query using OpenAI
    query_response = client.embeddings.create(
        input=query,
        model=emb_model
    )
    
    query_emb = query_response.data[0].embedding
    
    # Query the index using the query_emb
    docs = index.query(vector=query_emb, top_k=top_k, namespace=namespace, include_metadata=True)
    
    retrieved_docs = []
    sources = []
    for doc in docs['matches']:
        retrieved_docs.append(doc['metadata']['text'])
        sources.append((doc['metadata']['title'], doc['metadata']['url']))
    
    return retrieved_docs, sources

documents, sources = retrieve(
  query="How to build next-level Q&A with OpenAI",
  top_k=3,
  namespace='youtube_rag_dataset',
  emb_model="text-embedding-3-small"
)
print(documents)
print(sources)

'''
O código acima mostra como inserir dados de um DataFrame do Pandas em um índice do Pinecone, utilizando embeddings gerados pela API OpenAI. Ele:
1. Divide o DataFrame em lotes.
2. Extrai metadados e textos de cada lote.
3. Gera IDs únicos para cada vetor.
4. Cria embeddings dos textos usando a API OpenAI.
5. Insere esses vetores no índice do Pinecone com os metadados correspondentes.


'''