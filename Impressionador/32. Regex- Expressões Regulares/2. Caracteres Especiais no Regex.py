import re

texto = """
Bom dia,

Seguem os orçamentos solicitados:


Cerveja importada (330 ml) - R$12,30598615178 - bebida
Cerveja nacional (0,5 litros) - R$6,10 - bebida
Garrafa de vinho (750ml) - R$39,90 - bebida
Água (garrafa de 1,5 litros) - R$3,30 - bebida
Alface (1 unidade) - R$3,50 - comida
Cebolas (1kg) - R$5,10 - comida
Batatas (1 kg) - R$5,20 - comida
Tomates (1 kg) - R$7,90 - comida
Laranjas (1 kg) - R$4,70 - comida
Bananas (1kg) - R$5,50 - comida
Maçãs (1 kg) - R$8,30 - comida
Queijo fresco (1 kg) - R$42,90 - comida
Uma dúzia de ovos(12) - R$9,80 - comida
Arroz (1 kg) - R$5,70 - comida
Um quilo de pão (1 kg) - R$7,20 - comida
Leite (1 litro) - R$5,20 - bebida
Azeite (1 unidade) - R$20 - tempero
Pimenta Reino (20g) - R$5 - tempero


Favor informar as quantidades desejadas 
para emissão da Nota Fiscal.

Att.,"""

#Contar quantas comidas

padrao = re.compile("comida")
#Search te da apenas a 1 aparencia do padrão e fornece a posição do item
resultado = re.search(padrao,texto)
print(resultado)

padrao = re.compile("comida")
#finditer te a um iterador com cada elemento com as informações da posição
resultado = re.finditer(padrao,texto)
for item in resultado:
  print(item)


padrao = re.compile('\$')
resultado = re.findall(padrao,texto)
print(len(resultado))