vendas_tech = {'iphone':15000,'samsung galaxy':12000,'tv samsung':10000,'ps5':14300,'notebook hp':1000,'notebook dell':17000,'notebook asus':2450}


print('O Método Keys() pega todas as chaves e transofrma em dict_lista que são atualizadas junto com o dicionario')
print(vendas_tech.keys())
print('O Método values() pega todas as chaves e transofrma em dict_lista que são atualizadas junto com o dicionario')
print(vendas_tech.values())

print('Para transformar em uma lista python, salve em uma variavel e use o método List()')
chaves = vendas_tech.keys()
lista_chaves = list(chaves)
valores = vendas_tech.values()
valores = list(valores)
print(valores)
print(chaves)
lista_chaves.sort()
print('--------------')
for chave in lista_chaves:
    print(f'{chave} vendeu {vendas_tech[chave]} unidades')