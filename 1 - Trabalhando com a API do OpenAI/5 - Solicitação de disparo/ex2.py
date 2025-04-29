from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Add the example to the prompt
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Love these! = 5 
2. Unbelievably good! =
3. Shoes fell apart on the second use. =
4. The shoes look nice, but they aren't very comfortable. =
5. Can't wait to show them off! = """
# O love these e os sinais de igual foram colocados no lugar de ____

response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}], max_completion_tokens=100)
print(response.choices[0].message.content)

# O código acima é um exemplo de como usar a API do OpenAI para classificar sentimentos em uma lista de frases.
# O modelo gpt-4o-mini é utilizado para gerar a classificação de sentimentos, e o resultado é impresso na tela.
# Neste caso, há um exemplo para ajudar o modelo a entender o que se espera como resposta, o que se chama de "few-shot shot prompting"