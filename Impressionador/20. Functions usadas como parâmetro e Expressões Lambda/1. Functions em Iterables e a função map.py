# lista = list(map(function,iterable_original))
print(f'A Funcção MAP aplica uma função para cada item do iteravel original')
def padronizar_texto(texto):
  texto = texto.casefold()
  texto = texto.lower()
  texto = texto.replace("  "," ")
  texto = texto.strip()
  return texto

produtos = [' ABC12 ','abc1',' AbC37','BEb12','  BSA151 ','BEB23']

# Usando for
print(f'Lista de entrada: {produtos}')
for i,produto in enumerate(produtos):
  produtos[i] = padronizar_texto(produto)
print(f'Lista de saída: {produtos}')

# Usando MAP
produtos = [' ABC12 ','abc1',' AbC37','BEb12','  BSA151 ','BEB23']
print(f'Lista de entrada: {produtos}')
novos_produtos = list(map(padronizar_texto,produtos))
#Se eu não transformar em list() retorna o objeto map()
print(f'Lista de saída: {novos_produtos}')