from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

story = "In a distant galaxy, there was a brave space explorer named Alex. Alex had spent years traveling through the cosmos, discovering new planets and meeting alien species. One fateful day, while exploring an uncharted asteroid belt, Alex stumbled upon a peculiar object that would change the course of their interstellar journey forever..."

def get_response(prompt):
    print(prompt)

# Create a request to complete the story
prompt = f"""Complete the story delimited by triple backticks in the style of Shakespeare and in two paragraphs at most:
```{story}```
"""

# Get the generated response
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)

'''
O código acima é mais um exemplo de engenharia de prompts. No caso, o prompt pede que o modelo complete a história no estilo de Shakespeare e em no máximo dois parágrafos. Isso demonstra como a engenharia de prompts pode ser usada para guiar o modelo a gerar respostas mais específicas e criativas.

Além disso, a string do prompt usa f-strings para incluir a história original, o que facilita a formatação e a legibilidade do código. Isso é especialmente útil quando se trabalha com histórias ou textos longos, pois permite que o desenvolvedor mantenha o código organizado e fácil de entender.
O uso de aspas triplas para delimitar a história original também é uma prática comum em Python, pois permite que o texto seja escrito em várias linhas sem a necessidade de caracteres de escape. Isso torna o código mais limpo e legível.
'''