from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

prompt = """Replace Josh with Mary and adjust phrase: 
            Josh is a software engineer with a passion for developing innovative solutions to complex problems. He has a strong background in computer science and has worked on various projects ranging from web development to machine learning applications. Josh enjoys collaborating with teams and is always eager to learn new technologies."""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens= 300
)

input_token_price = 0.15 / 1_000_000 # _ pode ser usado para separar os números, mas não é necessário
output_token_price = 0.6 / 1_000_000
max_completion_tokens= 300

# Extract token usage
input_tokens = response.usage.prompt_tokens # usage e prompt_tokens foram inseridos no lugar de ____
output_tokens = max_completion_tokens
# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price) # output_tokens e output_token_price foram inseridos no lugar de ____
print(f"Estimated cost: ${cost}")

# O código acima calcula o custo estimado de uma solicitação à API da OpenAI, considerando o número de tokens de entrada e saída.
# O custo é calculado com base nos preços de tokens de entrada e saída definidos no código.
# O resultado é impresso no console.
