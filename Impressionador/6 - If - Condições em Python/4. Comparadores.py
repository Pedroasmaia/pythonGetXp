# == Igual
# != Diferente
# > Maior
# >= Maior ou Igual
# < Menor
# <= Menor ou Igual
# in (Existe dentro)
# not (Não existe dentro)
# pass Para prosseguir sem nenhum comando


faturamento1 = 2500
faturamento2 = 2220
print("Programa 1 | Comparador de Igual")
if faturamento1 == faturamento2:
    print('Os valores são iguais')
else:
    print("Os valores são diferentes")
print("Programa 2 | Comparador de Diferente")
email = 'pedro@gmail.com.br'
if email != 'pedro@gmail.com':
    print('Este não é o email')
else:
    print('Email correto')
print("Programa 3 | Comparador de not,in e pass")
email_user = input('Insira seu email: ')
if not '@' in email_user:
    print('Email invalido')
else:
   pass
