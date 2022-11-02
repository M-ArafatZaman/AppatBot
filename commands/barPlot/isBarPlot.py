from typing import List

BAR_PLOT_PREFIX = "barplot"

def isBarPlot(command: str) -> bool:
    """ 
    This helper function determines if the command is a barPlot 

    For example - [Appat] barPlot 1,2,3,4
    *Returns True* 
    """

    # Remove whitespaces
    command = command.strip()

    if command.startswith( BAR_PLOT_PREFIX ):
        return True 
    
    else:
        return False


def extractBarPlotParameters(command: str) -> List[float]:
    """
    This helper function returns the parameters from the command

    Example:
        [Appat] barplot 1,2,3,4
        -> [1,2,3,4]
    """

    # Remove whitespaces and params
    command = command.strip()
    params: str = command[len(BAR_PLOT_PREFIX):].strip()

    parameters: List[str] = params.split(",")

    barPlotParameters: List[float] = [float(i) for i in parameters]

    return barPlotParameters
    