'''

# Prepare and embed the user_history, and calculate the mean embeddings
history_texts = [create_product_text(product) for product in user_history]
history_embeddings = create_embeddings(history_texts)
mean_history_embeddings = np.mean(history_embeddings, axis=0)

# Filter products to remove any in user_history
products_filtered = [product for product in products if product not in user_history]

# Combine product features and embed the resulting texts
product_texts = [create_product_text(product) for product in products_filtered]
product_embeddings = create_embeddings(product_texts)

hits = find_n_closest(mean_history_embeddings, product_embeddings)

for hit in hits:
  product = products_filtered[hit['index']]
  print(product['title'])

'''

'''
O código acima é um exemplo de como usar embeddings para recomendar produtos com base no histórico de compras do usuário. Ele cria embeddings para cada produto no histórico do usuário e calcula a média desses embeddings. Em seguida, ele filtra a lista de produtos para remover aqueles que já estão no histórico do usuário e cria embeddings para os produtos restantes. A função `find_n_closest` é usada para encontrar os produtos mais próximos com base na similaridade dos embeddings, e os títulos dos produtos recomendados são impressos. Essa abordagem permite uma recomendação personalizada, sugerindo produtos que são semanticamente semelhantes aos comprados anteriormente pelo usuário, e evita recomendar produtos que o usuário já possui. É uma técnica eficaz para melhorar a experiência do usuário em sistemas de recomendação, utilizando a semântica dos produtos para encontrar itens relevantes.
'''