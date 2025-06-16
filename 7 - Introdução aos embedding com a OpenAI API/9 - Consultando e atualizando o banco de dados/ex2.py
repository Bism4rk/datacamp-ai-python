import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

client = chromadb.PersistentClient()


new_data = [{"id": "s1001", "document": """Title: Cats & Dogs (Movie)
Description: A look at the top-secret, high-tech espionage war going on between cats and dogs, of which their human owners are blissfully unaware."""},

 {"id": "s6884", "document": """Title: Goosebumps 2: Haunted Halloween (Movie)

Description: Three teens spend their Halloween trying to stop a magical book, which brings characters from the "Goosebumps" novels to life.
Categories: Children & Family Movies, Comedies"""}]

collection = client.get_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# Update or add the new documents
collection.upsert(
    ids=[doc['id'] for doc in new_data],
    documents=[doc['document'] for doc in new_data]
)

# Delete the item with ID "s95"
collection.delete(ids=["s95"])

result = collection.query(
    query_texts=["films about dogs"],
    n_results=3
)
print(result)

'''
O código acima é um exemplo de como atualizar ou adicionar documentos em uma coleção no ChromaDB usando a função de embedding da OpenAI. Ele adiciona dois novos documentos à coleção "netflix_titles" e remove o documento com o ID "s95". A função upsert é usada para atualizar ou adicionar os documentos, enquanto a função delete é usada para remover um documento específico. Após as operações, o código consulta a coleção por "filmes sobre cães" e imprime os resultados.
'''