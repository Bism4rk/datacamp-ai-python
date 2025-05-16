
'''
# Filter the documents
filtered = wikipedia.filter(lambda row: "football" in row["text"])

# Create a sample dataset
example = filtered.select(range(1))

print(example[0]["text"])
'''

'''
O código acima mostra como filtrar um conjunto de dados específico do Hugging Face, neste caso, o conjunto de dados "wikipedia".

A variável 'filtered' contém o conjunto de dados filtrado, onde apenas os documentos que contêm a palavra "football" no texto são selecionados. A função 'filter' é utilizada para aplicar essa condição de filtragem.
A variável 'example' contém um subconjunto do conjunto de dados filtrado, onde apenas a primeira amostra é selecionada. A função 'select' é utilizada para selecionar as amostras desejadas.
A última linha imprime o texto da primeira amostra do conjunto de dados filtrado.
'''