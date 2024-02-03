# API é uma aplicação para usar serviço/site/app
# API podem precisar de uma conta de desenvolvedor
# Geralmente as informações vem em formato JSON

import requests as r
import json

cotacoes = r.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()
print(cotacoes_dic)