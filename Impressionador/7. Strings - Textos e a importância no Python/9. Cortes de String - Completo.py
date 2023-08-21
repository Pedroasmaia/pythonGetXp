precos = "Jan: 25, Fev: 27, Mar:29"
#String[Inclusivo:Exclusivo]
preco_jan = precos[5:7]
preco_fev = precos[14:16]
#Indices negativos
preco_mar = precos[-2:]
print(preco_fev)

#Step , pegar de quantos em quantos [init:final:pulos]

codigo ='1.2.3.4,5,1,2.3.4,7.9'
pedaco_cod = codigo[::2]
print(pedaco_cod)
pedaco_cod_negativo = codigo[::-2]
print(pedaco_cod_negativo)
