import os
import requests as r

from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters,CallbackContext
from json.decoder import JSONDecodeError


load_dotenv()

token = os.getenv("telegram_token")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Olá {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def ability_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    pokemon = update.message.text
    pokemon = pokemon.lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon[12:]}'
    try:
        response_api = r.get(url=url)
        pokemon_info = response_api.json()
        pokemon_info = pokemon_info['abilities']
        pokemon_ability_list = [list(a.values())[0]['name'] for a in pokemon_info]
        ability_urls = [a['ability']['url'] for a in pokemon_info]
        for i,abilty in enumerate(pokemon_ability_list):
            effects = r.get(url=ability_urls[i])
            effects = effects.json()
            effects_text = effects['flavor_text_entries'][0]['flavor_text']
            effects_text = effects_text.replace('\n',' ')
            message = f'{abilty.title()}: {effects_text.title()}'
    except JSONDecodeError as i:
        print(f'Exception: {i}')   
        message = 'Esse Pokemon não existe'

    bot = context.bot
    await bot.send_message(chat_id=update.message.chat_id,text=message)   
    bot.send_message(chat_id=update.message.chat_id,text=f"O {pokemon[12:]} tem as seguintes habilidades:") 
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("habilidade", ability_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()

