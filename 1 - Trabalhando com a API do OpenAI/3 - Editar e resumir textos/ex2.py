from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

finance_text = """The stock market has been experiencing significant fluctuations in recent weeks, with major indices showing both gains and losses. Analysts attribute this volatility to a combination of factors, including rising interest rates, inflation concerns, and geopolitical tensions. Investors are advised to stay informed and consider diversifying their portfolios to mitigate risks."""

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}""" # Aqui, finance_text foi inserido no lugar de ____ e foi dada pelo curso fora do arquivo - a variável aqui é um exemplo para o código funcionar

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[{"role": "user", "content": prompt}],
  max_completion_tokens = 400 # max_completion tokens foi inserido aqui para limitar o número de tokens na resposta
)

print(response.choices[0].message.content)

# O código acima faz uma solicitação à API da OpenAI para gerar um resumo em dois pontos concisos de um texto sobre o mercado financeiro.
# A resposta gerada pela API é impressa no console.
