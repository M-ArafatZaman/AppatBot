import discord
import datetime

async def error_message(ctx, **kwargs):
    '''
    Display a error message
    
    Allowed kwargs:
        title="Error title"
        message="Error message"
    '''
    
    title = "Error title"
    # Check for title in kwargs
    if "title" in kwargs:
        title = kwargs["title"]

    message = "Error message"
    # Check for message in kwargs
    if "message" in kwargs:
        message = kwargs["message"]

    description = ""
    # Check for description in kwargs
    if "description" in kwargs:
        description = kwargs["description"]

    # Create error embed
    ErrorEmbed = discord.Embed(
        title = message,
        description = description,
        timestamp = datetime.datetime.now(),
        colour = discord.Colour(0xEF440E)
    )
    ErrorEmbed.set_author(
        name = title,
        icon_url = "https://i.imgur.com/UjdPxZw.png"
    )

    # Send the message
    await ctx.channel.send(embed=ErrorEmbed)
