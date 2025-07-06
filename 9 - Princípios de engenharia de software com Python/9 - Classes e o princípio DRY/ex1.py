class Document:
    def __init__(self, text):
        self.text = text
        self.tokens = self.tokenize(text)
        self.word_counts = self.count_words(self.tokens)

    def tokenize(self, text):
        # Tokenization logic (e.g., splitting by whitespace)
        return text.split()

    def count_words(self, tokens):
        from collections import Counter
        return Counter(tokens)

# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)

'''
O código acima mostra como usar herança em Python. A classe `SocialMedia` herda da classe `Document`, permitindo que ela utilize os métodos e atributos definidos na classe pai. Isso demonstra o princípio DRY (Don't Repeat Yourself), pois evita a duplicação de código ao reutilizar a lógica de tokenização e contagem de palavras da classe `Document`. Assim, a classe `SocialMedia` pode se concentrar em funcionalidades específicas relacionadas a mídias sociais, mantendo o código limpo e organizado.
'''
