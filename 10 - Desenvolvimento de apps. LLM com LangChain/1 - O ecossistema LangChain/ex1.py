from langchain.chat_models import ChatOpenAI

# Define the LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key="<OPENAI_API_TOKEN>")

# Predict the words following the text in question
prompt = 'Three reasons for using LangChain for LLM application development.'
response = llm.invoke(prompt)

print(response.content)

'''
O código acima é um exemplo de uso do LangChain para desenvolvimento de aplicações com LLMs (Modelos de Linguagem de Grande Escala). Ele define um modelo de linguagem usando a classe `ChatOpenAI` do LangChain, especificando o modelo "gpt-4o-mini" e uma chave de API do OpenAI. Em seguida, ele cria um prompt com uma pergunta e invoca o modelo para obter uma resposta, que é impressa no console. Isso demonstra como o LangChain pode ser usado para interagir com modelos de linguagem e gerar respostas baseadas em prompts fornecidos. 

O LangChain é uma biblioteca que facilita a construção de aplicações que utilizam LLMs, permitindo a integração com diferentes provedores de modelos e simplificando o processo de desenvolvimento. 
'''