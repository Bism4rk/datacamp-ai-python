from openai import OpenAI

def get_response(prompt):
    print(prompt)

def function():
    return "Hello, World!"

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

# Craft a chain-of-thought prompt that asks the model to explain what the function does
prompt = f"""Explain what the code delimited by triple backticks does. 
Let's think this step by step.
```{function}```
"""
 
response = get_response(prompt)
print(response)

'''
O código acima usa pensamento em cadeia para solicitar ao modelo que explique o que a função faz. O prompt pede ao modelo para pensar passo a passo e fornecer uma explicação detalhada do código fornecido.
'''