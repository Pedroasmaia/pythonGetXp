funcionarios = ['maria','jose','antonio','joao','fransisco','ana','paulo']
for i,funcionario in enumerate(funcionarios):
    print(f'{i} é o funcionário {funcionario}')

estoque = [1200,300,800,1500,900,2750,400,20,23,70,90]
produtos = ['coca','pespi','guarana','skol','brahma','agua','del valle','dolly','red bull','cachaça','vinho']

for i,qtde in enumerate(estoque):
    if qtde <= 50:
        print(f'O Produto {produtos[i]} está com apenas {qtde} unidades no estoque')