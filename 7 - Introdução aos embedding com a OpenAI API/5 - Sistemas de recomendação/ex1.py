'''
# Combine the features for last_product and each product in products
last_product_text = create_product_text(last_product)
product_texts = [create_product_text(product) for product in products]

# Embed last_product_text and product_texts
last_product_embeddings = create_embeddings(last_product_text)[0]
product_embeddings = create_embeddings(product_texts)

# Find the three smallest cosine distances and their indexes
hits = find_n_closest(last_product_embeddings, product_embeddings)

for hit in hits:
  product = products[hit['index']]
  print(product['title'])
'''

'''
O código acima é um exemplo de como usar embeddings para encontrar produtos semelhantes em um sistema de recomendação usando a OpenAI API. Ele cria embeddings para um produto específico e uma lista de produtos, e então encontra os produtos mais próximos com base na similaridade dos embeddings. A função `create_product_text` combina as informações do produto em um único texto, que é então usado para gerar os embeddings na função `create_embeddings`. A função `find_n_closest` calcula a distância coseno entre o embedding do produto de interesse e os embeddings dos outros produtos, retornando os mais próximos. Finalmente, os títulos dos produtos recomendados são impressos. Essa abordagem permite uma recomendação baseada em similaridade semântica, melhorando a experiência do usuário ao sugerir produtos relevantes.
'''