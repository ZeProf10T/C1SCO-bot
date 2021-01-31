import os
#from dotenv import load_dotenv
import discord

# Récupération du token
#load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Création du client
client = discord.Client()
