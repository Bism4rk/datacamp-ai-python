# load the Counter function into our environment
from collections import Counter
from words import words

# View the documentation for Counter.most_common
help(Counter.most_common)

# use Counter to find the top 5 most common words
top_5_words = Counter(words).most_common(5)

# display the top 5 most common words
print(top_5_words)

'''
O código acima mostra como podemos usar a função help para nos ajudar a entender como usar uma função específica do Python, neste caso, a função most_common do módulo Counter. A função most_common é usada para encontrar os elementos mais comuns em uma coleção, como uma lista ou um dicionário. A função most_common retorna uma lista de tuplas, onde cada tupla contém um elemento e sua contagem. No exemplo, estamos usando a função most_common para encontrar as 5 palavras mais comuns na lista words, que é importada do módulo words. A lista top_5_words contém as 5 palavras mais comuns e suas respectivas contagens.
'''