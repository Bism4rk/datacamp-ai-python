from openai import OpenAI

function_definition = [{'type': 'function', 'function': {'name': 'extract_sentiment_and_product_features', 'parameters': {'type': 'object', 'properties': {'product': {'type': 'string', 'description': 'The product name'}, 'sentiment': {'type': 'string', 'description': 'The overall sentiment of the review'}, 'features': {'type': 'array', 'items': {'type': 'string'}, 'description': 'List of features mentioned in the review'}, 'suggestions': {'type': 'array', 'items': {'type': 'string'}, 'description': 'Suggestions for improvement'}}}}}, {'type': 'function', 'function': {'name': 'reply_to_review', 'description': 'Return the additional message which replies to the client review', 'parameters': {'type': 'object', 'properties': {'reply': {'type': 'string', 'description': 'Reply'}}}}}]

messages = [{'role': 'system', 'content': 'Apply both functions and return responses.'}, {'role': 'user', 'content': "\nI recently purchased the TechCorp ProMax and I'm absolutely in love with its powerful processor. However, I think they could really improve the product by deciding to offer more color options.\n"}]
{"product": "TechCorp ProMax", "sentiment": "positive", "features": ["powerful processor"], "suggestions": ["offer more color options"]}

def get_response(messages, function_definition):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=function_definition,
        function_call={'name': 'extract_sentiment_and_product_features'}
    )
    return response.choices[0].message

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Append the second function
function_definition.append({'type': 'function', 
    'function':{
    'name': 'reply_to_review',
    'description': 'Return the additional message which replies to the client review', 
    'parameters': {
    'type': 'object', 
    'properties': {'reply': {'type': 'string', 'description': 'Reply'}}}}})

response = get_response(messages, function_definition)

# Print the response
print(response)

'''
O código acima é um exemplo de como trabalhar com várias funções na API da OpenAI. Ele define duas funções: uma para extrair o sentimento e as características do produto de uma revisão, e outra para responder à revisão do cliente. A primeira função é chamada automaticamente, enquanto a segunda é chamada manualmente após a primeira função ser executada.

# Após a execução, o código imprime a resposta da API, que inclui o sentimento, as características do produto e sugestões de melhoria, além de uma resposta ao cliente.
'''