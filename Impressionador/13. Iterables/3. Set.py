print('Os Set são um tipo de estrutura que não podem ter valores duplicados, mas não tem tem ordem definida')

set_produtos = {'arroz','feijão','macarrao','atum','azeite'}
print(set_produtos)

clientes = ['Jorge','Pedro','Alfredo','Pedro','Gomes','Julio','Julio','Julio','Leandro','Jorge','Pedro']
print(f'Qual o total de clientes que passaram na loja: {len(clientes)}')
clientes_unicos = set(clientes)
lista_clientes_unicos = list(clientes_unicos)
print(f'Qual o total de clientes unicos que passaram na loja: {len(clientes_unicos)}')