from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
import os

loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

# Split the document using RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 50
)
docs = splitter.split_documents(data) 

# Embed the documents in a persistent Chroma vector database
embedding_function = OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small')
vectorstore = Chroma.from_documents(
    docs,
    embedding=embedding_function,
    persist_directory=os.getcwd()
)

# Configure the vector store as a retriever
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

'''
O código acima mostra como carregar um documento PDF, dividi-lo em pedaços menores usando o `RecursiveCharacterTextSplitter`, e armazenar esses pedaços em um banco de dados vetorial persistente Chroma. Ele:
- Carrega o PDF usando `PyPDFLoader`.
- Divide o documento em pedaços menores com um tamanho de chunk de 300 caracteres e uma sobreposição de 50 caracteres.
- Cria uma função de incorporação usando `OpenAIEmbeddings` com um token de API OpenAI.
- Armazena os documentos incorporados em um banco de dados Chroma, que é persistente no diretório atual.
- Configura o banco de dados vetorial como um recuperador, permitindo buscas por similaridade com os parâmetros especificados.
O resultado final é um sistema que pode recuperar pedaços relevantes do documento com base em consultas, facilitando a recuperação de informações de forma eficiente.
'''