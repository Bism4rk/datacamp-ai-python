# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Bruno Reichert',
      packages=['text_analyzer'])

'''
O código acima mostra como criar um arquivo de configuração para um pacote Python usando a biblioteca `setuptools`. Esse arquivo é usado pelo `pip` para instalar o pacote e suas dependências. Ele define o nome do pacote, a versão, uma descrição, o autor e os pacotes incluídos no pacote. Isso é útil para tornar o pacote portátil, facilmente instalável em diferentes ambientes Python, e publicável no PyPI (Python Package Index) para que outros possam usá-lo.
'''