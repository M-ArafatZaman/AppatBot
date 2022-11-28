from .isBarPlot import extractBarPlotParameters
from typing import List
import io
import discord
import requests
from core.validation.error import error_message

async def barplot(ctx: discord.Message, _cmd: str):
    """
    This command sends an image of the barplot
    """

    ENDPOINT = "https://funapi.onrender.com/api/barplot/"

    # Generate y
    
    # Try parsing the parameters
    try:
        y: List[float] = extractBarPlotParameters(_cmd)

        # Parse is successful, send request
        y_str: List[str] = [str(i) for i in y]
        resp = requests.get(f'{ENDPOINT}?data={",".join(y_str)}')

        if resp.status_code == 200 and resp.headers["Content-Type"] == "image/png":
            # Got successful image return
            buffer = io.BytesIO(resp.content)
            image = discord.File(buffer, "plot.png")
            
            # Send image
            await ctx.channel.send(file=image)

            # Close buffer
            buffer.close()

    except Exception:
        await error_message(
            ctx,
            title="Invalid usage", 
            message="Please enter numeric parameters"
        )
        return

