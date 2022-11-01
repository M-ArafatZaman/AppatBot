from censor.inappropriate_words import INAPPROPRIATE_WORDS
import re

def is_inappropriate(text: str) -> bool:
    '''
    Check if the text contains any inappropriate words
    '''
    for inapp_word in INAPPROPRIATE_WORDS:
        match = re.search(r"\b"+inapp_word+r"\b", text)
        if match:
            return True
            
    return False