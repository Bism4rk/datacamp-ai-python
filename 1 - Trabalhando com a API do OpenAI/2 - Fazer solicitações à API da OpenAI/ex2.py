from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
  # Specify the model
  model="gpt-4o-mini", # O nome do modelo foi inserido no lugar de ____
  messages=[
    # Assign the correct role
    {"role": "user", # User foi inserido no lugar de ____
     "content": "Announce my new AI Engineer role on LinkedIn."}]
)

print(response.choices[0].message.content)