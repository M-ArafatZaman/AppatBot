from censor.is_inappropriate import is_inappropriate
from core.validation import warning_message

async def censor_message(ctx):
    '''
    Check if the message is in appropriate
    If so, warn the user
    '''

    if is_inappropriate(ctx.content):

        description = f"Hey {ctx.author.mention}! Please refrain from using bad language!"

        # React with ⚠️
        await ctx.add_reaction("⚠️")

        # Warn
        await warning_message(ctx,
            title="Warning!",
            message=None,
            description=description
        )