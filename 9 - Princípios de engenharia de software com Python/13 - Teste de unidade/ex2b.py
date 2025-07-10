from collections import Counter
from text_analyzer import SocialMedia # type: ignore

# Create an instance of SocialMedia for testing
test_post = 'learning #python & #rstats is awesome! thanks @datacamp!'
sm_post = SocialMedia(test_post)

# Test hashtag counts are created properly
def test_social_media_hashtags():
    expected_hashtag_counts = Counter({'#python': 1, '#rstats': 1})
    assert sm_post.hashtag_counts == expected_hashtag_counts

'''
O código acima mostra como criar um documento de teste para ser usado com o pacote pytest. Ele importa a classe `SocialMedia` do módulo `text_analyzer` e cria uma instância dessa classe com um post de teste. Em seguida, define uma função de teste que verifica se as contagens de hashtags estão corretas. A função usa o comando `assert` para comparar as contagens de hashtags esperadas com as contagens reais do post. Se a asserção falhar, o teste falhará, indicando que há um problema na implementação da classe `SocialMedia`.
'''