produtos = ['iphone','ipad','airpod','macbook']
precos = [7000,10000,2500,14000]

for preco in precos:
    print(preco * 1.1)

for i in range(len(produtos)):
    print(produtos[i],':',precos[i])

for i,preco in enumerate(precos):
    print(f'Produto: {produtos[i]},valor {preco*1.1}')