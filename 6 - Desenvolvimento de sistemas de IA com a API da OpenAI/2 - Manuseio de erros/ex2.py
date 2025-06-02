from openai import OpenAI, openai

message = "What is the FitnessGram Pacer Test?"

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Use the try statement
try:
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[message]
    )
    # Print the response
    print(response.choices[0].message.content)
# Use the except statement
except openai.AuthenticationError:
    print("Please double check your authentication key and try again, the one provided is not valid.")


'''
O código acima é um exemplo de como lidar com erros ao fazer uma solicitação à API da OpenAI. Usando blocos try e except, o código tenta fazer uma solicitação de chat e, se ocorrer um erro de autenticação, imprime uma mensagem amigável ao usuário. Isso é útil para evitar que o programa falhe silenciosamente ou exiba mensagens de erro técnicas que podem ser confusas para usuários não técnicos.
'''