# Define Document class
class Document:
    """A class for text analysis
    
    :param text: string of text to be analyzed
    :ivar text: string of text to be analyzed; set by `text` parameter
    """
    # Method to create a new instance of MyClass
    def __init__(self, text):
        # Store text parameter to the text attribute
        self.text = text

'''
O código acima mostra como definir uma classe em Python. Nesse caso, a classe `Document` é usada para análise de texto. Ela possui um construtor (`__init__`) que recebe um parâmetro `text` e o armazena como um atributo da instância. O parâmetro self é usado para referenciar a instância atual da classe. A docstring da classe fornece uma descrição do que a classe faz e dos parâmetros que aceita, o que é útil para documentação e compreensão do código.
'''