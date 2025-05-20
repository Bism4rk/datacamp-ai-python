from pypdf import PdfReader

# Extract text from the PDF
reader = PdfReader("US_Employee_Policy.pdf")

# Extract text from all pages
document_text = ""
for page in reader.pages: 
    document_text += page.extract_text()


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

print(document_text)

'''
O código acima é um exemplo de como extrair o texto de um documento PDF usando a bibliotca PdfReader do Python. No caso, um loop "for" é criado em que cada página do documento tem seu texto extraído e colocado em uma variável (document_text), e essa variável é imprimida no console.

Neste caso, o texto foi adicionado manualmente pois o documento PDF só pode ser acessado na plataforma DataCamp.
'''
