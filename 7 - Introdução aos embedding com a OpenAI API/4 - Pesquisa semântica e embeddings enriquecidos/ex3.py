from scipy.spatial import distance
from openai import OpenAI

client = OpenAI(api_key="API KEY HERE")

def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  
  return [data['embedding'] for data in response_dict['data']]
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

product_embeddings = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]  # Example embeddings


products = [

    {

        "title": "Smartphone X1",

        "short_description": "The latest flagship smartphone with AI-powered features and 5G connectivity.",

        "price": 799.99,

        "category": "Electronics",

        "features": [

            "6.5-inch AMOLED display",

            "Quad-camera system with 48MP main sensor",

            "Face recognition and fingerprint sensor",

            "Fast wireless charging"

        ]

    },

    {
        "title": "Wireless Headphones Pro",

        "short_description": "Premium noise-cancelling headphones with long battery life and touch controls.",

        "price": 299.99,

        "category": "Audio",

        "features": [

            "Active noise cancellation",

            "30 hours of battery life",

            "Touch-sensitive controls",

            "Voice assistant integration"

        ]

    },

    {

        "title": "Smartwatch Series 5",

        "short_description": "Stylish smartwatch with health tracking, GPS, and customizable watch faces.",

        "price": 199.99,

        "category": "Wearables",

        "features": [

            "Heart rate monitoring",

            "Built-in GPS",

            "Water-resistant design",

            "Customizable watch faces"

        ]
    }

]

# Create the query vector from query_text
query_text = "computer"
query_vector = create_embeddings(query_text)[0]

# Find the five closest distances
hits = find_n_closest(query_vector, product_embeddings, 5)

print(f'Search results for "{query_text}"')
for hit in hits:
  # Extract the product at each index in hits
  product = products[hit["index"]]
  print(product["title"])

'''
O código acima demonstra como usar embeddings para realizar uma pesquisa semântica em um conjunto de produtos. Ele define uma função `create_embeddings` que utiliza a API da OpenAI para gerar embeddings a partir de textos. A função `find_n_closest` calcula a distância coseno entre um vetor de consulta (query vector) e uma lista de embeddings, retornando os n produtos mais próximos. A variável `hits` contém os resultados da pesquisa, e o código imprime os títulos dos produtos correspondentes. Essa abordagem é útil para encontrar produtos relacionados com base em descrições ou consultas de texto, permitindo uma busca mais eficiente e precisa em grandes conjuntos de dados.
'''