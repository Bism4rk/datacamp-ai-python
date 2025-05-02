from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>") 

# O import e o client não faziam parte do código original, mas foram adicionados para que o programa não retornasse erro.

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create( # chat.comptions.create foi inserido no lugar de ____
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

# Test the function with your prompt
response = get_response("Please write a poem with 6 stanzas about ChatGPT.") # O prompt foi inserido no lugar de ____
print(response)

