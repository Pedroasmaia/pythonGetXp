"""
## 1. Criando um mini sistema de controle de estoque

- Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
- Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print) para fazer um novo pedido daquele produto.
- Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:

- alimentos -> Estoque mínimo: 50
- bebidas -> Estoque mínimo: 75
- limpeza -> Estoque mínimo: 30

Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.

Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.<br>
Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.<br>
Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.
"""

print('Controle de Estoque')

minimun_drinks = 75
minimun_food = 50
minimun_cleaning = 30

product_category = input('Insira o categoria do produto: ')
product_name = input('Insira o nome do produto: ')
product_quantity = input('Insira o quantidade do produto: ')


if product_name and product_category and product_quantity:
   if product_category.lower() == 'bebidas' and int(product_quantity) < minimun_drinks:
    print(f'Solicitar {product_name} à equipe de compras, temos apenas {product_quantity} em estoque')
   elif product_category.lower() == 'alimentos' and int(product_quantity) < minimun_food:
    print(f'Solicitar {product_name} à equipe de compras, temos apenas {product_quantity} em estoque')
   elif product_category.lower() == 'limpeza' and int(product_quantity) < minimun_cleaning:
    print(f'Solicitar {product_name} à equipe de compras, temos apenas {product_quantity} em estoque')
else:
   print('Preencha as informações corretamente')