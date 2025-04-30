from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

# Create a request to the Chat Completions endpoint
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": sys_msg},
    {"role": "user", "content": "Help me learn to make origami."}
  ]
)

print(response.choices[0].message.content)

# Novamente, esse código usa a função system para guiar a resposta do modelo
# Nesse caso, o prompt da função funciona como um guardrail, impedindo que o modelo fale sobre tópicos não relacionados à linguagens