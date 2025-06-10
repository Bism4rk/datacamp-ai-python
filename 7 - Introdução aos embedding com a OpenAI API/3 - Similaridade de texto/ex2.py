from openai import OpenAI

client = OpenAI(api_key="<INSERT API KEY HERE>")

short_description = "The latest flagship smartphone with AI-powered features and 5G connectivity."
list_of_descriptions = ['Charge your devices conveniently with this sleek wireless charging dock.', 'Elevate your skincare routine with this luxurious skincare set.']



# Define a create_embeddings function
def create_embeddings(texts):
  response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
  )
  response_dict = response.model_dump()
  
  return [data['embedding'] for data in response_dict['data']]

# Embed short_description and print
print(create_embeddings(short_description)[0])

# Embed list_of_descriptions and print
print(create_embeddings(list_of_descriptions))

'''
O código acima é um exemplo de como usar a OpenAI API para criar embeddings de texto. Ele define uma função `create_embeddings` que recebe uma lista de textos e retorna os embeddings correspondentes. Essa função é usada para gerar embeddings tanto para uma descrição curta quanto para uma lista de descrições. Os embeddings são impressos no console, permitindo que você veja as representações vetoriais dos textos fornecidos.
'''