# :< Alinha o texto à esquerda
# :> Alinha o texto à direita
# :^ Alinha o texto ao centro
# :+ Coloca o Sinal, positivo o negativo a frente do número
# :, coloca virgula como separador de milhar
# :e formato científico
# :f número com quantidade de casad decimais
# :x Formato HEX minúscula
# :X fortmato HEX maiúscula
# :% Formato percentual


email = 'lira@gmail.com'
print(f"Meu e-mail não é {email:^50}")

custo = 500
faturamento = 270
lucro = faturamento - custo
print(f"Faturamento foi {faturamento:+} e o lucro foi {lucro:+}")

print(f"Faturamento foi {faturamento:.2f} e o lucro foi {lucro:2f}")
margem = lucro / faturamento
print(f"Margem foi de {margem:.2%}")


#Função round() para arredondar
imposto = 0.15758
preco = 100
valor = round(preco * imposto,1)
print(valor)