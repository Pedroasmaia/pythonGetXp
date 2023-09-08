vendas = [
('20/08/2020','iphone x','azul','128gb',350,4000),
('20/08/2020','iphone x','prata','128gb',1500,4000),
('20/08/2020','ipad','prata','256gb',127,6000),
('20/08/2020','ipad','prata','128gb',981,5000),
('21/08/2020','iphone x','azul','128gb',397,4000),
('21/08/2020','iphone x','prata','128gb',1017,4000),
('21/08/2020','ipad','prata','256gb',50,6000),
('21/08/2020','ipad','prata','128gb',4000,5000),
]
produto_mais_vendido = ''
qtde_produto_mais_vendido = 0
cor_produto_mais_vendido = ''
memoria_produto_mais_vendido = ''
for item in vendas:
    data,produto,cor,memoria,unidade,valor = item
    if data == '21/08/2020':
        if unidade > qtde_produto_mais_vendido:
            produto_mais_vendido = produto
            qtde_produto_mais_vendido = unidade
            cor_produto_mais_vendido = cor
            memoria_produto_mais_vendido = memoria
print(f'O Produto mais vendido do dia 21/08/2020 foi o {produto_mais_vendido} com {qtde_produto_mais_vendido} vendas, da cor {cor_produto_mais_vendido} e memoria de{memoria_produto_mais_vendido}')
