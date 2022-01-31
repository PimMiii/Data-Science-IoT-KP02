import datetime

import discord
from discord.ext import tasks
import asyncio
import logging

import time

# import config variables
from config import discord_bot_token, discord_bot_prefix, discord_channel_id
# import update_data()
from thingspeak_read import update_data

# setup logging for the bot
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8',
                              mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:'
                                       ' %(message)s'))
logger.addHandler(handler)

client = discord.Client()


# set the on_ready event
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use!")


# set the on_message events
@client.event
async def on_message(message):
    # ignore the bot's own messages
    if message.author == client.user:
        return

    # a simple hello command
    if message.content.startswith(discord_bot_prefix + 'hello'):
        await message.channel.send('Hello!')

    # print temperature and humidity as embed, on command temp
    if message.content.startswith(discord_bot_prefix + 'temp'):
        if 'data' not in globals():
            data = None
        data = update_data(data)
        embed = discord.Embed(
            title="Temperature",
            description="most recently reported temperature and humidity data",
            color=discord.Colour.dark_orange(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_author(
            name="ThingSpeak",
            icon_url="https://thingspeak.com/favicon-32x32.png"
        )
        embed.add_field(
            name="Temperature",
            value=str(data['field5']) +"°C",
            inline=True
        )
        embed.add_field(
            name="humidity",
            value=str(data['field6']) +"%",
            inline=True
        )
        embed.set_footer(
            text=client.user.name,
            icon_url=client.user.avatar_url
        )
        await message.channel.send(embed=embed)


@tasks.loop(seconds=15)
async def check_task_completion(self):
    if 'data' not in globals():
        data = None
    data = update_data(data)
    if data['field1'] == 1:
        channel = self.client.get_channel(discord_channel_id)
        message = "Goed Gedaan, je hebt een taak volbracht!"
        embed = discord.Embed(
            title="Taak",
            description="Meest recent volbrachte taak",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_author(
            name="ThingSpeak",
            icon_url="https://thingspeak.com/favicon-32x32.png"
        )
        embed.add_field(
            name="Taak looptijd",
            value=str(data['field4']) + "seconden",
            inline=False
        )
        embed.add_field(
            name="Taak begonnen",
            value=str(datetime.datetime.fromtimestamp(data['field2'])),
            inline=True
        )
        embed.add_field(
            name="Taak gefinisht",
            value=str(datetime.datetime.fromtimestamp(data['field2'])),
            inline=True
        )
        embed.set_footer(
            text=client.user.name,
            icon_url=client.user.avatar_url
        )
        await channel.send(message=message, embed=embed)
    else:
        print(data)


@check_task_completion.before_loop
async def before_checking(self):
    print('waiting')
    await self.client.wait_until_ready()


if __name__ == '__main__':
    check_task_completion.start(client)
    client.run(discord_bot_token)
