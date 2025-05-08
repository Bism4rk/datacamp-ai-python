from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=1500,
        n=1,
        stop=None
    )
    return response.choices[0].message['content']

text = "something here idk man"

# Craft a prompt to transform the text
prompt = f"""Transform the text delimited by triple backticks with the following steps:
Step 1 - Proofread it without changing its structure
Step 2 - Change the tone to be formal and friendly
```{text}```
"""

response = get_response(prompt)

print("Before transformation:\n", text)
print("After transformation:\n", response)

'''
O código acima é um exemplo de transformação de texto por meio de prompts multi-step, pedindo que o modelo primeiro só revise o texto e depois mude o seu tom para ser formal e amigável.
'''