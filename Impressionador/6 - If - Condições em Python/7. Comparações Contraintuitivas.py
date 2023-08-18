## Comparações Contraintuitivas

faturamento = input('Qual foi o faturamento da loja esse mês? ')
custo = input('Qual foi o custo da loja esse mês? ')

if faturamento and custo:
 lucro = int(faturamento) - int(custo)
 print(f'O Lucro da loja foi de {lucro} reais')
else:
 print("Preencha o faturamento e o custo corretamente")