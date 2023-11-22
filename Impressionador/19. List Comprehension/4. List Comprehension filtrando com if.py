# lista = [expressão for item in iteravel if condição]


meta = 1000
vendas_produtos = [1500,150,2100,1950]
produtos = ['vinho','cafeiteira','microondas','iphone']

produtos_acima_da_meta = []
for i,produto in enumerate(produtos):
    if vendas_produtos[i] >= meta:
        produtos_acima_da_meta.append(produto)

print(produtos_acima_da_meta)

produtos_acima_da_meta_2 = [produto for i,produto in enumerate(produtos) if vendas_produtos[i] >= meta]
print(produtos_acima_da_meta_2)