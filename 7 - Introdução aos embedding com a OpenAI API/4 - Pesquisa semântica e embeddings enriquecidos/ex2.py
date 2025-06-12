from scipy.spatial import distance

def find_n_closest(query_vector, embeddings, n=3):
  distances = []
  for index, embedding in enumerate(embeddings):
    # Calculate the cosine distance between the query vector and embedding
    dist = distance.cosine(query_vector, embedding)
    # Append the distance and index to distances
    distances.append({"distance": dist, "index": index})
  # Sort distances by the distance key
  distances_sorted = sorted(distances, key=lambda x: x["distance"])
  # Return the first n elements in distances_sorted
  return distances_sorted[0:n]

'''
O código acima mostra uma função que usa embeddings para encontrar os n produtos mais próximos de um vetor de consulta (query vector). A função `find_n_closest` calcula a distância coseno entre o vetor de consulta e cada embedding na lista de embeddings, armazenando as distâncias e os índices correspondentes. Em seguida, ela ordena as distâncias por meio de uma função de ordenação e retorna os n produtos mais próximos, com base na menor distância. Essa abordagem é útil para tarefas de busca semântica, onde você deseja encontrar itens semelhantes com base em suas representações vetoriais. 
'''