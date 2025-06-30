# Import needed package
import pycodestyle

# Create a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

# Run PEP 8 check on multiple files
result = style_checker.check_files(['nay_pep8.py', 'yay_pep8.py'])

# Print result of PEP 8 style check
print(result.messages)


'''
O código acima mostra como usar o módulo pycodestyle para verificar se o código Python segue as convenções de estilo PEP 8. Primeiro, importamos o módulo pycodestyle e criamos uma instância de StyleGuide. Em seguida, usamos o método check_files para verificar os arquivos 'nay_pep8.py' e 'yay_pep8.py'. O resultado da verificação é armazenado na variável result, que contém mensagens sobre quaisquer problemas encontrados. Por fim, imprimimos as mensagens de resultado.
O módulo pycodestyle é uma ferramenta útil para garantir que o código Python esteja em conformidade com as convenções de estilo PEP 8, que são amplamente aceitas na comunidade Python. Ele ajuda a manter o código legível e consistente, facilitando a colaboração entre desenvolvedores e a manutenção do código a longo prazo.
'''