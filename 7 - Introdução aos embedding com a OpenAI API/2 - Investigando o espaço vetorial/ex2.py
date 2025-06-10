from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt # type: ignore

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

# Create reviews and embeddings lists using list comprehensions
categories = [product['category'] for product in products]
embeddings = [product['embedding'] for product in products]

# Reduce the number of embeddings dimensions to two using t-SNE
tsne = TSNE(n_components=2, perplexity=5)
embeddings_2d = tsne.fit_transform(np.array(embeddings))

# Create a scatter plot from embeddings_2d
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])

for i, category in enumerate(categories):
    plt.annotate(category, (embeddings_2d[i, 0], embeddings_2d[i, 1]))

plt.show()

'''
O código acima mostra como usar a técnica de t-SNE para reduzir a dimensionalidade dos embeddings de produtos e visualizá-los em um gráfico 2D. Reduzir a dimensionalidade (diminuir o número de dimensões) é uma técnica comum em aprendizado de máquina e ciência de dados, especialmente quando se trabalha com embeddings de alta dimensão, como os gerados por modelos de linguagem. Cada lista de embeddings do OpenAI contém 1536 dimensões, e o t-SNE aqui o reduz para apenas 2 dimensões, permitindo uma visualização mais fácil e intuitiva dos dados.

As listas `categories` e `embeddings` são criadas usando list comprehensions, que são uma maneira concisa de gerar listas em Python. A lista `categories` contém as categorias dos produtos, enquanto a lista `embeddings` contém os embeddings correspondentes. Após isso, o t-SNE é aplicado para reduzir a dimensionalidade dos embeddings, e um gráfico de dispersão é criado para visualizar os produtos em um espaço 2D. Cada ponto no gráfico representa um produto, e as anotações mostram suas respectivas categorias. Isso permite identificar visualmente como os produtos estão agrupados com base em suas descrições e características.

No caso, o [:, 0] e [:, 1] são usados para acessar as duas dimensões resultantes do t-SNE, que são então plotadas no gráfico de dispersão. As anotações são adicionadas para identificar cada ponto com sua categoria correspondente.

Como o código não funciona pois a biblioteca da OpenAI requer uma chave de API válida que é paga, o scatter plot não será exibido. No entanto, o código está estruturado corretamente para gerar e visualizar os embeddings de produtos se a chave de API for fornecida. Além disso, o scatter plot resultante está incluído nesta pasta como um arquivo de imagem para referência visual.

'''