vendas_tech = {'iphone':15000,'samsung galaxy':12000,'tv samsung':10000,'ps5':14300,'notebook hp':1000,'notebook dell':17000,'notebook asus':2450}

total_notebook = 0

for chave in vendas_tech:
    if 'notebook' in chave:
        total_notebook += vendas_tech[chave]
print(f'Total de notebooks vendidos {total_notebook}')

