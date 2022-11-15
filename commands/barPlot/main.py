import matplotlib.pyplot as plt
from .isBarPlot import extractBarPlotParameters
from typing import List
import io
import discord

async def barplot(ctx, _cmd: str):
    """
    This command sends an image of the barplot
    """

    # Generate x and y
    y: List[float] = extractBarPlotParameters(_cmd)
    x: List[int] = [i+1 for i in range(len(y))]

    # Plot data
    plt.bar(x, y, label="Numbers visualized")
    plt.legend(loc="upper right")
    fig = plt.gcf()

    # Create input buffer
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    fig.clear()
    plt.close()
    
    await ctx.channel.send(file=discord.File(buf, "plot.png"))
    buf.close()
