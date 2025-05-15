from transformers import pipeline

my_pipeline = pipeline(task="text-generation", model="gpt2")

# Generate three text outputs with a maximum length of 10 tokens
results = my_pipeline("How to", max_length=10, num_return_sequences=3)

# Display each result
for result in results:
    print(result['generated_text'])


'''
O código acima é um exemplo de como usar a biblioteca Transformers do Hugging Face para gerar texto usando o modelo GPT-2.
No caso, o modelo é carregado automaticamente do Hugging Face Hub, e o pipeline é criado para a tarefa de geração de texto.
O pipeline é uma abstração que facilita o uso de modelos pré-treinados para tarefas específicas, como classificação, tradução, geração de texto, entre outras.
'''

'''
Neste caso, o código não consegue gerar texto, pois o modelo "gpt2" não está disponível localmente e não foi feito o download do modelo.
'''