# 001 - Verificação de Disponibilidade de Domínio

## Requisitos

1. Crie um script em Python que permita ao usuário verificar a disponibilidade de um nome de domínio.

2. Utilize a API pública do WHOIS (por exemplo, https://www.whoisxmlapi.com/whoisserver/WhoisService) para realizar a consulta de informações sobre o domínio.

3. O usuário deve ser capaz de inserir o nome de domínio que deseja verificar.

4. O script deve enviar uma solicitação para a API do WHOIS para obter informações sobre o status do domínio.

5. Exiba na tela se o domínio está disponível ou não, com base na resposta recebida da API.

## Dicas

- Considere tratar erros ou respostas inesperadas da API.
- Pode ser útil criar uma função para lidar com a comunicação com a API e outra para analisar a resposta.
- Utilize bibliotecas como requests para fazer solicitações HTTP.
