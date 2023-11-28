#Lambdas Expression são funções anônimas, e tem apenas 1 linha de codigo
# variavel = lambda parametro: expressão

def minha_funcao(num):
  return num*2
print(minha_funcao(5))

minha_funcao2 = lambda num: num*2
print(minha_funcao2(5))

imposto = 1.3
tax= lambda money: money*imposto

print(tax(100))


