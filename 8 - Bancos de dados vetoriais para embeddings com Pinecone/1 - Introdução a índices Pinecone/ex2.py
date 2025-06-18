# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

# Create your Pinecone index
pc.create_index(
    name="my-first-index-test",
    dimension=256,
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

'''
O código acima mostra como criar um índice no Pinecone usando a classe ServerlessSpec para especificar as configurações do índice, como a nuvem e a região. O cliente Pinecone é inicializado com uma chave de API (inicializado por meio de um arquivo .env para segurannça) e o índice é criado com um nome, uma dimensão (número de características dos embeddings) e as especificações do servidor sem servidor (ServerlessSpec).
'''