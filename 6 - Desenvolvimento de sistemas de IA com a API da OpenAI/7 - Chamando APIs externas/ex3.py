''''
if response.choices[0].finish_reason=='tool_calls':
  function_call = response.choices[0].message.tool_calls[0].function
  # Check function name
  if function_call.name == "get_airport_info":
    # Extract airport code
    code = json.loads(function_call.arguments)["airport code"]
    airport_info = get_airport_info(code)
    print(airport_info)
  else:
    print("Apologies, I couldn't find any airport.")
else: 
  print("I am sorry, but I could not understand your request.")
'''

'''
O código acima é um exemplo de como lidar com a resposta de uma chamada de função na API da OpenAI. Ele verifica se a razão de término da escolha é 'tool_calls', o que indica que uma função foi chamada. Em seguida, ele extrai o nome da função e os argumentos passados. Se o nome da função for 'get_airport_info', ele extrai o código do aeroporto dos argumentos e chama a função `get_airport_info` para obter as informações correspondentes. Caso contrário, ele informa que não conseguiu encontrar nenhum aeroporto. Se a razão de término não for 'tool_calls', ele informa que não entendeu a solicitação.
'''