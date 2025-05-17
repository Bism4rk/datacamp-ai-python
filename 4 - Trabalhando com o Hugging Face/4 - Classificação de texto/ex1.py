from transformers import pipeline

# Create a pipeline for grammar checking
grammar_checker = pipeline(
  task="text-classification", 
  model="abdulmatinomotoso/English_Grammar_Checker"
)

# Check grammar of the input text
output = grammar_checker("I will walk dog")
print(output)

'''
O código acima é um exemplo de como usar a biblioteca Transformers do Hugging Face para verificar a gramática de um texto. A pipeline 'grammar_chcker' é criada para a tarefa de classificação de texto, utilizando o modelo "abdulmatinomotoso/English_Grammar_Checker".
O modelo é carregado automaticamente do Hugging Face Hub, e o pipeline é criado para a tarefa de verificação gramatical.
No caso, o código verifica a gramática da frase "I will walk dog" e imprime o resultado, que foi 'LABEL_0' e uma pontuação de 0.9999, indicando que a frase está quase certamente incorreta.
'''