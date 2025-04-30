from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
        {"role": "user", "content": "Give me a quick summary of France."},
        {"role": "assistant", "content": "France is a country in Europe which borders Spain, Andorra, Italy, Switzerland, and Belgium. Its capital city is Paris."},
        {"role": "user", "content": "Give me a quick summary of Greece."}
    ]
)

print(response.choices[0].message.content)

# O código acima mostra como as funções system e assistant ajuda a guiar os resultados gerados por um modelo.
# No caso, o prompt system diz como o modelo deve agir, e a dupla user/assistant dá um exemplo de questão e resposta respectivamente.