from pinecone import Pinecone, ServerlessSpec, itertools
from dotenv import load_dotenv
import os

def chunks(iterable, batch_size=100):
    """A helper function to break an iterable into chunks of size batch_size."""
    # Convert the iterable into an iterator
    it = iter(iterable)
    # Slice the iterator into chunks of size batch_size
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        # Yield the chunk
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

'''
O código acima mostra como dividir um vetor em pedaços menores (chunks) para processamento em lotes. A função `chunks` recebe um iterável e um tamanho de lote (`batch_size`) como parâmetros. Ela utiliza `itertools.islice` (uma função do módulo `itertools` que permite fatiar iteradores) para criar pedaços do iterável com o tamanho especificado. A função retorna um gerador que produz esses pedaços, permitindo que você processe grandes conjuntos de dados em partes menores, o que é útil para evitar problemas de memória e melhorar a eficiência do processamento.
'''