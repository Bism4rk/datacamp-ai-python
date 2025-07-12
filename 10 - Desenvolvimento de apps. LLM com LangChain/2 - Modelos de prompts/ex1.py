from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# Create a prompt template from the template string
template = "You are an artificial intelligence assistant, answer the question. {question}"
prompt = PromptTemplate.from_template(
    template=template
)

llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')	

# Create a chain to integrate the prompt template and LLM
llm_chain = prompt | llm

# Invoke the chain on the question
question = "How does LangChain make LLM application development easier?"
print(llm_chain.invoke({"question": question}))

'''
O código acima mostra como criar um modelo de prompt usando LangChain e integrá-lo com um modelo de linguagem (LLM) para responder a perguntas. O modelo de prompt é definido com um template que inclui um espaço reservado para a pergunta. Em seguida, o modelo de linguagem é configurado para usar o modelo GPT-4o-mini da OpenAI. Finalmente, uma cadeia (cadeia é um termo usado em LangChain para descrever a sequência de operações) é criada para combinar o modelo de prompt e o modelo de linguagem, permitindo que a pergunta seja respondida de forma estruturada. A saída do código será a resposta gerada pelo modelo de linguagem para a pergunta fornecida.
'''

