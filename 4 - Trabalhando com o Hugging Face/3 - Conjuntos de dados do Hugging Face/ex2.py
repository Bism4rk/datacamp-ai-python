# Import the function to load dataset metadata
from datasets import load_dataset

# Load the "test" split of the TIGER-Lab/MMLU-Pro dataset
my_dataset = load_dataset("TIGER-Lab/MMLU-Pro", split="test")

# Display dataset details
print(my_dataset)

'''
O código acima mostra como carregar e exibir informações sobre um conjunto de dados específico do Hugging Face, neste caso, o conjunto de dados "MMLU-Pro".

O código utiliza a função `load_dataset` da biblioteca `datasets` para carregar o conjunto de dados "TIGER-Lab/MMLU-Pro" e o divide em partes, neste caso, a parte de teste. Após isso, ele exibe os detalhes do conjunto de dados, incluindo o número de amostras, o número de colunas e o tamanho do conjunto de dados em bytes.
'''