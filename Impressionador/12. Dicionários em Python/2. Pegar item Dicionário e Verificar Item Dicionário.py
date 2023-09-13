#Informações são pegados pela chave:
mais_vendidos = {'tecnologia':'iphone','refrigeracao':"ar consul 12000 btu","livro": "o alquimista","lazer":"Prancha de Surf"}
vendas_tech = {'iphone':15000,'samsung galaxy':12000,'tv samsung':10000,'ps5':14300}

print(f"O Livro mais vendido foi {mais_vendidos['livro']}")
print(f"O Item mais mais vendido foi em lazer foi: {mais_vendidos['lazer']}")

print(f"O Vendemos {vendas_tech.get('iphone')} Iphones")

print(vendas_tech.get('Iphone X'))

#print(vendas_tech['Iphone X'])


if 'copo' in vendas_tech:
    print(vendas_tech['copo'])
else:
    print('Não existe copo nesse dicionario')
if vendas_tech.get('copo') == None:
    print('Não existe copo nesse dicionario')
else:
    print(vendas_tech['copo'])