from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

marketing_message = "Introducing our latest collection of premium leather handbags. Each bag is meticulously crafted using the finest leather, ensuring durability and elegance. With a variety of designs and colors, our handbags are perfect for any occasion. Shop now and experience the epitome of style and quality."

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

# Craft a prompt that translates
prompt = f"""Translate the English text delimited by triple backticks to French, Spanish, and Japanese:
```{marketing_message}```"""
 
response = get_response(prompt)

print("English:", marketing_message)
print(response)

'''
O código acima é um exemplo de transformação, e especificamente tradução de texto. O prompt pede que o modelo traduza um texto em inglês para francês, espanhol e japonês.
'''