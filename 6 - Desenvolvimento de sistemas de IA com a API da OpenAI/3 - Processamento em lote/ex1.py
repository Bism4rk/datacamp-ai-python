from openai import OpenAI
# Import the tenacity library
from tenacity import (retry, wait_random_exponential, stop_after_attempt)

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Add the appropriate parameters to the decorator
@retry(wait=wait_random_exponential(min=5, max=40), stop=stop_after_attempt(4))
def get_response(model, message):
    response = client.chat.completions.create(
      model=model,
      messages=[message]
    )
    return response.choices[0].message.content
print(get_response("gpt-4o-mini", {"role": "user", "content": "List ten holiday destinations."}))

'''
O código acima é um exemplo de como usar a biblioteca tenacity para implementar uma lógica de repetição com espera exponencial aleatória em caso de falhas ao chamar a API da OpenAI. A função `get_response` tenta obter uma resposta do modelo GPT-4o-mini, e se falhar, ela será reexecutada até quatro vezes, com um tempo de espera que varia entre 5 e 40 segundos entre as tentativas.
'''