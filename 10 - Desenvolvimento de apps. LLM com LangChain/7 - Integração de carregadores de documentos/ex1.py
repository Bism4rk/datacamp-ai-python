# Import library
from langchain_community.document_loaders import PyPDFLoader

# Create a document loader for rag_vs_fine_tuning.pdf
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')

# Load the document
data = loader.load()
print(data[0])

'''
O código acima mostra como criar um carregador de documentos usando a biblioteca LangChain para carregar um arquivo PDF chamado "rag_vs_fine_tuning.pdf". O carregador é criado com a classe `PyPDFLoader`, e o método `load()` é usado para carregar o conteúdo do PDF. O primeiro elemento do documento carregado é impresso na tela.
'''