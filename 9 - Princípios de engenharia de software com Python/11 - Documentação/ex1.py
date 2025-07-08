import re

text = "Our competitor pricing is $10.50 an inch. Our price is $125.00 a foot."


def extract_0(text):
    # match and extract dollar amounts from the text
    return re.findall(r'\$\d+\.\d\d', text)

def extract_1(text):
    # return all matches to regex pattern
    return re.findall(r'\$\d+\.\d\d', text)

# Print the text
print(text)

# Print the results of the function with better commenting
print(extract_1(text))

'''
O código acima utiliza expressões regulares para extrair valores monetários de um texto. A função `extract_1` é uma versão melhorada da função `extract_0`, pois inclui comentários mais claros e explicativos. Ambas as funções utilizam o método `findall` do módulo `re` para encontrar todas as ocorrências de valores monetários no formato "$X.XX" no texto fornecido.

Além disso, as duas funções são funcionalmente idênticas, mas a `extract_1` é preferível por sua clareza e legibilidade. O seu comentário explica que a função retorna todas as correspondências para o padrão regex, o que é útil para quem lê o código entender rapidamente o propósito da função.
'''