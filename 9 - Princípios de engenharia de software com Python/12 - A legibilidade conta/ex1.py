import math

'''
Opções de nome para a função:
- do_stuff
- hypotenuse_length
- pythagorean_theorem
- square_root_of_leg_a_squared_plus_leg_b_squared
'''

def hypotenuse_length(leg_a, leg_b):
    """Find the length of a right triangle's hypotenuse

    :param leg_a: length of one leg of triangle
    :param leg_b: length of other leg of triangle
    :return: length of hypotenuse
    
    >>> hypotenuse_length(3, 4)
    5
    """
    return math.sqrt(leg_a**2 + leg_b**2)


# Print the length of the hypotenuse with legs 6 & 8
print(hypotenuse_length(6, 8))

'''
O código acima define uma função que calcula o comprimento da hipotenusa de um triângulo retângulo usando o teorema de Pitágoras. A função recebe os comprimentos dos dois catetos como parâmetros e retorna o comprimento da hipotenusa. O exemplo dado calcula a hipotenusa para os catetos de comprimento 6 e 8, resultando em 10.

Além disso, o exercício pediu que o nome da função fosse colocado como um de quatro opções - do_stuff, hypotenuse_length, pythagorean_theorem, square_root_of_leg_a_squared_plus_leg_b_squared. A opção escolhida foi 'hypotenuse_length', que é clara e descritiva, algo importante para a legibilidade do código.
'''