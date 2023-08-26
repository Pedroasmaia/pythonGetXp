produtos = ['tv','celular','tablet','mouse','teclado','geladeira','forno']
estoque = [100,150,100,120,70,90,80,15]


i = produtos.index('geladeira')
print(f'A quantidade do estoque da geladeira é {estoque[5]}')


def exercise():
    produto = input('Insira o nome do produto: ')
    if produto.lower() in produtos:
        i = produtos.index(produto.lower())
        print(f'A quantidade do estoque da {produto} é {estoque[i]}')
    else:
        print(f"{produto} não consta no estoque")
exercise()