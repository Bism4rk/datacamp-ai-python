# Import custom text_analyzer package
import text_analyzer # type: ignore

datacamp_tweet = "DataCamp is a great place to learn data science! #DataScience #Python"

# Create an instance of Document with datacamp_tweet
my_document = text_analyzer.Document(text=datacamp_tweet)

# Print the text attribute of the Document instance
print(my_document.text)

'''
O código acima mostra como usar uma classe definida em um pacote personalizado chamado `text_analyzer`. Ele importa a classe `Document` do pacote, cria uma instância dessa classe passando uma string de texto (`datacamp_tweet`) e imprime o atributo `text` da instância. Isso demonstra como instanciar classes de pacotes personalizados e acessar seus atributos.
'''