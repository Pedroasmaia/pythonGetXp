
import os
from twilio.rest import Client


account_id = 'AC5c52b5d9fa32088f70d66c823b6acab8'
token = 'a8f205992ed89496d65494c816943b96'

client = Client(account_id, token)

remetente = '+12673146276'
destino = '+5531998058074'
message = client.messages.create(
  from_=remetente,
  to=destino,
  body = "Você esta programando em Python meu querido"
)

print(message.sid)