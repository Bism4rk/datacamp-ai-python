class Document:
  def __init__(self, text):
    self.text = text
    # pre tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # pre tokenize the document with non-public count_words
    self.word_counts = self._count_words()

  def _tokenize(self):
    return tokenize(self.text) # type: ignore
	
  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens) # type: ignore
  
  
'''
O código acima mostra como adicionar funcionalidades a uma classe em Python. A classe `Document` agora possui dois métodos não públicos: `_tokenize` e `_count_words`. O método `_tokenize` é responsável por dividir o texto em tokens, enquanto o método `_count_words` usa a classe `Counter` para contar as ocorrências de cada token. Esses métodos são chamados no construtor da classe, permitindo que a instância da classe tenha os tokens e as contagens de palavras prontamente disponíveis após a criação.
Esses métodos são marcados como não públicos (com o prefixo `_`) para indicar que eles são destinados a uso interno da classe e não devem ser acessados diretamente por usuários da classe. Isso é uma prática comum em Python para encapsular a lógica interna de uma classe, mantendo a interface pública limpa e fácil de usar.
'''