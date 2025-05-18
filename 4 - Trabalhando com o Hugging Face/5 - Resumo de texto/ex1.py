from transformers import pipeline

original_text = "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues. The 20 meter pacer test is a running test that measures a person's aerobic capacity. The test begins with the participant standing behind a line and running to the other side of the 20 meter distance when they hear a beep. The participant must reach the line before the next beep sounds. The time between beeps decreases as the test progresses, making it more challenging."

# Create the summarization pipeline
summarizer = pipeline(task="summarization", model="cnicu/t5-small-booksum")

# Summarize the text
summary_text = summarizer(original_text)

# Compare the length
print(f"Original text length: {len(original_text)}")
print(f"Summary length: {len(summary_text[0]['summary_text'])}")


'''
O código acima é um exemplo de como usar o Hugging Face Transformers para resumir um texto. Ele utiliza o modelo "cnicu/t5-small-booksum" para gerar um resumo do texto original. O código também imprime o comprimento do texto original e do resumo gerado, permitindo comparar os tamanhos dos dois textos.
'''