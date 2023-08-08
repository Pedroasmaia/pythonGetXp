nome = "Pedro Augusto Souza Maia"
primeiro,segundo,terceiro,quarto = nome.split(' ')
print(primeiro)
print(segundo)
print(terceiro)
print(quarto)

numeros= 9998909598909794
try:
   a,b,c,d,e,d,f,g = numeros.split('9')
except AttributeError:
   print("Não funciona em Inteiros")
try:
   doc = {"A":"A","B":"B","C":"C"}
   letra_a,letra_c = doc.split("B")
except ArithmeticError:
   print("Não funciona em Dict")