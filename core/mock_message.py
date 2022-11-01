'''
A function which turns a text into mockery
'''
import random


def mock_message(message: str) -> str:
    choices = ("U", "L") # U means Uppercase, L means lowercase
    text = ""
    
    # Iterate through the message
    for i in message:

        # Flip a coin and decide
        if "".join(random.choices(choices)) == choices[0]:
            # If it is uppercase
            text += i.upper()

        else:
            # Else it is lowercase
            text += i.lower()

    return text
