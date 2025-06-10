from openai import OpenAI
# Initialize OpenAI client

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

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

# Extract a list of product short descriptions from products
product_descriptions = [product["short_description"] for product in products]

# Create embeddings for each product description
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=product_descriptions
)
response_dict = response.model_dump()

# Extract the embeddings from response_dict and store in products
for i, product in enumerate(products):
    product['embedding'] = response_dict['data'][i]['embedding']
    
print(products[0].items())

'''
O código acima demonstra como utilizar a API da OpenAI para criar embeddings de descrições de produtos. Primeiro, extraímos as descrições curtas dos produtos e, em seguida, solicitamos à API que gere embeddings para essas descrições usando o modelo "text-embedding-3-small". Os embeddings resultantes são então adicionados a cada produto no dicionário `products`, permitindo que cada produto tenha uma representação vetorial de sua descrição. 
'''