from transformers import pipeline

document_text = """US Employee Policy Document
    Welcome to the US Employee Policy document. This document outlines the policies and benefits
    available to all employees. Please read carefully to understand your entitlements and
    responsibilities.
    1. Vacation Policy:
    Employees are entitled to 25 vacation days annually.
    2. Sick Leave:
    Employees may take up to 10 sick days per year.
    3. Notice Period:
    Employees are required to give a 2-week notice before resignation.Work and Leave Policies
    4. Public Holidays:
    The company observes 12 public holidays annually.
    5. Maternity Leave:
    Employees are entitled to up to 16 weeks of maternity leave.
    6. Paternity Leave:
    Employees are entitled to up to 10 days of paternity leave.
    7. Volunteer Days:
    Each employee is allowed 1 volunteer day annually to contribute to social causes.Additional Information
    8. Probation Period:
    New employees undergo a 3-month probation period.
    9. Remote Work:
    Employees may work remotely up to 2 days per week.
    10. Retirement Age:
    The standard retirement age is 65 years.
    For further questions, please contact the HR department."""

# Load the question-answering pipeline
qa_pipeline = pipeline(task="question-answering", model="distilbert-base-cased-distilled-squad")

question = "What is the notice period for resignation?"

# Get the answer from the QA pipeline
result = qa_pipeline(question=question, context=document_text)

# Print the answer
print(f"Answer: {result['answer']}")

'''
O código acima mostra como responder perguntas comuns com documentos por meio de uma pipeline da HuggingFace. Neste caso, a pergunta sobre o período de pré-aviso para demissão é respondida por meio da variável document_text, obtida no exercício anterior por meio da extração de texto de um documento PDF (colocada aqui manualmente para não dar erro).
'''