'''
A function which checks if the command is provoked
'''

COMMAND_PREFIX: str = "[Appat]"

def is_command(message: str):
    '''
    If the command prefix is matched, return the rest of the parameters
    Else return None
    '''

    if message.lower().startswith( COMMAND_PREFIX.lower() ):
        return message[len(COMMAND_PREFIX):].strip()

    else:

        return None
