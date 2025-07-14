
customers = {
    "name": ["Peak Performance Co.", "Tech Innovators Inc.", "Green Solutions Ltd."],
    "industry": ["Fitness", "Technology", "Environmental"],
    "location": ["New York", "San Francisco", "Seattle"],
    "revenue": [500000, 1200000, 800000]
}

# Define a function to retrieve customer info by-name
def retrieve_customer_info(name: str) -> str:
    """Retrieve customer information based on their name."""
    # Filter customers for the customer's name
    customer_info = customers[customers['name'] == name]
    return customer_info.to_string()
  
# Call the function on Peak Performance Co.
print(retrieve_customer_info("Peak Performance Co."))

'''
O código acima mostra como criar uma função que recupera informações de clientes com base no nome, que será usada para criar um agente React personalizado com LangChain. A função filtra um dicionário de clientes e retorna as informações correspondentes ao nome fornecido. A saída é formatada como uma string para fácil leitura.
'''