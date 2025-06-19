# Import ServerlessSpec
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:\\Users\\reich\\Downloads\\datacamp-ai-python\\8 - Bancos de dados vetoriais para embeddings com Pinecone\\apikey.env", override=True)
apikey = os.getenv("apikey")

# Set up the client with your API key
pc = Pinecone(api_key=apikey)

# Delete your Pinecone index
pc.delete_index('my-second-index')

# List your indexes
print(pc.list_indexes())

'''
O código acima mostra como excluir um índice existente no Pinecone e listar os índices restantes. A classe Pinecone é usada para inicializar o cliente com uma chave de API, e o método delete_index é usado para excluir o índice especificado. Após a exclusão, o método list_indexes é chamado para listar os índices restantes no Pinecone. Isso é útil para gerenciar seus índices e garantir que você esteja trabalhando apenas com os índices necessários.
'''