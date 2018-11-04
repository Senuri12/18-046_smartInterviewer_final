from Controller import ginger
from difflib import SequenceMatcher

def grammerMarks(a):

    fixedAnswer = ginger.checker(a)
    print(fixedAnswer)
    precentage = SequenceMatcher(None, a, fixedAnswer).ratio()
    return precentage
