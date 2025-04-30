from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

response = client.chat.completions.create(
   model="gpt-4o-mini",
   # Add in the extra examples and responses
   messages=[
       {"role": "system", "content": "You are a helpful Geography tutor that generates concise summaries for different countries."},
       {"role": "user", "content": "Give me a quick summary of Portugal."},
       {"role": "assistant", "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa."},
       {"role": "user", "content": "Can you give me a quick summary of Brazil?"},
       {"role": "assistant", "content": "Sure! Brazil is a large, tropical country located in South America famous for its vibrant and varied culture and vibrant biodiversity. Its capital is Brasília."},
       {"role": "user", "content": "Give me a quick summary of the Vatican City."},
       {"role": "assistant", "content": "The Vatican city is a tiny European city-state located entirely within the Italian capital of Rome. It's famous for being where the Pope lives."},
       {"role": "user", "content": "Give me a quick summary of China."},
       {"role": "assistant", "content": "China is a large Asian country famous for its long history and rich cuisine, culture, and traditions, and has a wide variety of biomes within it too. Its capital is Beijing."},
       {"role": "user", "content": "Give me a quick summary of Greece."}
   ]
)

print(response.choices[0].message.content)

# Mesma coisa do exercício passado, mas com mais exemplos