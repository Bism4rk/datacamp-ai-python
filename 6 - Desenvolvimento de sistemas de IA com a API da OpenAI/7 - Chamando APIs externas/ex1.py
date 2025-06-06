from openai import OpenAI

def get_response(function_definition):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=[{'role': 'user', 'content': "What is the airport code for Los Angeles?"}],
        functions=function_definition,
        function_call={'name': 'get_airport_info'}
    )
    return response.choices[0].message


client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Define the function to pass to tools

function_definition = [{"type": "function",

                        "function" : {"name": "get_airport_info",

                                "description": "This function calls the AviationAPI and returns a corresponding airport code",

                                "parameters": {"type": "object", "properties": {"airport_code": {"type": "string", "description": "The airport code to the passed to the get_airport_info function."}} }, 

                                "result": {"type": "string"} }}]



response = get_response(function_definition)

print(response)

'''
O código acima demonstra como chamar uma API externa usando a OpenAI API. Ele define uma função chamada `get_airport_info` que busca o código do aeroporto de Los Angeles. A função é passada como parte da definição de ferramentas para o modelo, que então pode chamar essa função para obter a informação solicitada. A resposta do modelo é impressa no final.

'''