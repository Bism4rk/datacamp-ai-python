import doctest
from collections import Counter

def sum_counters(counters):
    """Aggregate collections.Counter objects by summing counts

    :param counters: list/tuple of counters to sum
    :return: aggregated counters with counts summed

    >>> d1 = text_analyzer.Document('1 2 fizz 4 buzz fizz 7 8')
    >>> d2 = text_analyzer.Document('fizz buzz 11 fizz 13 14')
    >>> sum_counters([d1.word_counts, d2.word_counts])
    Counter({'fizz': 4, 'buzz': 2})
    """
    return sum(counters, Counter())

doctest.testmod()

'''
O código acima mostra como testar a funcionalidade de uma função com o uso de doctest. A função `sum_counters` recebe uma lista ou tupla de objetos `Counter` e retorna um novo `Counter` com as contagens somadas. O teste incluído verifica se a função retorna o resultado esperado ao somar os contadores de dois documentos de texto. A função `doctest.testmod()` executa os testes definidos na docstring da função `sum_counters`. Se os testes passarem, não haverá saída; caso contrário, serão exibidos erros detalhados indicando quais testes falharam. Isso é útil para garantir que a função se comporte conforme o esperado e para detectar regressões em futuras alterações de código.
'''