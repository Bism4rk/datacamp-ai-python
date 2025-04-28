from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Create a detailed prompt
prompt = """ Please write a compelling product design for the SonicPro headphones, and highlight its key features: Active noise canceeling, a 40-hour battery life, and a foldable design.

Use a persuasive and engaging tone to attract audiophiles and people who exercise frequently, and keep everything in a single paragraph.
""" # O prompt foi criado para ser mais detalhado e específico, com o objetivo de gerar um texto mais envolvente e persuasivo.

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=200,
    temperature=1 # Max_completion_tokens e temperature foram inseridos para ajustar o número de tokens na resposta e a aleatoriedade da resposta, respectivamente
)

print(response.choices[0].message.content)

# O código acima faz uma solicitação à API da OpenAI para gerar um texto persuasivo sobre os fones de ouvido SonicPro, destacando suas principais características.
# A resposta gerada pela API é impressa no console.
# O texto deve ser envolvente e atrativo para audiophiles e pessoas que se exercitam com frequência.