# Import the recursive character splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = RecursiveCharacterTextSplitter(
    separators = ["\n", " ", ""],
    chunk_size = chunk_size,
    chunk_overlap = chunk_overlap
)

# Split the document and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])

'''
O código acima demonstra como utilizar o `RecursiveCharacterTextSplitter` da biblioteca LangChain para dividir uma string em pedaços menores. O texto é dividido com base no tamanho do chunk (`chunk_size`) e na sobreposição entre os chunks (`chunk_overlap`). Os separadores utilizados incluem quebras de linha, espaços e strings vazias. Após a divisão, os pedaços resultantes são impressos, assim como o comprimento de cada pedaço. A diferença entre o `CharacterTextSplitter` e o `RecursiveCharacterTextSplitter` é que este último permite uma divisão mais flexível, utilizando múltiplos separadores (como é visto no exemplo com a list `separators`). 
'''