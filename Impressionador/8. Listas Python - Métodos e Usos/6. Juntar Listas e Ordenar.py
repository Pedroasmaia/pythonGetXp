produtos = ['apple tv', 'mac', 'iphone x','ipad','apple watch','mac book','airpods']
novos_produtos = ['iphone 12','Ioculos']

#Juntando listas com Extend para manter o nome da lista
#produtos.extend(novos_produtos)
print(produtos)

todos_produtos = novos_produtos + produtos
print(todos_produtos)

# [1] + [2] != 1+2
print(f'[1]+[2] é igual a lista {[1]+[2]} e 1 + 2 é igual a {1+2}')


#Ordenar as  listas pelo ASCII
produtos.sort()
print(produtos)
vendas = [100,270,900,1000,1500,15000,20000,1200]
vendas.sort()
print(vendas)
vendas.sort(reverse=True)
print(vendas)