
# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia): # type: ignore
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(text)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT') # type: ignore
        # Return retweet_text as a SocialMedia object
        return SocialMedia(retweet_text) # type: ignore

help(filter_lines) # type: ignore

'''
O código acima é um exemplo de herança de classes em Python, onde a classe `Tweets` herda de `SocialMedia`. A classe `Tweets` adiciona uma funcionalidade específica para processar retweets, utilizando o método `_process_retweets`. O uso de `super()` permite chamar o construtor da classe pai, garantindo que todas as funcionalidades herdadas sejam mantidas. A função `filter_lines` é usada para filtrar o texto dos tweets, e o resultado é retornado como um objeto `SocialMedia`.
'''