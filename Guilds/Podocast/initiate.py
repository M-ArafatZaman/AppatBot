'''
Initiate the messages
'''
import discord
import datetime

async def test_embed(message):
    embed_text = discord.Embed(
        title="Hello there! 😁",
        description="How are you doing <@678622647118200855>? I hope you are doing great 😁\n\nThis is amazing \n",
        colour=discord.Colour.blue(),
        timestamp=datetime.datetime.now()
    )

    embed_text.set_footer(text="Arafat (c) 2020")
    embed_text.set_author(
        name="Appat",
        icon_url="https://cdn.discordapp.com/app-icons/736160654561509407/7ff9ba09d5af47d54df58ff9a59ba494.png"
    )

    await message.channel.send(embed=embed_text)