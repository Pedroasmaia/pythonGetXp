vendas_tech = {'iphone':15000,'samsung galaxy':12000,'tv samsung':10000,'ps5':14300,'notebook hp':1000,'notebook dell':17000,'notebook asus':2450}

print('Items() do dicionários, transforma em uma lista de tuplas')

'''
items_dicionario = vendas_tech.items()
print(items_dicionario)
##Ou
'''

for produto,quantidade in vendas_tech.items():
    print(f'O {produto} vendeu {quantidade}')

'''
print(f'Complicando um pouco')
for produto,quantidade in vendas_tech.items():
    if quantidade > 5000:
        print(f'O {produto} vendeu {quantidade}')
'''
