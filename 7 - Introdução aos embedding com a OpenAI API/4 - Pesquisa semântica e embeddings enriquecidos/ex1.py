from openai import OpenAI

client = OpenAI(api_key="API KEY HERE")

def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  
  return [data['embedding'] for data in response_dict['data']]

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


# Define a function to combine the relevant features into a single string
def create_product_text(product):
  return f"""Title: {product['title']}
Description: {product['short_description']}
Category: {product['category']}
Features: {product['features']}"""

# Combine the features for each product
product_texts = [create_product_text(product) for product in products]

# Create the embeddings from product_texts
product_embeddings = create_embeddings(product_texts)

'''
O código acima mostra como criar embeddings para uma lista de produtos, onde cada produto é representado por um dicionário contendo informações como título, descrição curta, preço, categoria e características. A função `create_product_text` combina essas informações em uma string formatada, que é então usada para gerar embeddings usando a função `create_embeddings`. Esses embeddings podem ser usados posteriormente para tarefas de similaridade ou busca semântica.
'''