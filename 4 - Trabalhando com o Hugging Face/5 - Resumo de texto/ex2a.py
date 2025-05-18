from transformers import pipeline

original_text = "Greece is a country located in southeastern Europe, known for its rich history, stunning landscapes, and vibrant culture. It is often referred to as the cradle of Western civilization due to its significant contributions to art, philosophy, and politics. The country is famous for its ancient ruins, such as the Acropolis in Athens and the Palace of Knossos in Crete. Greece is also renowned for its beautiful islands, including Santorini and Mykonos, which attract millions of tourists each year. The Greek cuisine, characterized by its use of olive oil, fresh vegetables, and seafood, is another highlight of the country's culture."

# Create a short summarizer
short_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_length=1, max_length=10)

# Summarize the input text
short_summary_text = short_summarizer(original_text)

# Print the short summary
print(short_summary_text[0]["summary_text"])

# Repeat for a long summarizer
long_summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum", min_length=50, max_length=150)

long_summary_text = long_summarizer(original_text)

# Print the long summary
print(long_summary_text[0]["summary_text"])

'''
O código acima é um exemplo de como usar o Hugging Face Transformers para resumir um texto. Ele utiliza o modelo "cnicu/t5-small-booksum" para gerar resumos curtos e longos do texto original sobre a Grécia. O código imprime os resumos gerados, permitindo comparar as versões resumidas do texto.

Ambas as funções short_summarizer e long_summarizer utilizam o mesmo modelo, mas com diferentes parâmetros de comprimento mínimo e máximo para controlar o tamanho do resumo gerado. O resumo curto tem um comprimento máximo de 10 tokens, enquanto o resumo longo tem um comprimento máximo de 150 tokens.
'''

