vendas = [1200,300,800,1500,1900,2750,400,20,23,70,90,80,1100,999,900,800,870,50,1111,120,300,450,800]
meta = 1000

qtde_bateu_meta = 0
for venda in vendas:
    if venda >= meta:
        qtde_bateu_meta += 1
qtde_funcionarioss = len(vendas)
print(f'{qtde_bateu_meta/qtde_funcionarioss:.1%} Bateram a meta')