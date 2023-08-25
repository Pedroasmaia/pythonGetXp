'''
Verifique se uma string tem a mesma quantidade de 'x's e 'o's. O método deve retornar um booleano e não diferenciar maiúsculas de minúsculas. A string pode conter qualquer caractere.
'''
def xo(s):
   s = s.lower()
   return s.count('x') == s.count('o')
print(xo('XO'))