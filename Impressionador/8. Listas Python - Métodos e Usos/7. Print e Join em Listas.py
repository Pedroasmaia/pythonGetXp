produtos = ['apple tv', 'mac', 'iphone x','ipad','apple watch','mac book','airpods']
print(produtos)

#join()
print(f'Esses são meus produtos: ')
print('\n'.join(produtos))

#split faz o contrario:
produtos = 'apple tv,  mac, iphone x, ipad, apple watch, mac book, airpod'
lista = produtos.split(', ')
print(lista)