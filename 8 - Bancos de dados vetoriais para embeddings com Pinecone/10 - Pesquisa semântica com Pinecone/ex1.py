from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

# Create Pinecone index
pc.create_index(
    name='pinecone-datacamp', 
    dimension=1536,
    spec=ServerlessSpec(cloud='aws', region='us-east-1')
)

# Connect to index and print the index statistics
index = pc.Index('pinecone-datacamp')
print(index.describe_index_stats())

'''
O código acima mostra como criar um índice no Pinecone com uma dimensão específica (1536) e uma especificação de servidor sem servidor (ServerlessSpec) para a nuvem AWS na região us-east-1. Após a criação do índice, ele se conecta ao índice recém-criado e imprime as estatísticas do índice, que fornecem informações sobre o estado atual do índice, como o número de vetores armazenados e espaço utilizado.
'''