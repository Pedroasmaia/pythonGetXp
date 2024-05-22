
import os
from twilio.rest import Client


account_id = 'minha_id'
token = 'meu_token'

client = Client(account_id, token)

remetente = '+12673146276'
destino = '+5531998058074'
message = client.messages.create(
  from_=remetente,
  to=destino,
  body = "Você esta programando em Python meu querido"
)

print(message.sid)