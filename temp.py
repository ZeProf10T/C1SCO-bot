


# Création du client
client = discord.Client()


# Listes des commandes
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('.hello'):
        await message.channel.send('Hello!')


# https://github.com/Rapptz/discord.py/blob/master/examples/reaction_roles.py
class RoleReactClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_message_id = 805174002267717693  # ID of message that can be reacted to to add role
        self.emoji_to_role = {
            ":heart:": 805154812785065985,  # ID of role associated with partial emoji object 'partial_emoji_1'
            ":upside_down:": 805157001666756619 # ID of role associated with partial emoji object 'partial_emoji_2'
        }

    async def on_raw_reaction_add(self, payload):
        """Gives a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about
        if payload.message_id != self.role_message_id:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally add the role
            await payload.member.add_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

    async def on_raw_reaction_remove(self, payload):
        """Removes a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about
        if payload.message_id != self.role_message_id:
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        guild = self.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        member = guild.get_member(payload.user_id)
        if member is None:
            # Makes sure the member still exists and is valid
            return

        try:
            # Finally, remove the role
            await member.remove_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass


# This bot requires the members and reactions intents.
intents = discord.Intents.default()
intents.members = True
client = RoleReactClient(intents=intents)


if contenu.find('thierry') != -1:
        await message.channel.send("Thierry ? C'est le boss en fait !")
    elif contenu.find('ping') != -1:
        await message.channel.send('PONG !')
    elif contenu.find('bernard') != -1 or contenu.find('helly') != -1:
        await message.channel.send('EH OH revise tes equa-diff !')
    elif contenu.find('sebastien') != -1 or contenu.find('sébastien') != -1:
        await message.channel.send('Sébastien ? Il fait des Opé Sponso Cisco !')


if message.content.startswith('.clear'):
        number_of_message = int(message.content.split(" ")[1])

        messages = await message.channel.history(limit=number_of_message).flatten()
        
        for mes in messages:
            await mes.delete()


@client.event
async def on_raw_reaction_remove(payload):


    message_id = payload.message_id
    if message_id == MESSAGE_ROLE_REACTION:
        guild = client.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name="2017")
        member = guild.get_member(payload.user_id)
        await member.remove_roles(role)