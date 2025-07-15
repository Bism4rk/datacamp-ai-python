from langchain_community.document_loaders import UnstructuredHTMLLoader

# Create a document loader for unstructured HTML
loader = UnstructuredHTMLLoader('white_house_executive_order_nov_2023.html')

# Load the document
data = loader.load()

# Print the first document
print(data[0])

# Print the first document's metadata
print(data[0].metadata)

'''
O código acima mostra como criar um carregador de documentos usando a biblioteca LangChain para carregar um arquivo HTML não estruturado. O carregador é criado com a classe `UnstructuredHTMLLoader`, e o método `load()` é usado para carregar o conteúdo do HTML. O primeiro elemento do documento carregado é impresso na tela, assim como os metadados do primeiro documento.
'''