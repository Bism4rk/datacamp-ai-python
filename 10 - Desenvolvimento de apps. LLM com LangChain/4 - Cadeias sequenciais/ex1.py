from langchain.prompts import PromptTemplate

# Create a prompt template that takes an input activity
learning_prompt = PromptTemplate(
    input_variables=["activity"],
    template="I want to learn how to {activity}. Can you suggest how I can learn this step-by-step?"
)

# Create a prompt template that places a time constraint on the output
time_prompt = PromptTemplate(
    input_variables=['learning_plan'],
    template="I only have one week. Can you create a plan to help me hit this goal: {learning_plan}."
)

# Invoke the learning_prompt with an activity
print(learning_prompt.invoke({"activity": "play golf"}))

'''
O código acima mostra como criar dois modelos de prompt usando a biblioteca LangChain. O primeiro modelo, `learning_prompt`, é usado para solicitar um plano de aprendizado passo a passo para uma atividade específica, enquanto o segundo modelo, `time_prompt`, adiciona uma restrição de tempo ao plano de aprendizado sugerido. No próximo exercício, veremos como encadear esses prompts para criar um fluxo de trabalho mais complexo e uma cadeia sequential de prompts.
'''