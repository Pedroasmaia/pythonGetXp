produtos = ['apple tv', 'mac', 'iphone x','ipad','apple watch','mac book','airpods']
print(produtos)
# Append() Adiciona o item na lista no final
produtos.append('iphone 11')
print(produtos)
# Remove() usa o item
produtos.remove('iphone x')
print(produtos)

# Pop() usa o indice, e pode armazenar em alguma váriavel o item removido
i = produtos.index('airpods')
item_removido = produtos.pop(i)
print(f'Removemos o produto: {item_removido}')


## Tratando erro com if
 
remover_item = 'mac'
if remover_item in produtos:
    produtos.remove(remover_item)
else:
    print(f"{remover_item} não existe na lista de produtos")

## Tratando erro com Try

try:
    produtos.remove(remover_item)
except:
    print(f"{remover_item} não existe na lista de produtos")    