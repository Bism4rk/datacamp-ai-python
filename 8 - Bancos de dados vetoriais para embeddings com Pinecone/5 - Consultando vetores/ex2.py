# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

# Create an index that uses the dot product distance metric
pc.create_index(
    name="dotproduct-index",
    dimension=1536,
    metric='dotproduct',
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'
    )
)

# Print a list of your indexes
print(pc.list_indexes())

'''
O código acima mostra como criar um índice no Pinecone que usa uma métrica diferente de distância, especificamente a métrica de produto escalar (dot product). A criação do índice é feita com o método `create_index`, onde você especifica o nome do índice, a dimensão dos vetores a métrica de distância, e o tipo de especificação do servidor (ServerlessSpec) que define a nuvem e a região onde o índice será hospedado. Após a criação, o código imprime uma lista dos índices disponíveis, incluindo o novo índice criado.
'''