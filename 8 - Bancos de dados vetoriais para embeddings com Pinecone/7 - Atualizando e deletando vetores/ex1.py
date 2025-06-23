# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
import vectorfr

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

vector = vectorfr.vector # Example vector, replace with your actual vector

# Initialize the Pinecone client with your API key
pc = Pinecone(api_key=apikey)

index = pc.Index('datacamp-index')

# Update the values of vector ID 7
index.update(
    id='7',
    values=vector
)

# Fetch vector ID 7
fetched_vector = index.fetch(ids=['7'])
print(fetched_vector)

'''
O código acima demonstra como atualizar um vetor específico no Pinecone. Ele utiliza o método `update` do índice para modificar os valores do vetor com o ID '7'. Após a atualização, o código busca o vetor atualizado usando o método `fetch` e imprime os detalhes do vetor atualizado. Isso é útil para manter os dados no banco de dados vetorial atualizados com as informações mais recentes.
'''