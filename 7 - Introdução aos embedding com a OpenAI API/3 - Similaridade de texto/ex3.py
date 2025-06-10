from openai import OpenAI
from scipy import spatial, distance
import numpy as np

client = OpenAI(api_key="<INSERT API KEY HERE>")

def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  
  return [data['embedding'] for data in response_dict['data']]


# Embed the search text
search_text = "soap"
search_embedding = create_embeddings(search_text)[0]

products = ["imagine there are products with embeddings here, it's way too long to fit here without blocking the screen",
           "each product has a short_description and an embedding"]

distances = []
for product in products:
  # Compute the cosine distance for each product description
  dist = distance.cosine(search_embedding, product['embedding'])
  distances.append(dist)

# Find and print the most similar product short_description    
min_dist_ind = np.argmin(distances)
print(products[min_dist_ind]['short_description'])

'''
- O código acima é um exemplo de como calcular a similaridade entre um texto de busca e uma lista de produtos usando embeddings.

- No caso, o loop for itera sobre uma lista de produtos, calcula a distância coseno entre o embedding do texto de exemplo ("soap) e o embedding de cada produto, e armazena essas distâncias em uma lista.

- Após isso, o código encontra o índice do produto com a menor distância (ou seja, o mais similar) por meio da função `np.argmin` da biblioteca numpy, e imprime a descrição curta desse produto.

'''
