from time import sleep
from difflib import SequenceMatcher
import tatsoftTranslate as tt

class TatSpellCheck:
    all_words=set()
    def __init__(self):
        with open("wordlist.txt", "r") as f:
            for line in f:
                self.all_words.update(line.split())

    def spellcheck(self,tattext):
        rustext = tt.tat_to_rus(tattext)
        tattext = tattext.split(" ")
        rustext = rustext.split(" ")
        iter = 0
        for i in tattext:
            iter += 1
            ttr=tt.tat_to_rus(i).lower()
            rttttr=tt.rus_to_tat(ttr).lower()
            rata=SequenceMatcher(None, i.lower(), rttttr).ratio()
            ratb=SequenceMatcher(None, i.lower(), ttr).ratio()
            if rata<0.7 or ratb>0.95:
                return (iter, i)
        return (0, "")


