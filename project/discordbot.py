import discord
import asyncio
import logging

from config import discord_bot_token, discord_bot_prefix


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8',
                              mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:'
                                       ' %(message)s'))
logger.addHandler(handler)

client = discord.Client()

bot_prefix = "!"


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(discord_bot_prefix + 'hello'):
        await message.channel.send('Hello!')

if __name__ == '__main__':
    client.run(discord_bot_token)
