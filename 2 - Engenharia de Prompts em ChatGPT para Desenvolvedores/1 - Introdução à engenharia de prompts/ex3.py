from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

def get_response(prompt):
    print(prompt) # A função get_respone foi pré-carregada no código original, mas não foi inserida aqui, essa aqui é só um exemplo para que o programa não retornasse erro.

# O import, ger_response, e client não faziam parte do código original, mas foram adicionados para que o programa não retornasse erro.

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a prompt that follows the instructions
prompt = "Write a poem about ChatGPT in basic English that a young child can understand."

# Get the response
response = get_response(prompt) # A função get_respone foi pré-carregada no código original, mas não foi inserida aqui.

print(response)

'''
Aqui há um exemplo de engenharia de prompts, onde o prompt foi elaborado para que o modelo desse uma resposta melhor. Nesse caso, além de pedir um poema sobre o ChatGPT, como no exercício anterior, o prompt também pedia que o modelo escrevesse em inglês básico, para que uma criança pequena pudesse entender.
'''