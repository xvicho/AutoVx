import discord
import json
import os

config_file = open(f"{os.path.dirname(__file__)}/config.json")
config_data = json.load(config_file)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Login as {client.user}')

@client.event
async def on_message(message):
    if message.content.startswith("https") and message.content[8:17] != "vxtwitter":
        if message.content[8:15] == "twitter":

            new_url = message.content[:8] + "vxtwitter" + message.content[15:]
            await message.reply(new_url)
        elif message.content[8:9] == "x":

            new_url = message.content[:8] + "vxtwitter" + message.content[9:]
            await message.reply(new_url)

client.run(config_data["token"])
