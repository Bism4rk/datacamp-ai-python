from transformers import pipeline

modelId = "distilbert-base-uncased-finetuned-sst-2-english"

my_pipeline = pipeline("text-classification", 
                        model=modelId)

my_pipeline.save_pretrained(f"models/{modelId}")

# Reload the saved model
reloaded_pipeline = pipeline("text-classification", model=f"models/{modelId}")

# Test the reloaded model
print(reloaded_pipeline("Hugging Face is great!"))

'''
O código acima mostra como salvar e recarregar um modelo pré-treinado do Hugging Face usando a biblioteca Transformers.
O modelo utilizado é o "distilbert-base-uncased-finetuned-sst-2-english", que é um modelo de classificação de texto.
O modelo é carregado automaticamente do Hugging Face Hub e um pipeline é criado para a tarefa de classificação de texto.
Neste caso, o modelo é salvo em um diretório local chamado "models" e, em seguida, recarregado a partir desse diretório.
O pipeline recarregado é testado com uma frase de exemplo, e o resultado da classificação é impresso.
'''