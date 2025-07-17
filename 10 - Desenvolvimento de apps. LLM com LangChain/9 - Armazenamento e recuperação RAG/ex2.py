from langchain.prompts import ChatPromptTemplate

# Add placeholders to the message string
message = """
Answer the following question using the context provided:

Context:
{context}

Question:
{question}

Answer:
"""

# Create a chat prompt template from the message string
prompt_template = ChatPromptTemplate.from_messages([("human", message)])

'''
O código acima mostra como criar um modelo de prompt de chat usando a biblioteca LangChain. Ele define uma mensagem que inclui espaços reservados para o contexto e a pergunta, e então cria um modelo de prompt de chat a partir dessa mensagem. O modelo pode ser usado para gerar respostas baseadas no contexto fornecido e na pergunta feita.
'''