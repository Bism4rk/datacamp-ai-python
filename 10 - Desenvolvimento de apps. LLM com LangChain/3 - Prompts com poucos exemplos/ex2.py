from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from ex1 import examples

# Complete the prompt for formatting answers
example_prompt = PromptTemplate.from_template("Question: {question}\n{answer}")

# Create the few-shot prompt
prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

prompt = prompt_template.invoke({"input": "What is Jack's favorite technology on DataCamp?"})
print(prompt.text)

'''
O código acima mostra como criar um prompt de poucos exemplos usando o LangChain. Ele utiliza um template de prompt para formatar as respostas e um conjunto de exemplos para guiar o modelo. O resultado é um prompt que pode ser usado para responder a perguntas específicas, como a preferência tecnológica de Jack no DataCamp.
'''