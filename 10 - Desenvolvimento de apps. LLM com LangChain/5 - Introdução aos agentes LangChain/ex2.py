from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key='your_api_key_here')

# Define the tools
tools = load_tools(["wikipedia"])

# Define the agent
agent = create_react_agent(llm, tools)

# Invoke the agent
response = agent.invoke({"messages": [("human", "How many people live in New York City?")]})
print(response['messages'][-1].content)

'''
O código acima mostra como criar um agente React usando LangChain. Após a importação das bibliotecas necessárias, um modelo de linguagem é instanciado com a chave da API. Em seguida, as ferramentas são carregadas, neste caso, a ferramenta de busca na Wikipedia (que necessita a instalação do pacote `wikipedia`). Com isso feito, um agente React é criado utilizando o modelo de linguagem e as ferramentas definidas. Por fim, o agente é invocado com uma pergunta sobre a população de Nova York, e a resposta é impressa.
'''