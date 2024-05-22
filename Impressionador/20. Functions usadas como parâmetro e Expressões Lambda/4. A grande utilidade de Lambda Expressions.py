preco_tecnologia = {'notebook asus':2450,'iphone':4500,'samsung galaxy':3000,'tv samsung':1000,'ps5':3000}
print(f'Function Comum: ')
def incluir_imposto(preco):
  return preco*1.3

preco_com_imposto = list(map(incluir_imposto,preco_tecnologia.values()))
print(preco_com_imposto)

print(f'Function Lambda: ')
preco_com_imposto2 = list(map(lambda preco: preco * 1.3,preco_tecnologia.values()))
print(preco_com_imposto2)


print('Função Filter, recebe uma função e um item, retorna como resposta todos os itens onde a função é TRUE')

print('Usando Function Comum:')
def maior_que200(item):
  return item[1] > 2000

produto_acima2000 = list(filter(maior_que200,preco_tecnologia.items()))
print(produto_acima2000)

print('Usando Function Lambda: ')
produto_acima2000_2 = list(filter(lambda item: item[1] > 2000,preco_tecnologia.items()))
print(produto_acima2000_2)
