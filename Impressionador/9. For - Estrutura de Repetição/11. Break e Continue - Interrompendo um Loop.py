# Break -> Interrompe o Loop
# Continue -> Interrompe a repetiçao

vendas = [100,150,1500,2000,120]
vendedores = ['Joao','Julia','Ana','Jose','Maria']
meta = 110
for venda in vendas:
    if venda < meta:
        print('A Lojá Não ganha bonus')
        break
    print(venda)

meta = 130
for i,venda in enumerate(vendas):
    if venda < meta:
        continue
    print(f'O {vendedores[i]} vendeu {venda}')