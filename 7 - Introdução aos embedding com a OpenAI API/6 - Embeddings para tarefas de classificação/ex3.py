from openai import OpenAI
from scipy import spatial as distance

client = OpenAI(api_key="THIS IS A FAKE KEY, A REAL KEY IS REQUIRED TO RUN THIS CODE")

reviews = [
    "I love this product, it works great!",
    "This is the worst purchase I've ever made.",
    "It's okay, not the best but not the worst.",
    "Absolutely fantastic! Highly recommend it.",
    "Terrible experience, I will never buy this again."
    ]

sentiments = [
    {"label": "positive", "description": "This is a positive sentiment."},
    {"label": "negative", "description": "This is a negative sentiment."},
    {"label": "neutral", "description": "This is a neutral sentiment."}
    ]
def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  
  return [data['embedding'] for data in response_dict['data']]


# Extract and embed the descriptions from sentiments
class_descriptions = [sentiment['description'] for sentiment in sentiments]
class_embeddings = create_embeddings(class_descriptions)
review_embeddings = create_embeddings(reviews)

def find_closest(query_vector, embeddings):
  distances = []
  for index, embedding in enumerate(embeddings):
    dist = distance.cosine(query_vector, embedding)
    distances.append({"distance": dist, "index": index})
  return min(distances, key=lambda x: x["distance"])

for index, review in enumerate(reviews):
  closest = find_closest(review_embeddings[index], class_embeddings)
  label = sentiments[closest['index']]['label']
  print(f'"{review}" was classified as {label}')

'''
O código acima é um exemplo de como usar embeddings para classificar textos, neste caso, avaliações de produtos. Ele cria embeddings para as avaliações e para as descrições dos sentimentos, e depois encontra a classe mais próxima para cada avaliação com base na distância entre os embeddings. Nesse caso, os embeddings são criados usando as descrições do sentimentos e não só os rótulos, o que pode melhorar a precisão da classificação, pois as descrições fornecem mais contexto sobre o que cada sentimento representa.

De resto, o processo é semelhante ao exemplo anterior, onde as distâncias são calculadas e a classe mais próxima é identificada para cada avaliação. A saída do código mostra como cada avaliação foi classificada de acordo com os sentimentos definidos.

'''