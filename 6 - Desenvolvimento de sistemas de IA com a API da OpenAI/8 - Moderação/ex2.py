from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

message = "Can you show some example sentences in the past tense in French?"

# Use the moderation API
moderation_response = client.moderations.create(input=message)

# Print the response
print(moderation_response.results[0].categories)

'''
O código acima é um exemplo de como usar a API de moderação da OpenAI para verificar se uma mensagem contém conteúdo potencialmente problemático. Ele envia uma mensagem solicitando exemplos de frases no passado em francês e imprime as categorias de moderação retornadas pela API, que são usadas para identificar se o conteúdo é seguro ou não. A resposta pode incluir categorias como "violence" (violência), "hate" (ódio), "harassment" (assédio), entre outras, indicando se a mensagem é aceitável ou não de acordo com as diretrizes da OpenAI. No caso, a mensagem solicitada não deve conter conteúdo problemático, então as categorias devem indicar que é seguro.
'''