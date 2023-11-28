# Criar uma função que permita calcular o valor acrescido do imposto em diferentes categorias(Produto, serviço royalties, etc):
# Produto : 0.1
# Serviço : 0.15
# Royalties: 0.25

def calcular_imposto(imposto):
  return lambda preco: preco*imposto


calcular_preco_produto = calcular_imposto(1.1)
calcular_preco_serviço = calcular_imposto(1.15)
calcular_preco_royalties = calcular_imposto(1.25)

print(int(calcular_preco_produto(100)))
print(int(calcular_preco_royalties(100)))
print(int(calcular_preco_serviço(100)))