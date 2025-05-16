# Import the function to load dataset metadata
from datasets import load_dataset_builder

# Initialize the dataset builder for the MMLU-Pro dataset
reviews_builder = load_dataset_builder("TIGER-Lab/MMLU-Pro")

# Display dataset metadata
print(reviews_builder.info)

# Calculate and print the dataset size in MB
dataset_size_mb = reviews_builder.info.dataset_size / (1024 ** 2)
print(f"Dataset size: {round(dataset_size_mb, 2)} MB")


'''
O código acima mostra como carregar e exibir informações sobre um conjunto de dados específico do Hugging Face, neste caso, o conjunto de dados "MMLU-Pro".

O código utiliza a função `load_dataset_builder` da biblioteca `datasets` para inicializar um construtor de conjunto de dados para o conjunto de dados "TIGER-Lab/MMLU-Pro". Após isso, ele exibe as informações do conjunto de dados, incluindo o número de amostras, o número de colunas e o tamanho do conjunto de dados em bytes. O tamanho do conjunto de dados é convertido para megabytes (MB) e impresso na tela.
'''

# Esse código realmente funciona, ao contrário dos de modelos.