import re

# Complete the function's docstring
def tokenize(text, regex=r'[a-zA-z]+'):
  """Split text into tokens using a regular expression

  :param text: text to be tokenized
  :param regex: regular expression used to match tokens using re.findall 
  :return: a list of resulting tokens

  >>> tokenize('the rain in spain')
  ['the', 'rain', 'in', 'spain']
  """
  return re.findall(regex, text, flags=re.IGNORECASE)

# Print the docstring
help(tokenize)

'''
O código acima mostra como documentar uma função em Python usando docstrings. A função `tokenize` recebe um texto e uma expressão regular (regex) como parâmetros, e utiliza a função `re.findall` para dividir o texto em tokens com base na regex fornecida. A docstring explica os parâmetros da função, o que ela faz e fornece um exemplo de uso.
'''