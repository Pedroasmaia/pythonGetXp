import re

informacoes = [
    "http://hashtagtreinamentos.com", 
    "https://vimeo.com/",
    "https://youtube.com/",
    "Pesquisar no Google: http://google.com",
    "http://wikipedia.org",
    "http://google.com",
    "http://bcb.gov.br/",
    "Pesquisar no Bing",
]

# Começa com
pattern = re.compile(r"^http")
for item in informacoes:
  result = re.findall(pattern,item)
  print(f'{item} contém: {result}')
# Termina com
pattern = re.compile(r".com/?$")
for item in informacoes:
  result = re.findall(pattern,item)
  print(f'{item} contém: {result}')