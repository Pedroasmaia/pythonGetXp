#Verificar tamanho
produtos = ['apple tv', 'mac', 'iphone x','ipad','apple watch','mac book','airpods']
vendas = [1000,1500,15000,270,900,100,1200]
tamanho = len(produtos)
print(f'Temos {tamanho} produtos')
#Verificar maior tamanho
mais_vendido = max(vendas)
print(f'O Produto mais vendido teve {mais_vendido} vendas')
#Verificar o menor tamanho
menos_vendido = min(vendas)
print(f'O Produto menos vendido teve {menos_vendido} vendas')
i = vendas.index(menos_vendido)
print(f'O Produto menos vendido foi {produtos[i]}')
i = vendas.index(mais_vendido)
print(f'O Produto mais vendido foi {produtos[i]}')
