from lib.init import *
from lib.env import *
import discord

from datetime import datetime

@client.event
async def on_message(message):
    if message.author == client.user:
        return


    #############
    # COMMANDES #
    #############


    # Obtenir la date (.date)
    if message.content.startswith('.date'):
        jour = datetime.now().day
        mois = datetime.now().month
        annee = datetime.now().year
        await message.channel.send(f"Nous sommes le : {jour}/{mois}/{annee}")

    # Obtenir l'heure (.heure)
    if message.content.startswith('.heure'):
        heure = datetime.now().hour + 1 # Décallage horaire d'une heure
        minute = datetime.now().minute
        await message.channel.send(f"Il est : {heure}H{minute}")

    # Clean du channel :
    if message.content.startswith('.clear'):
        number_of_message = int(message.content.split(" ")[1])

        messages = await message.channel.history(limit=number_of_message + 1).flatten()
        for mes in messages:
            await mes.delete()

    ################
    # Easters Eggs #
    ################
    contenu = message.content.lower()
    for key, value in EASTER_EGGS.items():
        if contenu.find(key) != -1:
            await message.channel.send(value)
