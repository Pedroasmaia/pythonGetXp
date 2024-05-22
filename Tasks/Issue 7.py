import string

print()

password = input('Insira a senha que deseja testar: ')
strong_level = 0

for c in password:
  if c in string.ascii_uppercase:
    strong_level += 1
    break
for c in password:
  if c in string.ascii_lowercase:
    strong_level += 1
    break
for c in password:
  if c in string.punctuation:
    strong_level += 2
    break
for c in password:
  if c in string.digits:
    strong_level += 1
    break

if len(password) <= 3:
  print('Sua deve ter no mínimo 3 caracteres')
  exit()
elif len(password) < 4:
  strong_level += 1
elif len(password) < 8:
  strong_level += 2
else:
  strong_level += 3

if strong_level >= 8:
  print('Senha Forte')
elif strong_level < 8 and strong_level > 4:
  print('Senha Média')
else:
  print('Senha Fraca')