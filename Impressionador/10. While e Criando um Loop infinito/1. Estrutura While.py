'''
while condição:
    repete esse bloco
'''

vendas = []
venda = input('Registre um Produto. Para cancelar, basta apertar enter com a caixa vazia. ')
while venda:
    vendas.append(venda)
    venda = input('Registre um Produto. Para cancelar, basta apertar enter com a caixa vazia. ')
print(f'Produtos cadastrados foram: {vendas}')