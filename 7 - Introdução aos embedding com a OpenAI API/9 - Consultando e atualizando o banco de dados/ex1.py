import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient()

# Retrieve the netflix_titles collection
collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# Query the collection for "films about dogs"
result = collection.query(
  query_texts=["films about dogs"],
  n_results=3
)

print(result)

'''
O código acima é um exemplo de como consultar uma coleção no ChromaDB usando a função de embedding da OpenAI. Ele busca por documentos relacionados a "filmes sobre cães" na coleção "netflix_titles" e retorna os 3 resultados mais relevantes. A função query toma 2 parâmetros: o texto da consulta e o número de resultados desejados.
O resultado é impresso no console, mostrando os documentos que correspondem à consulta.
'''