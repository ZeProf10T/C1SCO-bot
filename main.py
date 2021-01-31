# bot.py
from lib.init import *
from lib import roles, message
import discord

@client.event
async def on_ready():
    print('Le Bot est prêt.')



# Lancement du client
client.run(TOKEN)
