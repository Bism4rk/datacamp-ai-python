from openai import OpenAI

message_listing = [{'role': 'system', 'content': "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous."}, {'role': 'user', 'content': 'Step into this beautiful two-story, single-family home located in Springfield, USA, priced at $350,000. This charming property features 4 bedrooms, 2.5 bathrooms, a spacious living room with a cozy fireplace, a modern kitchen with stainless steel appliances, and a large backyard perfect for family gatherings. The master bedroom includes an en-suite bathroom and a walk-in closet. Enjoy the convenience of an attached two-car garage and a recently updated HVAC system. Located near top-rated schools, parks, and shopping centers, this home is ideal for families looking for comfort and convenience.'}]

function_definition =[{'type': 'function', 'function': {'name': 'real_estate_info', 'description': 'Get the information about homes for sale from the body of the input text', 'parameters': {'type': 'object', 'properties': {'home type': {'type': 'string', 'description': 'Home type'}, 'location': {'type': 'string', 'description': 'Location'}, 'price': {'type': 'integer', 'description': 'Price'}, 'bedrooms': {'type': 'integer', 'description': 'Number of bedrooms'}}}}}]

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response= client.chat.completions.create(
    model="gpt-4o-mini",
    # Add the message
    messages=message_listing,
    # Add your function definition
    tools=function_definition
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

'''
O código acima é um exemplo da extração de dados estruturados de um texto usando a API da OpenAI. Ele define uma mensagem de entrada que descreve uma propriedade imobiliária e uma definição de função que especifica os dados que queremos extrair, como tipo de casa, localização, preço e número de quartos. A API é chamada com essas informações, e a resposta é impressa, mostrando os dados extraídos em um formato estruturado. A variável response usa o parâmetro tools para especificar a função que será usada para processar a mensagem de entrada e extrair as informações desejadas.
'''