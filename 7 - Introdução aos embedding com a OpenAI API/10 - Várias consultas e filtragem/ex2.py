import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient()

collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

reference_texts = ["children's story about a car", "lions"]

# Query two results using reference_texts
result = collection.query(
  query_texts=reference_texts,
  n_results=2,
  # Filter for titles with a G rating released before 2019
  where={
    "$and": [
        {"rating": 
        	{"$eq": "G"}
        },
        {"release_year": 
         	{"$lt": 2019}
        }
    ]
  }
)

print(result['documents'])

'''
O código acima é um exemplo de como usar a biblioteca ChromaDB para consultar uma coleção de documentos com base em múltiplos textos de referência e filtrar os resultados por critérios específicos. Ele utiliza a função de incorporação da OpenAI para gerar embeddings dos textos e realizar a consulta. A consulta retorna os documentos mais relevantes com base nos textos de referência fornecidos, além de aplicar um filtro para obter apenas títulos com classificação "G" lançados antes de 2019. A variável `reference_texts` contém os textos de referência, e a consulta é feita com esses textos para obter os documentos mais relevantes na coleção "netflix_titles".
'''