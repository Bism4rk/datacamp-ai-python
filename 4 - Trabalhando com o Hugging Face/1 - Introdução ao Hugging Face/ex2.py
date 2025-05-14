from huggingface_hub import HfApi

# Create an instance of the HfApi class
api = HfApi()

# List only the first 2 models available on the Hub
models = list(api.list_models(limit=2))

# Print the first 2 models
for model in models:
    print(model)


'''
O código acima mostra como usar a biblioteca huggingface_hub para listar os modelos disponíveis no Hugging Face Hub.
O Hugging Face Hub é uma plataforma que hospeda modelos de aprendizado de máquina, datasets e outros recursos relacionados à inteligência artificial e processamento de linguagem natural.

Como a API do Hugging Face Hub é gratuita, esse código pode ser executado sem a necessidade de autenticação, ao contrário dos códigos anteriores que exigiam autenticação para acessar os modelos.
'''