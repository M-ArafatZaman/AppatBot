'''
A discord bot for fun activites and banter

Author: Mohammad Arafat Zaman
'''
import discord
from commands.mock_reply import mock_reply
from commands.barPlot.isBarPlot import isBarPlot
from commands.barPlot import *
from core.is_command import is_command
from core.validation.success import success_message
from core.validation import error_message, warning_message, success_message
from Guilds.Podocast.initiate import test_embed
from censor.main import censor_message
from dotenv import load_dotenv
import os

load_dotenv(".env")

# Token, KEEP IT A SECRET
token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Event for when the bot has connected
@client.event
async def on_ready():
    print(f"{client.user} has connected to discord")

    # Change presence
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="[Appat] commands"))

    # Get a list of all the available guilds
    # for guild in client.guilds:
    #     print(f"Guild name: '{guild.name}'")
    #     print(f"Guild channels:")
    #     for channel in guild.channels:
    #         print(f"\tChannel name: '{channel.name}'")
    #         print("")


# On message
@client.event
async def on_message(message):
    # If the message is from the bot itself
    if message.author == client.user:
        return

    
    # Censor message
    await censor_message(message)

    # If the message is requested to the bot, prefix = "[Appat]"
    _command = is_command(message.content)

    if _command == "test_embed()":
        await test_embed(message)

    elif _command == "preview_success()":
        await success_message(message)

    elif _command == "preview_warning()":
        await warning_message(message)
    
    elif _command == "preview_error()":
        await error_message(message)

    # The command is a barplot command
    elif isBarPlot(_command):
        print(extractBarPlotParameters(_command))

    # Else just mock
    elif _command:
        await mock_reply(message, _command)


client.run(token)