from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from ex1 import examples, example_prompt
from langchain.chat_models import ChatOpenAI

prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

# Create an OpenAI chat LLM
llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

# Create and invoke the chain
llm_chain = prompt_template | llm
print(llm_chain.invoke({"input": "What is Jack's favorite technology on DataCamp?"}))

'''
O código acima mostra como criar um prompt de poucos exemplos usando o LangChain e como integrá-lo com um modelo de linguagem da OpenAI. Ele utiliza um template de prompt para formatar as respostas com base em exemplos fornecidos e invoca o modelo para responder a uma pergunta específica. O resultado é uma resposta gerada pelo modelo com base no contexto dos exemplos.
'''