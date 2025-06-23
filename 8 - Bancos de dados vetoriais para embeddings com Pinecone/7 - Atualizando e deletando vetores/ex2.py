# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")


# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

index = pc.Index('datacamp-index')

# Update the metadata of vector ID 7
index.update(
    id='7',
    set_metadata={"genre": "thriller", "year": 2024}
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=['7'])
print(fetched_vector)

'''
O código acima é um exemplo de como atualizar os metadados de um vetor específico no Pinecone. Ele utiliza o método `update` do índice para modificar os metadados do vetor com o ID '7', definindo novos valores para o gênero e o ano. Após a atualização, o código busca o vetor atualizado usando o método `fetch` e imprime os detalhes do vetor atualizado, incluindo os novos metadados. Isso é útil para manter as informações associadas aos vetores atualizadas e relevantes.
'''