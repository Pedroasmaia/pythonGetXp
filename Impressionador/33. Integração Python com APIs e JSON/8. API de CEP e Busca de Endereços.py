import requests as r
import pprint
import pandas as pd


def input_cep():
  cep = input("Entre com seu CEP:")
  cep = cep.replace("-","").replace(".","").replace(" ","")
  url = f"https://viacep.com.br/ws/{cep}/json/"

  if len(cep) == 8:
    a = r.get(url)
    if a.status_code == 200:
      dict_request = a.json()
      uf = dict_request['uf']
      localidade = dict_request['localidade']
      bairro = dict_request['bairro']
      print(localidade)
      print(bairro)
      print(uf)
    else:
      print(f"{a.status_code} : {a.text}")
  else:
    print(f"O Cep tem {len(cep)} dígitos")

def search_adress():    
  cidade = input("Qual a cidade: ")
  uf = input("Qual a sigla do estado: ")
  endereco = input("Qual o endereço: ")
  url_seach_cep = f"https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/"
  search = r.get(url_seach_cep)
  dict_enderecos = search.json()
  tabela = pd.DataFrame(dict_enderecos)
  print("*" * 16)
  print(tabela)
  print("*" * 16)
search_adress()