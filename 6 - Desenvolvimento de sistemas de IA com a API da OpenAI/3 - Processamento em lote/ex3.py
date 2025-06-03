from openai import OpenAI
import tiktoken

client = OpenAI(api_key="<OPENAI_API_TOKEN>")
input_message = {"role": "user", "content": "I'd like to buy a shirt and a jacket. Can you suggest two color pairings for these items?"}

# Use tiktoken to create the encoding for your model
encoding = tiktoken.encoding_for_model("gpt-4o-mini")
# Check for the number of tokens
num_tokens = len(encoding.encode(input_message['content']))

# Run the chat completions function and print the response
if num_tokens <= 100:
    response = client.chat.completions.create(model="gpt-4o-mini", messages=[input_message])
    print(response.choices[0].message.content)
else:
    print("Message exceeds token limit")

'''
O código acima demonstra como usar a biblioteca `tiktoken` para contar o número de tokens em uma mensagem antes de enviá-la para a API da OpenAI. Ele verifica se o número de tokens na mensagem de entrada não excede 100, e se estiver dentro do limite, faz uma solicitação de chat completions ao modelo GPT-4o-mini. Caso contrário, imprime uma mensagem informando que a mensagem excede o limite de tokens. Isso ajuda a evitar bater em limites de tokens e garante que a solicitação seja válida antes de ser enviada à API.
'''