# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='text_analyzer',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='Bruno Reichert',
      packages=['text_analyzer'],
      install_requires=['matplotlib>=3.0.0'])

'''
O código acima novamente mostra como criar um arquivo de configuração para um pacote Python usando a biblioteca `setuptools`. Além dos campos já mencionados, ele também inclui o campo `install_requires`, que especifica que o pacote depende da biblioteca `matplotlib` com uma versão mínima de 3.0.0. Isso garante que, ao instalar o pacote, a dependência necessária será instalada automaticamente, facilitando ainda mais a portabilidade do pacote Python.
'''