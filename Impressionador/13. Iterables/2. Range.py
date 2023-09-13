produtos = ['arroz','feijao','macarrao','atum','azeite']
estoque = [50,100,20,5,80]

print('O Range abaixo preenche os valores até o item passado como parâmetro, sendo ele excludente')
for i in range (5):
    print(f'O indice {i} é o produto: {produtos[i]} na lista de produtos')

print('Podemos passar o inicio e o fim:')
for i in range(3,6):
    print(i)

print('Podemos pedir pro ranger andar de x em x casas:')
for i in range(0,13,3):
    print(i)