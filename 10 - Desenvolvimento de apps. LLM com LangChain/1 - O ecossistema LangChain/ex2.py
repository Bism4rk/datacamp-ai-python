# Import the class for defining Hugging Face pipelines
from langchain_huggingface import HuggingFacePipeline

# Define the LLM from the Hugging Face model ID
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 20}
)

prompt = "Hugging Face is"

# Invoke the model
response = llm.invoke(prompt)
print(response)

'''
O código acima demonstra como usar o LangChain com um modelo do Hugging Face. Ele importa a classe `HuggingFacePipeline` para definir um pipeline de LLM e cria uma instância do modelo "nano-mistral" para geração de texto. O prompt "Hugging Face is" é passado para o modelo, que gera uma resposta com até 20 novos tokens. A resposta é então impressa no console.
Isso ilustra como o LangChain pode ser usado para integrar modelos do Hugging Face em aplicações, facilitando o uso de modelos de linguagem pré-treinados para tarefas de geração de texto.
'''