import requests as r
from dotenv import load_dotenv
import os

load_dotenv()

domain = input('Qual dominio quer validar: ') 

def api_info(domain):
  ''' A função faz a conexão com a API do whois

Parameters:
  domain(string): Domínio que será validado na conexão

Returns:
  registry_data(dict): Dicionário com as informações de registro do dominio

  '''
  api_key = os.getenv('pass')
  try:
    free_domain = r.get(f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={api_key}&domainName={domain}&outputFormat=json")
  except Exception as i:
    print(f'Erro na requisição {i}')
    return None
  response = free_domain.json()
  response = response['WhoisRecord']
  registry_data = response['registryData']
  return registry_data

registry_data = api_info(domain)


def analisys_response(registry_data):
  '''A Função analiza se o dominio já foi registrado baseado na resposta da conexão

Parameters:
  registry_data(dict): Dicionário com as informações de registro do dominio

  '''
  if 'No match for' in registry_data['rawText']:
    print(f'O Domínio {domain} está disponivel')
  else:
    print(f'O Domínio {domain} não está disponivel')

analisys_response(registry_data)