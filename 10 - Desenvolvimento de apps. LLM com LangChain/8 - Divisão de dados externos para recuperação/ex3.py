from langchain_community.document_loaders import UnstructuredHTMLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load the HTML document into memory
loader = UnstructuredHTMLLoader('white_house_executive_order_nov_2023.html')
data = loader.load()

# Define variables
chunk_size = 300
chunk_overlap = 100

# Split the HTML
splitter = RecursiveCharacterTextSplitter(
    chunk_size=chunk_size,
    chunk_overlap=chunk_overlap,
    separators='.')

docs = splitter.split_documents(data)
print(docs)

'''
O código acima mostra como dividir um documento HTML carregado em pedaços menores usando o `RecursiveCharacterTextSplitter` da biblioteca LangChain. O carregador `UnstructuredHTMLLoader` é usado para carregar o conteúdo do HTML, e o `RecursiveCharacterTextSplitter` divide o documento em pedaços com base no tamanho do chunk (`chunk_size`) e na sobreposição entre os chunks (`chunk_overlap`). Os separadores utilizados são pontos ('.'). Após a divisão, os pedaços resultantes são impressos.
'''