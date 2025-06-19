# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

vectors = [
    {
        'id': 'vec1',
        'values': [0.1] * 1536,  # Example vector with 1536 dimensions
    },
    {
        'id': 'vec2',
        'values': [0.2] * 1536,  # Another example vector
    }
]

# Initialize the Pinecone client using your API key
pc = Pinecone(api_key=apikey)

# Create your Pinecone index
pc.create_index(
    name="datacamp-index", 
    dimension=1536, 
    spec=ServerlessSpec(
        cloud='aws', 
        region='us-east-1'
    )
)

# Check that each vector has a dimensionality of 1536
vector_dims = [len(vector['values']) == 1536 for vector in vectors]
print(all(vector_dims))

'''
O código acima demonstra como criar um índice no Pinecone e verificar se os vetores inseridos possuem a dimensionalidade correta de 1536. A classe Pinecone é usada para inicializar o cliente com uma chave de API, e o método create_index é utilizado para criar um novo índice com as especificações fornecidas. Após a criação do índice, o código verifica se cada vetor tem exatamente 1536 dimensões, retornando True se todos os vetores estiverem corretos.
'''