import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient()

collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

reference_ids = ['s999', 's1000']

# Retrieve the documents for the reference_ids
reference_texts = collection.get(ids=reference_ids)['documents']

# Query using reference_texts
result = collection.query(
  query_texts=reference_texts,
  n_results=3
)

print(result['documents'])

'''
O código acima é um exemplo de como usar a biblioteca ChromaDB para consultar uma coleção de documentos com base em múltiplos textos de referência. Ele utiliza a função de incorporação da OpenAI para gerar embeddings dos textos e realizar a consulta. A consulta retorna os documentos mais relevantes com base nos textos de referência fornecidos. A varíavel `reference_texts` é criada a partir dos IDs de referência fornecidos, e a consulta é feita com esses textos para obter os documentos mais relevantes na coleção "netflix_titles".
'''