# Import necessary library for tokenization
from transformers import AutoTokenizer

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Split input text into tokens
tokens = tokenizer.tokenize("AI: Making robots smarter and humans lazier!")

# Display the tokenized output
print(f"Tokenized output: {tokens}")

'''
O código acima é um exemplo de AutoTokenizer do Hugging Face, que é uma ferramenta poderosa para tokenização de texto. O modelo utilizado é o "distilbert-base-uncased-finetuned-sst-2-english", que é uma versão reduzida do BERT, otimizada para tarefas de classificação de sentimentos. A função `tokenize` divide a frase de entrada em tokens, que são as unidades básicas de processamento de linguagem natural. O resultado é uma lista de tokens que representam a frase original.
'''