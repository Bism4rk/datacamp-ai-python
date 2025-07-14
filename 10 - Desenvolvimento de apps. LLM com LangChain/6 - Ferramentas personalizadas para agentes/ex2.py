from langchain.tools import tool
import pandas as pd

customers = pd.DataFrame({
    "name": ["Peak Performance Co.", "Tech Innovators Inc.", "Green Solutions Ltd."],
    "industry": ["Fitness", "Technology", "Environmental"],
    "location": ["New York", "San Francisco", "Seattle"],
    "revenue": [500000, 1200000, 800000]
})

# Convert the retrieve_customer_info function into a tool
@tool
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Print the tool's arguments
print(retrieve_customer_info.args)

'''
O código acima mostra como converter uma função que recupera informações de clientes em uma ferramenta usando LangChain. A função filtra um DataFrame de clientes e retorna as informações correspondentes ao nome fornecido. A saída é formatada como uma string para fácil leitura. A ferramenta pode ser usada em um agente React personalizado.
'''