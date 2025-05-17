from transformers import pipeline

# Create the pipeline
classifier = pipeline(task="text-classification", model="cross-encoder/qnli-electra-base")

# Predict the output
output = classifier("Where is the capital of France?, Brittany is known for its stunning coastline.")

print(output)

'''
O código acima é mais um exemplo de classificação de texto usando a biblioteca Transformers do Hugging Face. Neste caso, o modelo utilizado é "cross-encoder/qnli-electra-base", que é um modelo pré-treinado para a tarefa de classificação de texto QNLI - Question Natural Language Inference (inferência de Linguagem Natural de Perguntas), que determina se premissas respondem perguntas ou não.

Neste caso, o modelo retornou 'LABEL_0', indicando que a premissa não respondeu a pergunta.
'''