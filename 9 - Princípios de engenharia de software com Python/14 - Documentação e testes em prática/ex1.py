from text_analyzer import Document # type: ignore

class SocialMedia(Document):
    """Analyze text data from social media
    
    :param text: social media text to analyze

    :ivar hashtag_counts: Counter object containing counts of hashtags used in text
    :ivar mention_counts: Counter object containing counts of @mentions used in text
    """
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

'''
O código acima mostra como criar uma docstring para uma classe em Python, que então pode ser usada com a ferramenta Sphinx para gerar documentação. A docstring inclui uma breve descrição da classe, parâmetros e variáveis de instância, seguindo o padrão reStructuredText (reST) que é compatível com Sphinx. A ferramenta Sphinx pode então extrair essas informações para gerar documentação estruturada e legível em um formato como HTML ou PDF, que então pode ser usada para entender melhor o código e suas funcionalidades e colocada na web (ser hospedada em um link GitHub Pages, por exemplo).
'''