import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# Create a persistant client
client = chromadb.PersistentClient()

ids = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"] #exemplo

documents = ["""Title: Dick Johnson Is Dead (Movie)
Description: As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable.
Categories: Documentaries"""]

# Recreate the netflix_titles collection
collection = client.create_collection(
  name="netflix_titles",
  embedding_function=OpenAIEmbeddingFunction(model_name="text-embedding-3-small", api_key="<OPENAI_API_TOKEN>")
)

# Add the documents and IDs to the collection
collection.add(
  ids=ids,
  documents=documents
)

# Print the collection size and first ten items
print(f"No. of documents: {collection.count()}")
print(f"First ten documents: {collection.peek()}")

'''
O código acima mostra como adicionar documentos e IDs a uma coleção (o equivalente a uma tabela em um banco de dados ChromaDB). Após a criação da coleção, os ids e documents (que estão em lists próprios) são adicionados por meio da função add. Após isso, o código imprime o número de documentos na coleção e os primeiros dez documentos adicionados.
'''