from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini", api_key='<OPENAI_API_TOKEN>')

learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

time_prompt = PromptTemplate(
    input_variables=["learning_plan"],
    template="I only have one week. Can you create a concise plan to help me hit this goal: {learning_plan}."
)

# Complete the sequential chain with LCEL
seq_chain = ({"learning_plan": learning_prompt | llm | StrOutputParser()}
    | time_prompt
    | llm
    | StrOutputParser())

# Call the chain
print(seq_chain.invoke({"activity": "play soccer"}))

'''
O código acima mostra como criar uma cadeia sequencial usando LangChain. Os dois prompts, `learning_prompt` e `time_prompt`, são usados para gerar um plano de aprendizado e, em seguida, ajustá-lo para um período de uma semana. Na cadeia, o primeiro prompt gera um plano de aprendizado detalhado, que é então passado para o segundo prompt para criar um plano mais conciso adequado ao tempo disponível. O resultado final é impresso na tela.
'''