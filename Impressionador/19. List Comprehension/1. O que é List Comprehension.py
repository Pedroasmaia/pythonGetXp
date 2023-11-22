print("List Comprehension é uma forma reduzida de se escrever um for")
# lista = [expressão for item in itrerable]~

preco_produto = [100,150,300,5500]
produtos = ['vinho','cafeiteira','microondas','iphone']

imposto = []
# Tarefa feita com FOR
for produto in preco_produto:
  imposto.append(produto*0.3)
print(imposto)

# Tarefa feita com List Comprehension
impostos = [preco * 0.3 for preco in preco_produto]
# Impostos é uma lista de preço * 0.3 para cada preço dentro da lista preço produto
print(impostos)


def calcular_imposto(preco,imposto):
  return preco * imposto

impostos = [calcular_imposto(preco,0.1) for preco in preco_produto]
print(impostos)
