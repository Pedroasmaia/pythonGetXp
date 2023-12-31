import re

text = """
Bom dia,

Seguem os orçamentos solicitados:


Cerveja importada (330 ml) - R$12,30 - bebida
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


pattern = re.compile(r"R\$\d+,?\d*")
result = re.findall(pattern,text)
print(f"{result}",len(result))
pattern = re.compile(r"R\$\d+,?[0-5]") #Colchete diz que eu quero os numeros de zero a cinco, serve pra texto também [a-zA-Z]
result = re.findall(pattern,text)
print(f"{result}",len(result))
pattern = re.compile(r"R\$\d+,?\d{0,2}]") #Diz a de quantos, até caracteres quer pegar
result = re.findall(pattern,text)
print(f"{result}",len(result))