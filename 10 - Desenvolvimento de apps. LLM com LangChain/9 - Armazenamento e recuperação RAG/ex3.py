from langchain.chat_models import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.runnables import RunnablePassthrough
from ex2 import prompt_template
import os

docs = PyPDFLoader('rag_vs_fine_tuning.pdf').load()

llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

vectorstore = Chroma.from_documents(
    docs,
    embedding=OpenAIEmbeddings(api_key='<OPENAI_API_TOKEN>', model='text-embedding-3-small'),
    persist_directory=os.getcwd()
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)

# Create a chain to link retriever, prompt_template, and llm
rag_chain = ({"context": retriever, "question": RunnablePassthrough()}
            | prompt_template
            | llm)

# Invoke the chain
response = rag_chain.invoke("Which popular LLMs were considered in the paper?")
print(response.content)

'''
O código acima mostra como implementar um sistema de Recuperação de Resposta Aumentada (RAG) usando a biblioteca LangChain. Ele:
- Carrega um documento PDF usando `PyPDFLoader`.
- Cria um modelo de linguagem com `ChatOpenAI`.
- Armazena os documentos em um banco de dados vetorial Chroma, usando `OpenAIEmbeddings` para incorporar os textos.
- Configura um recuperador para buscar documentos relevantes com base na similaridade.
- Cria uma cadeia que combina o recuperador, um modelo de prompt e o modelo de linguagem.
- Invoca a cadeia com uma pergunta específica, retornando a resposta gerada pelo modelo de linguagem.
O resultado final é um sistema que pode responder perguntas baseadas no conteúdo do documento PDF, utilizando técnicas de RAG para melhorar a precisão e relevância das respostas.
'''