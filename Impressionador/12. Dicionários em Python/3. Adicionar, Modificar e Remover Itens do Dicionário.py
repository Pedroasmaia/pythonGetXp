print('Adicionando Items a dicionários')
lucro_1tri = {'jan':100000,'fev':120000,'mar':90000}
lucro_2tri = {'abr':88000,'mai':89000,'jun':120000}
print(lucro_1tri)
lucro_1tri['abr'] = 88000
print(lucro_1tri)


lucro_1tri.update(lucro_2tri)
print(lucro_1tri)

print('Modificando um item já existente')

lucro_1tri['jan'] = 88000
print(lucro_1tri)

print('Removendo com Del')
del lucro_1tri['jun']
print(lucro_1tri)

print('Removendo com Pop e salvando em uma váriavel')
lucro_mai = lucro_1tri.pop('mai')
print(lucro_1tri)
print(lucro_mai)


print('Limpando um dicionário')
print(lucro_1tri.clear())
