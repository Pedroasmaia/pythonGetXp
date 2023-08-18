meta = 20000
vendas = 50000

if vendas < meta:
    print(f'Não ganhou o bônus')
elif vendas > (meta*2):
    bonus = vendas * 0.07
    print(f'Ganhou {bonus} de bônus')
else:
    bonus = vendas * 0.03
    print(f'Ganhou {bonus} de bônus')
    