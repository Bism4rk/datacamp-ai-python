# Import the Pinecone library
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")


# Initialize the Pinecone client
pc = Pinecone(api_key=apikey)

'''
O código acima mostra como importar a biblioteca Pinecone e inicializar o cliente com uma chave de API.
A chave de API é carregada de um arquivo .env usando a biblioteca dotenv, que permite gerenciar variáveis de ambiente de forma segura.

O Pinecone é um serviço de banco de dados vetorial que permite armazenar e consultar embeddings de alta dimensão de forma eficiente.
'''