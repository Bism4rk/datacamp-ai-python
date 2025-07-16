# Import the character splitter
from langchain_text_splitters import CharacterTextSplitter

quote = 'Words are flowing out like endless rain into a paper cup,\nthey slither while they pass,\nthey slip away across the universe.'
chunk_size = 24
chunk_overlap = 10

# Create an instance of the splitter class
splitter = CharacterTextSplitter(
    chunk_size = chunk_size,
    chunk_overlap = chunk_overlap,
    separator = '\n'
)

# Split the string and print the chunks
docs = splitter.split_text(quote)
print(docs)
print([len(doc) for doc in docs])

'''
O código acima mostra como usar o `CharacterTextSplitter` da biblioteca LangChain para dividir uma string em pedaços menores. O texto é dividido com base no tamanho do chunk (`chunk_size`) e na sobreposição entre os chunks (`chunk_overlap`). O separador utilizado é a quebra de linha (`\n`). Após a divisão, os pedaços resultantes são impressos, assim como o comprimento de cada pedaço.
'''