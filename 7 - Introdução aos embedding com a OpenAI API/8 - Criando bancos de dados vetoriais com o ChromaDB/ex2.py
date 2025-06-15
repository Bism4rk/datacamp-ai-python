import tiktoken

documents = [
    "O Brasil é um país da América do Sul, conhecido por sua diversidade cultural e belezas naturais.",
    "A capital do Brasil é Brasília, uma cidade planejada inaugurada em 1960.",
    "O Rio de Janeiro é famoso por suas praias, como Copacabana e Ipanema, e pelo Carnaval.",
    "A Amazônia é a maior floresta tropical do mundo, abrigando uma vasta biodiversidade.",
    "O futebol é o esporte mais popular no Brasil, com muitos jogadores famosos como Pelé e Neymar.",
]

# Load the encoder for the OpenAI text-embedding-3-small model
enc = tiktoken.encoding_for_model("text-embedding-3-small")

# Encode each text in documents and calculate the total tokens
total_tokens = sum(len(enc.encode(text)) for text in documents)

cost_per_1k_tokens = 0.00002

# Display number of tokens and cost
print('Total tokens:', total_tokens)
print('Cost:', cost_per_1k_tokens * total_tokens/1000)

'''
O código acima mostra como calcular o número de tokens em um conjunto de documentos usando o modelo "text-embedding-3-small" da OpenAI. O número total de tokens é calculado somando o comprimento da codificação de cada documento. O custo é então calculado com base no número total de tokens, multiplicando pelo custo por 1.000 tokens, que é de $0.00002.
'''