'''
Antes:

def print_phrase(phrase, polite=True, shout=False):
    if polite:# It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:  #All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


#Politely ask for help
print_phrase('help me', polite=True)
 # Shout about a discovery
print_phrase('eureka', shout=True)
'''

'''
Depois:
'''

def print_phrase(phrase, polite=True, shout=False):
    if polite:  # It's generally polite to say please
        phrase = 'Please ' + phrase

    if shout:  # All caps looks like a written shout
        phrase = phrase.upper() + '!!'

    print(phrase)


# Politely ask for help
print_phrase('help me', polite=True)
# Shout about a discovery
print_phrase('eureka', shout=True)

'''
O código acima mostra como usar a convenção de estilo PEP 8 para melhorar a legibilidade do código Python. As principais mudanças incluem o uso de espaços em branco nos comentários para torná-los mais claros, a adição de espaços ao redor dos operadores de atribuição e a organização do código em blocos lógicos. Essas práticas ajudam a tornar o código mais fácil de ler e entender, seguindo as diretrizes recomendadas pela PEP 8.
'''