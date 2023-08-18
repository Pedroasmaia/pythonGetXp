# And (E)
# Or (Ou)

meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 15000
vendas_loja = 200000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
  bonus = 0.03* vendas_funcionario
  print(f'Bônus do funcionario foi de {bonus}')
else:
  print("Funcionario sem bônus")


nota_funcionario = 9
meta_nota = 9

if nota_funcionario >= meta_nota or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
  bonus = 0.03 * vendas_funcionario
  print(f'Bônus do funcionario foi de {bonus}')
else:
  print("Funcionário sem bônus") 
