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

def prompt_with_context_builder(query, documents):
    prompt = f"Answer the following question based on the provided context:\n\nQuestion: {query}\n\nContext:\n"
    for i, doc in enumerate(documents):
        prompt += f"\nDocument {i+1}:\n{doc}\n"
    return prompt

# Initialize the Pinecone client
pc = Pinecone(api_key="pcsk_6bDVCU_PWeXezYoQHimbyb5DgcVM7kFwAYScuv1MtgLU7sRqBfD5rwg17vKqLAvaaQ6Rwi")
index = pc.Index('pinecone-datacamp')

query = "How to build next-level Q&A with OpenAI"

# Retrieve the top three most similar documents and their sources
documents, sources = retrieve(query, top_k=3, namespace='youtube_rag_dataset', emb_model="text-embedding-3-small")

prompt_with_context = prompt_with_context_builder(query, documents)
print(prompt_with_context)

def question_answering(prompt, sources, chat_model):
    sys_prompt = "You are a helpful assistant that always answers questions."
    
    # Use OpenAI chat completions to generate a response
    res = client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    answer = res.choices[0].message.content.strip()
    answer += "\n\nSources:"
    for source in sources:
        answer += "\n" + source[0] + ": " + source[1]
    
    return answer

answer = question_answering(
  prompt=prompt_with_context,
  sources=sources,
  chat_model='gpt-4o-mini')
print(answer)

'''
O código acima mostra como criar um chatbot RAG (Retrieval-Augmented Generation) usando Pinecone e OpenAI. Ele:
1. Define uma função `retrieve` para buscar documentos relevantes com base em uma consulta.
    1.1. Recupera embeddings da consulta usando o modelo de embeddings da OpenAI.
    1.2. Consulta o índice do Pinecone para obter os documentos mais relevantes.
    1.3  Retorna os documentos recuperados e suas fontes.

2. Define uma função `prompt_with_context_builder` para construir um prompt que inclui a consulta e os documentos recuperados.
    2.1. Formata o prompt para incluir a pergunta e o contexto dos documentos.

3. Define uma função `question_answering` que usa o modelo de chat da OpenAI para responder à pergunta com base no prompt e nas fontes.
    3.1. Configura um prompt do sistema para orientar o modelo de chat.
    3.2. Envia o prompt para o modelo de chat da OpenAI e obtém a resposta.

4. Recupera os documentos relevantes para a consulta "How to build next-level Q&A with OpenAI" e constrói o prompt com contexto.

5. Usa a função `question_answering` para gerar uma resposta com base no prompt e nas fontes recuperadas.

6. Imprime a resposta final, incluindo as fontes dos documentos utilizados.

'''