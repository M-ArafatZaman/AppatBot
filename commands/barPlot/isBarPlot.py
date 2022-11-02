
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
        

    