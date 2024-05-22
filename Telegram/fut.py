import os
import requests as r

from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters,CallbackContext
from json.decoder import JSONDecodeError


load_dotenv()

token = os.getenv("token_api")
# url = f'https://api.sportmonks.com/v3/football/fixtures/18535517?api_token={token}&include=events'
url = f'https://api.sportmonks.com/v3/football/topscorers/seasons/21638'
try:
  response_api = r.get(url=url+f'?api_token={token}')
  print(response_api.json())
except JSONDecodeError as i:
  print(f'Exception: {i}')   


# bot = context.bot
# await bot.send_message(chat_id=update.message.chat_id,text=message)   
# bot.send_message(chat_id=update.message.chat_id,text=f"O {pokemon[12:]} tem as seguintes habilidades:")