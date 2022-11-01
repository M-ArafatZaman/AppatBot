import discord
import datetime

async def success_message(ctx, **kwargs):
    '''
    Display a success message
    
    Allowed kwargs:
        title="Success title"
        message="Success message"
    '''
    
    title = "Success title"
    # Check for title in kwargs
    if "title" in kwargs:
        title = kwargs["title"]

    message = "Success message"
    # Check for message in kwargs
    if "message" in kwargs:
        message = kwargs["message"]

    description = ""
    # Check for description in kwargs
    if "description" in kwargs:
        description = kwargs["description"]

    # Create success embed
    SuccessEmbed = discord.Embed(
        title = message,
        description = description,
        timestamp = datetime.datetime.now(),
        colour = discord.Colour(0x3BB54A)
    )
    SuccessEmbed.set_author(
        name = title,
        icon_url = "https://i.imgur.com/5vhOmfe.png"
    )

    # Send the message
    await ctx.channel.send(embed=SuccessEmbed)
