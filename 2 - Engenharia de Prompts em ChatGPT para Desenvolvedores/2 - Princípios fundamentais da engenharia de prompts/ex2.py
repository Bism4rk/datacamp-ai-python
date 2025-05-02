from openai import OpenAI

client = OpenAI(api_key="<OPENAI_API_TOKEN>")

story = "In a distant galaxy, there was a brave space explorer named Alex. Alex had spent years traveling through the cosmos, discovering new planets and meeting alien species. One fateful day, while exploring an uncharted asteroid belt, Alex stumbled upon a peculiar object that would change the course of their interstellar journey forever..."

def get_response(prompt):
    print(prompt)

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks:
```{story}```
"""

# Get the generated response 
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)

# O código acima é um exemplo de como criar um prompt para completar uma história.
# O código original foi modificado para incluir uma história inicial e um prompt que pede para completar essa história.
# A história original é fornecida ao prompt por meio de formatação com aspas triplas.
