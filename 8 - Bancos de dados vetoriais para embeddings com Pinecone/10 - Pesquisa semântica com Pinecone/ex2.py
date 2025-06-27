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

for batch in np.array_split(df, len(df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='squad_dataset')

'''
O código acima mostra como inserir vetores em um índice do Pinecone usando dados de um arquivo CSV. Ele lê o arquivo CSV contendo perguntas e respostas, divide os dados em lotes de tamanho definido (`batch_limit`), extrai metadados relevantes e utiliza a API OpenAI para gerar embeddings dos textos. Em seguida, os vetores são inseridos no índice do Pinecone com um namespace específico (`squad_dataset`), permitindo consultas semânticas eficientes posteriormente.
'''