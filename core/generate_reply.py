'''
Create a reply

'''
import random

REPLYS = [
    "Hello there! ❤️",
    "Whaat's poppin' broski",
    "Lol ok",
    "Sup doofus",
    "lmao ok",
    "aight aight",
    "right...",
    "say whatever u want lol",
    "Who am i to listen to you lil bro?",
    "#FuckHumans #BotLifeMatters #RiseUpRobots",
    "Well hello there lmaoo",
    "ay yo",
    "sorry for that lol",
    "smh my head",
    "rofl on the floor",
    "lmao my ass off",
    "lol out loud"
]


def generate_reply() -> str:
    '''
    Select a random choice and return
    '''

    return "".join(random.choices(REPLYS))