from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define a multi-line prompt to classify sentiment
prompt = """Classify the following reviews for an online shoe store called Toe-Tally Comfortable from 1 to 5, 1 being very bad and 5 very good: 
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!"""

# A primeira parte do prompt foi inserida por mim 

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}], # prompt foi colocado aqui por mim no lugar de ___
  max_completion_tokens=100
)

print(response.choices[0].message.content)

# O código acima utiliza a API da OpenAI para classificar sentimentos de avaliações de um produto (sapatos) em uma loja online chamada Toe-Tally Comfortable.
# O prompt contém quatro avaliações, e o modelo GPT-4o-mini é solicitado a classificá-las de 1 a 5, onde 1 é muito ruim e 5 é muito bom.
