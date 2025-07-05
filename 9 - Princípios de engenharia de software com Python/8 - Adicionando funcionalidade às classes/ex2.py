# create a new document instance from datacamp_tweets
datacamp_doc = Document(datacamp_tweets) # type: ignore

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc.word_counts.most_common(5))

'''
O código acima mostra como criar uma instância da classe `Document` usando um conjunto de tweets do DataCamp. Ele imprime os primeiros 5 tokens do documento e as 5 palavras mais usadas, juntamente com suas contagens. Isso demonstra como a classe `Document` pode ser usada para análise de texto, fornecendo funcionalidades para tokenização e contagem de palavras de forma encapsulada e organizada.
'''