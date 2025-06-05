from openai import OpenAI

model = "gpt-3.5-turbo-0613"
messages = [
    {"role": "system", "content": "Apply the function and return the response."},
    {"role": "user", "content": "\nI recently purchased the TechCorp ProMax and I'm absolutely in love with its powerful processor. However, I think they could really improve the product by deciding to offer more color options.\n"}
] # exemplo gerado pelo copilot

function_definition = [
    {
        'type': 'function',
        'function': {
            'name': 'extract_review_info',
            'description': 'Extract product name, sentiment, features, and suggestions from the review.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'product': {'type': 'string', 'description': 'The product name'},
                    'sentiment': {'type': 'string', 'description': 'The overall sentiment of the review'},
                    'features': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of features mentioned in the review'},
                    'suggestions': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Suggestions for improvement'}
                },
                'required': ['product', 'sentiment', 'features', 'suggestions']
            }
        }
    }
] # exemplo gerado pelo copilot

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response= client.chat.completions.create(
    model=model,
    messages=messages,
    # Add the function definition
    tools = function_definition,
    # Specify the function to be called for the response
    tool_choice={'type': 'function',
        'function': {'name': 'extract_review_info'}}
)

# Print the response
print(response.choices[0].message.tool_calls[0].function.arguments)

'''
O código acima é mais um exemplo de como trabalhar com múltiplas funções na API da OpenAI. Ele define uma função para extrair informações de uma revisão de produto, como nome do produto, sentimento, características e sugestões. Neste caso, o parâmetro `tool_choice` é usado para especificar qual função deve ser chamada para gerar a resposta. A resposta da API inclui as informações extraídas da revisão do produto.
'''