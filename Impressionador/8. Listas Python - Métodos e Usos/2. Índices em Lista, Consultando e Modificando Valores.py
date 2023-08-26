produtos = ['tv','celular','mouse','teclado','tablet']
print(produtos[1])
vendas = [1000,1500,350,270,900]
print(vendas[1])
print(f'Vendas do produto {produtos[3]} foram de {vendas[3]} unidades')
#Listas são mutaveis
vendas[3] += 30
print(f'Vendas do produto {produtos[3]} foram de {vendas[3]} unidades')

texto = 'pedro@gmail.com'
texto = texto.replace('o','a')
print(texto)
