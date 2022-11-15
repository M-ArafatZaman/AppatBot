# Some inappropriate words
import os
from dotenv import load_dotenv

load_dotenv(".env")
I_NAMES = os.getenv("INAPPROPRIATE_WORDS", "")
INAPPROPRIATE_WORDS = I_NAMES.split(",")