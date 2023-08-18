"""
Exercício 1
Crie um programa que calcule e dê um print do bônus que os funcionários devem receber segundo a regra:

A meta é 1000 vendas
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é de 10% do valor de vendas.
Caso contrário o valor de bônus do funcionário é de 10% do valor de vendas.
Caso contrário o valor de bônus do funcionário é de 0 %.
Print o bônus dos 3 funcionários 
"""


employee1 = 1000
employee2 = 770
employee3 = 2700
def exercise1(sales):
  goal_sales = 1000
  if sales >= goal_sales:
      bonus = sales * 0.1
  else:
      bonus = 0
  print(f'O Bonus do Funcionário é de R${bonus},00')
exercise1(employee1)
exercise1(employee2)
exercise1(employee3)

"""
Exercício 2
Crie um programa que calcule e dê um print do bônus que os funcionários novamente. Porém há uma nova regra nesse 2° caso:
A meta é 1000 vendas
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:
- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15%, sobre o valor de vendas
- Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas.
- Se vendas funcionário for menos do que 1000 então o bonus do funcionário é de 0
Use as mesmas variáveis de vendas_funcionários.
"""


def exercise2(sales):
  goal_sales = 1000
  if sales >= 2000:
    bonus = 0.15*sales
  elif sales < 2000 and sales>=1000:
    bonus = 0.1*sales
  else:
    bonus = 0
  print(f'O Bonus do funcionário é de R${bonus},00')

exercise2(employee1)
exercise2(employee2)
exercise2(employee3)