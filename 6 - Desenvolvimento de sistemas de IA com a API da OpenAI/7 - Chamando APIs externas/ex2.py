from openai import OpenAI

def print_response(response):
    if response.choices and response.choices[0].message:
        if 'tool_calls' in response.choices[0].message:
            for tool_call in response.choices[0].message.tool_calls:
                print(f"Tool Call: {tool_call.function.name}")
                print(f"Arguments: {tool_call.function.arguments}")
        else:
            print("No tool calls found in the response.")
    else:
        print("No valid response received.") # gerado pelo copilot

def function_definition():
    return [{
        "type": "function",
        "function": {
            "name": "get_airport_info",
            "description": "This function calls the AviationAPI and returns a corresponding airport code",
            "parameters": {
                "type": "object",
                "properties": {
                    "airport_code": {
                        "type": "string",
                        "description": "The airport code to be passed to the get_airport_info function."
                    }
                }
            }
        }
    }] # gerado pelo copilot

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Call the Chat Completions endpoint 
response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are an AI assistant, an aviation specialist. You should interpret the user prompt, and based on it extract an airport code corresponding to their message."},
    {"role": "user", "content": "I'm planning to land a plane in JFK airport in New York and would like to have the corresponding information."}],
  tools=function_definition)

print_response(response)

'''
O código acima é mais um exemplo de como chamar uma API externa usando a OpenAI API. Ele define uma função chamada `get_airport_info` que busca o código do aeroporto de JFK em Nova York. A função é passada como parte da definição de ferramentas para o modelo, que então pode chamar essa função para obter a informação solicitada. A resposta do modelo é impressa no final, mostrando os detalhes da chamada da ferramenta e os argumentos passados. No parâmetro messages, uma mensagem do sistema é incluída para orientar o modelo sobre seu papel como assistente de aviação, ajudando a interpretar a solicitação do usuário e extrair o código do aeroporto correspondente.
'''