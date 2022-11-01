from censor.inappropriate_words import INAPPROPRIATE_WORDS
import re

def sanitize_text(text: str) -> str:
    '''
    Replaces any inappropriate words with [CENSORED]
    '''
    for inapp_word in INAPPROPRIATE_WORDS:
        text = re.sub(r"\b"+inapp_word+r"\b", "[CENSORED]", text)

    return text