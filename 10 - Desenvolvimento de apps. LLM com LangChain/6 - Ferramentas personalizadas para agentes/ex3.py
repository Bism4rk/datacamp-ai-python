from langchain.tools import tool
import pandas as pd
from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini", api_key='your_api_key_here')

customers = pd.DataFrame({
    "name": ["Peak Performance Co.", "Tech Innovators Inc.", "Green Solutions Ltd."],
    "industry": ["Fitness", "Technology", "Environmental"],
    "location": ["New York", "San Francisco", "Seattle"],
    "revenue": [500000, 1200000, 800000]
})

@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()

# Create a ReAct agent
agent = create_react_agent(llm, [retrieve_customer_info])

# Invoke the agent on the input
messages = agent.invoke({"messages": [("human", "Create a summary of our customer: Peak Performance Co.")]})
print(messages['messages'][-1].content)

'''
O código acima mostra como criar um agente React personalizado usando LangChain e usá-lo. Primeiro, um modelo de linguagem é instanciado com a chave da API. Em seguida, um DataFrame de clientes é criado. A função `retrieve_customer_info` é definida para recuperar informações de clientes com base no nome, e essa função é convertida em uma ferramenta usando o decorador `@tool`. Um agente React é então criado utilizando o modelo de linguagem e a ferramenta definida. Por fim, o agente é invocado com uma mensagem solicitando um resumo do cliente "Peak Performance Co.", e a resposta é impressa.
'''