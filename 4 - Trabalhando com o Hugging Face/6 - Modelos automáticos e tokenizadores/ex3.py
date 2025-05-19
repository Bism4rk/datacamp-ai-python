from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

# Download the model and tokenizer
my_model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
my_tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

# Create the pipeline
my_pipeline = pipeline(task="sentiment-analysis", model=my_model, tokenizer=my_tokenizer)

# Predict the sentiment
output = my_pipeline("This course is pretty good, I guess.")
print(f"Sentiment using AutoClasses: {output[0]['label']}")

'''
O código acima é mais um exemplo do uso de classes Auto - o modelo e o tokenizador são inicializados por meio da função `from_pretrained`, que baixa o modelo e o tokenizador do repositório do Hugging Face. O pipeline é criado com a função `pipeline`, que permite realizar tarefas de PNL de forma simples e rápida. A função `sentiment-analysis` é utilizada para análise de sentimentos, e o resultado é impresso na tela.
'''