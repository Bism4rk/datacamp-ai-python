'''
# Define a function to return the minimum distance and its index
def find_closest(query_vector, embeddings):
  distances = []
  for index, embedding in enumerate(embeddings):
    dist = distance.cosine(query_vector, embedding)
    distances.append({"distance": dist, "index": index})
  return min(distances, key=lambda x: x["distance"])

for index, review in enumerate(reviews):
  # Find the closest distance and its index using find_closest()
  closest = find_closest(review_embeddings[index], class_embeddings)
  # Subset sentiments using the index from closest
  label = sentiments[closest['index']]['label']
  print(f'"{review}" was classified as {label}')
'''

'''
O código acima define uma função `find_closest` que calcula a distância entre um vetor de consulta e uma lista de embeddings, retornando o índice do embedding mais próximo. Em seguida, para cada avaliação, ele encontra a classe mais próxima e imprime o rótulo correspondente.
'''