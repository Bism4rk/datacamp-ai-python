from transformers import pipeline

text = "AI-powered robots assist in complex brain surgeries with precision."

# Create the pipeline
classifier = pipeline(task="zero-shot-classification", model="facebook/bart-large-mnli")

# Create the categories list
categories = ["politics", "science", "sports"]

# Predict the output
output = classifier(text, categories)

# Print the top label and its score
print(f"Top Label: {output['labels'][0]} with score: {output['scores'][0]}")

'''
O código acima é um exemplo de atribuição dinâmica de rótulos a um texto usando a biblioteca Transformers do Hugging Face. Neste caso, o modelo utilizado é "facebook/bart-large-mnli", que é um modelo pré-treinado para a tarefa de classificação zero-shot (sem treinamento prévio) com base em múltiplas categorias.
A classificação zero-shot permite que o modelo atribua rótulos a um texto sem ter sido treinado especificamente para essas categorias. O modelo retorna o rótulo mais provável e sua pontuação associada.
O texto "AI-powered robots assist in complex brain surgeries" é classificado como pertencente à categoria "science" com uma pontuação de 0.95, indicando uma alta confiança na classificação.
'''