lista = ['ipad', 'iphone x', 'apple tv']
lista2 = lista
lista[1] = 'Iphone 11'
print(lista)
print(lista2)


##Copiando

lista2 = lista.copy()
lista[1] = 'Iphone 12'
print(lista)
print(lista2)

## Para copiar parcial usamos o index

lista3 = lista[1:]
print(lista3)