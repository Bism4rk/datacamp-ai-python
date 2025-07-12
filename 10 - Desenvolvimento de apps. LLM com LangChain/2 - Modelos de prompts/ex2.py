from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

# Create a chat prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a geography expert that returns the colors present in a country's flag."),
        ("human", "France"),
        ("ai", "blue, white, red"),
        ("human", "{country}")
    ]
)

# Chain the prompt template and model, and invoke the chain
llm_chain = prompt_template | llm

country = "Japan"
response = llm_chain.invoke({"country": country})
print(response.content)

'''
O código acima mostra como criar um modelo de prompt de chat com mensagens de sistema, humano e IA usando LangChain. O modelo de linguagem é configurado para usar o modelo GPT-4o-mini da OpenAI. O modelo de prompt é definido com mensagens que especificam o papel do sistema, a pergunta do humano e a resposta esperada da IA. Em seguida, uma cadeia é criada para combinar o modelo de prompt e o modelo de linguagem, permitindo que a pergunta sobre as cores da bandeira do Japão seja respondida de forma estruturada. A saída do código será a resposta gerada pelo modelo de linguagem para a pergunta fornecida.
'''