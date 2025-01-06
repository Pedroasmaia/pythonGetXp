import discord
import os
from discord.ext import commands
from spotify import get_musics

TOKEN = os.getenv('DISCORD_TOKEN')

# Configurando intents
intents = discord.Intents.default()
intents.message_content = True  # Necessário para acessar o conteúdo das mensagens

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(name="playlist")
async def music_list(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        if ctx.voice_client is not None and ctx.voice_client.channel == channel:
            pass
        else:
            instance = await channel.connect()  
    await ctx.send("Gerando Playlist")
    musics = get_musics(ctx.message.content[10:])
    for music in musics:
        await ctx.send(f"{music}")
    await instance.disconnect()
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "olá" in message.content.lower():
        await message.channel.send(f"Olá, {message.author.name}!")
    
    await bot.process_commands(message)



bot.run(TOKEN)
