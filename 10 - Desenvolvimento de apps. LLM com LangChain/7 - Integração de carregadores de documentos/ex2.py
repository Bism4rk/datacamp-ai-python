# Import library
from langchain_community.document_loaders.csv_loader import CSVLoader

# Create a document loader for fifa_countries_audience.csv
loader = CSVLoader('fifa_countries_audience.csv')

# Load the document
data = loader.load()
print(data[0])

'''
O código acima mostra como criar um carregador de documentos usando a biblioteca LangChain para carregar um arquivo CSV em Python. O carregador é criado com a classe `CSVLoader`, e o método `load()` é usado para carregar o conteúdo do CSV. O primeiro elemento do documento carregado é impresso na tela.
'''