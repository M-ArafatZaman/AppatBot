import discord
import datetime

async def warning_message(ctx, **kwargs):
    '''
    Display a warning message
    
    Allowed kwargs:
        title="Warning title"
        message="Warning message"
        description=""
    '''
    
    title = "Warning title"
    # Check for title in kwargs
    if "title" in kwargs:
        title = kwargs["title"]

    message = "Warning message"
    # Check for message in kwargs
    if "message" in kwargs:
        message = kwargs["message"]
        
    description = ""
    # Check for description in kwargs
    if "description" in kwargs:
        description = kwargs["description"]

    # Create warning embed
    WarningEmbed = discord.Embed(
        title = message,
        description = description,
        timestamp = datetime.datetime.now(),
        colour = discord.Colour(0xF5EE1A)
    )
    WarningEmbed.set_author(
        name = title,
        #icon_url = "https://i.imgur.com/gin6QcD.png"
        icon_url = "https://i.imgur.com/K7AwQbe.png"
    )

    # Send the message
    await ctx.channel.send(embed=WarningEmbed)
