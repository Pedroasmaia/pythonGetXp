produtos = ['apple tv','mac','iphone 11','iphone X','Ipad','Apple Watch','air pods']
produtos.sort(key=str.lower)
#Passando o função lower() como chave, assim ele coloca todos em letra minuscula e depois vai ordenar
print(produtos)

vendas_produtos = {'vinho':150,'cafeiteira':500,'microondas':300,'iphone':5500}

lista_vendas = list(vendas_produtos.items())
print(lista_vendas)

def segundo_item(tupla):
  return tupla[1]

lista_vendas.sort(key=segundo_item,reverse=True)
print(lista_vendas)