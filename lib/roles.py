from lib.init import *
from lib.env import *
import discord

@client.event
async def on_raw_reaction_add(payload):

    message_id = payload.message_id
    if message_id == MESSAGE_ROLE_REACTION:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    
        print(payload.emoji.name)
        # Match the emoji
        for emo, rol in EMOJI_TO_ROLES.items():
            if payload.emoji.name == emo:
                print("Add role", rol)
                role = discord.utils.get(guild.roles, name=rol)
                await payload.member.add_roles(role)



