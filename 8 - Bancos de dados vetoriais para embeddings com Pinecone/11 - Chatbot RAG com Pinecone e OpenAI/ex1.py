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
pc = Pinecone(api_key="pcsk_6bDVCU_PWeXezYoQHimbyb5DgcVM7kFwAYScuv1MtgLU7sRqBfD5rwg17vKqLAvaaQ6Rwi")
client = OpenAI(api_key='INSERT API KEY HERE')
index = pc.Index('pinecone-datacamp')

youtube_df = pd.read_csv('https://raw.githubusercontent.com/datacamp/datacamp-datasets/main/youtube_dataset.csv')

batch_limit = 100

for batch in np.array_split(youtube_df, len(youtube_df) / batch_limit):
    # Extract the metadata from each row
    metadatas = [{
      "text_id": row['id'],
      "text": row['text'],
      "title": row['title'],
      "url": row['url'],
      "published": row['published']} for _, row in batch.iterrows()]
    texts = batch['text'].tolist()
    
    ids = [str(uuid4()) for _ in range(len(texts))]
    
    # Encode texts using OpenAI
    response = client.embeddings.create(input=texts, model="text-embedding-3-small")
    embeds = [np.array(x.embedding) for x in response.data]
    
    # Upsert vectors to the correct namespace
    index.upsert(vectors=zip(ids, embeds, metadatas), namespace='youtube_rag_dataset')
    
print(index.describe_index_stats())

'''
O código acima mostra como inserir dados de um DataFrame do Pandas em um índice do Pinecone, utilizando embeddings gerados pela API OpenAI. Ele divide o DataFrame em lotes, extrai metadados e textos, gera IDs únicos para cada vetor, cria embeddings dos textos e, finalmente, insere esses vetores no índice do Pinecone com os metadados correspondentes. As estatísticas do índice são impressas ao final para verificar o sucesso da operação.
'''