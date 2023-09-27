def cadastrar_produto():
    produto = input('Digite o nome do produto: ')
    produto = produto.strip()
    return produto.title()

produto = cadastrar_produto()
print(f'Produto: {produto} cadastrado com sucesso')