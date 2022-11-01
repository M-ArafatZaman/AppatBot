'''
Mock a reply

Example:
    USER: [Appat] hi there
    Appat [Bot]: hI tHeRe
    Appat [Bot]: *Insert a random message from core/generate_reply.py* 
'''
from core.mock_message import mock_message
from core.generate_reply import generate_reply

async def mock_reply(message, _command):
    # Add LOSER reaction
    await message.add_reaction("🇱")
    await message.add_reaction("🇴")
    await message.add_reaction("🇸")
    await message.add_reaction("🇪")
    await message.add_reaction("🇷")

    # Mock reply
    await message.channel.send( mock_message(_command) )
    # Send a following reply
    await message.channel.send(generate_reply())
